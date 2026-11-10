
import cv2
import numpy as np
import os
import shutil


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

input_folder = os.path.join(BASE_DIR, "mini_input")
output_folder = os.path.join(BASE_DIR, "mini_output")


edge_folder = os.path.join(output_folder, "edges")
morph_folder = os.path.join(output_folder, "morphology")
final_folder = os.path.join(output_folder, "final")

# Create output folders
os.makedirs(edge_folder, exist_ok=True)
os.makedirs(morph_folder, exist_ok=True)
os.makedirs(final_folder, exist_ok=True)

# Create kernel
kernel = np.ones((5, 5), np.uint8)

# Read all images
images = os.listdir(input_folder)

# Process each image
for filename in images:

    if not filename.lower().endswith(
        (".jpg", ".jpeg", ".png")
    ):
        continue

    image_path = os.path.join(input_folder, filename)

    # Load original image
    image = cv2.imread(image_path)

    if image is None:
        print("Cannot read:", filename)
        continue

    print("Processing:", filename)

    # Step 1: Grayscale
    gray = cv2.cvtColor(
        image, cv2.COLOR_BGR2GRAY
    )

    # Step 2: Gaussian Blur
    blur = cv2.GaussianBlur(
        gray, (5, 5), 0
    )

    # Step 3: Canny Edge Detection
    edges = cv2.Canny(
        blur, 50, 150
    )

    # Save edge result
    cv2.imwrite(
        os.path.join(edge_folder, filename),
        edges
    )

    # Step 4: Morphological Closing
    morph = cv2.morphologyEx(
        edges,
        cv2.MORPH_CLOSE,
        kernel,
        iterations=2
    )

    # Save morphology result
    cv2.imwrite(
        os.path.join(morph_folder, filename),
        morph
    )

    # Step 5: Find contours
    contours, hierarchy = cv2.findContours(
        morph,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Step 6: Find largest contour
    if len(contours) > 0:

        largest_contour = max(
            contours, key=cv2.contourArea
        )

        # Calculate perimeter
        perimeter = cv2.arcLength(
            largest_contour, True
        )

        # Approximate contour
        approx = cv2.approxPolyDP(
            largest_contour,
            0.02 * perimeter,
            True
        )

        # Draw detected boundary
        if len(approx) == 4:
            cv2.drawContours(
                image, [approx], -1,
                (0, 255, 0), 3
            )
        else:
            cv2.drawContours(
                image, [largest_contour], -1,
                (0, 255, 0), 3
            )

        print("Boundary detected:", filename)

    else:
        print("No boundary found:", filename)

    # Step 7: Save final image
    cv2.imwrite(
        os.path.join(final_folder, filename),
        image
    )

print("All images processed successfully!")
