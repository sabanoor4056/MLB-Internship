
import cv2
import numpy as np
import os

# Get the current script location
base_folder = os.path.dirname(os.path.abspath(__file__))

# Input and output folders
input_folder = os.path.join(base_folder, "..", "input_images")
output_folder = os.path.join(base_folder, "..", "output_images")

# Create output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Arrange four document corners in correct order
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

    for contour in contours[:10]:

        perimeter = cv2.arcLength(contour, True)

        approx = cv2.approxPolyDP(
            contour,
            0.02 * perimeter,
            True
        )

        if len(approx) == 4:

            points = approx.reshape(4, 2)
            points = order_points(points)

            top_left, top_right, bottom_right, bottom_left = points

            width = int(max(
                np.linalg.norm(bottom_right - bottom_left),
                np.linalg.norm(top_right - top_left)
            ))

            height = int(max(
                np.linalg.norm(top_right - bottom_right),
                np.linalg.norm(top_left - bottom_left)
            ))

            if width < 2 or height < 2:
                break

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

    # If corners are not detected, keep original image
    return img


# Enhance document
def enhance_document(img):

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Reduce noise
    denoised = cv2.bilateralFilter(gray, 9, 75, 75)

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

    sharp = cv2.filter2D(bright, -1, kernel)

    return sharp


# Process all document images
if not os.path.exists(input_folder):
    print("Input folder not found:", input_folder)
    exit()

print("Input folder found!")
print("Output folder:", output_folder)
for filename in os.listdir(input_folder):

    if filename.lower().endswith(
        (".jpg", ".jpeg", ".png")
    ):

        image_path = os.path.join(input_folder, filename)

        img = cv2.imread(image_path)

        if img is None:
            print("Could not read:", filename)
            continue

        # Step 1: Perspective correction
        corrected = correct_perspective(img)

        # Step 2: Save corrected image
        corrected_path = os.path.join(
            output_folder, "corrected_" + filename
        )

        cv2.imwrite(corrected_path, corrected)

        # Step 3: Enhance document
        enhanced = enhance_document(corrected)

        # Step 4: Save final image
        enhanced_path = os.path.join(
            output_folder, "enhanced_" + filename
        )

        cv2.imwrite(enhanced_path, enhanced)

        print("Processed:", filename)

print("All images processed successfully!")
