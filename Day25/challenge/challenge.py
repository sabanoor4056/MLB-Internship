
import cv2
import numpy as np
import os

# Get the correct Day25 folder
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Input and output folders
input_folder = os.path.join(BASE_DIR, "input_images")
output_folder = os.path.join(BASE_DIR, "challenge_output")

os.makedirs(output_folder, exist_ok=True)


# Arrange four document corners
def order_points(points):

    rect = np.zeros((4, 2), dtype="float32")

    total = points.sum(axis=1)
    rect[0] = points[np.argmin(total)]
    rect[2] = points[np.argmax(total)]

    diff = np.diff(points, axis=1)
    rect[1] = points[np.argmin(diff)]
    rect[3] = points[np.argmax(diff)]

    return rect


# Correct document perspective
def correct_perspective(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 50, 150)

    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE
    )

    contours = sorted(
        contours,
        key=cv2.contourArea,
        reverse=True
    )

    for contour in contours[:15]:

        perimeter = cv2.arcLength(contour, True)

        approx = cv2.approxPolyDP(
            contour, 0.02 * perimeter, True
        )

        if len(approx) == 4:

            points = order_points(
                approx.reshape(4, 2)
            )

            tl, tr, br, bl = points

            width = int(max(
                np.linalg.norm(br - bl),
                np.linalg.norm(tr - tl)
            ))

            height = int(max(
                np.linalg.norm(tr - br),
                np.linalg.norm(tl - bl)
            ))

            if width < 2 or height < 2:
                continue

            new_points = np.float32([
                [0, 0],
                [width - 1, 0],
                [width - 1, height - 1],
                [0, height - 1]
            ])

            matrix = cv2.getPerspectiveTransform(
                points, new_points
            )

            corrected = cv2.warpPerspective(
                img, matrix, (width, height)
            )

            return corrected

    print("Corners not detected. Original image used.")
    return img


# Enhance document
def enhance_document(img):

    # Convert to grayscale
    gray = cv2.cvtColor(
        img, cv2.COLOR_BGR2GRAY
    )

    # Remove noise
    denoised = cv2.bilateralFilter(
        gray, 9, 75, 75
    )

    # Improve contrast
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    contrast = clahe.apply(denoised)

    # Improve brightness
    bright = cv2.convertScaleAbs(
        contrast, alpha=1.1, beta=10
    )

    # Sharpen image
    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    sharp = cv2.filter2D(
        bright, -1, kernel
    )

    return sharp


# Find document images
images = [
    file for file in os.listdir(input_folder)
    if file.lower().endswith((".jpg", ".jpeg", ".png"))
]

# Select only three images
images = sorted(images)[:3]

if len(images) == 0:
    print("No images found in input_images folder!")

else:

    print("Total images found:", len(images))

    for i, filename in enumerate(images, start=1):

        image_path = os.path.join(
            input_folder, filename
        )

        img = cv2.imread(image_path)

        if img is None:
            print("Cannot read:", filename)
            continue

        # Create image folder
        folder = os.path.join(
            output_folder, f"image{i}"
        )

        os.makedirs(folder, exist_ok=True)

        # Save original
        cv2.imwrite(
            os.path.join(folder, "original.jpg"),
            img
        )

        # Correct perspective
        corrected = correct_perspective(img)

        cv2.imwrite(
            os.path.join(folder, "corrected.jpg"),
            corrected
        )

        # Enhance document
        enhanced = enhance_document(corrected)

        cv2.imwrite(
            os.path.join(folder, "enhanced.jpg"),
            enhanced
        )

        print("Successfully processed:", filename)

    print("\nChallenge completed!")
    print("Check your challenge_output folder.")
