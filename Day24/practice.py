
import cv2
import os
from datetime import date

import os

# Get the folder where practice.py is saved
base_folder = os.path.dirname(os.path.abspath(__file__))

# Input and output folder paths
input_folder = os.path.join(base_folder, "input_images")
output_folder = os.path.join(base_folder, "output")

os.makedirs(output_folder, exist_ok=True)

# Create output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Today's date
today = date.today().strftime("%Y-%m-%d")

# Read all images from input folder
image_files = [
    file for file in os.listdir(input_folder)
    if file.lower().endswith((".jpg", ".jpeg", ".png"))
]
print("Found images:", image_files)
# Process each image
for image_file in image_files:

    print("\nProcessing:", image_file)

    # Read image
    image_path = os.path.join(input_folder, image_file)
    image = cv2.imread(image_path)

    if image is None:
        print("Image could not be loaded:", image_file)
        continue

    # Create separate output folder for each image
    image_name = os.path.splitext(image_file)[0]
    save_folder = os.path.join(output_folder, image_name)
    os.makedirs(save_folder, exist_ok=True)

    # 1. Display image information
    height, width = image.shape[:2]
    channels = image.shape[2] if len(image.shape) == 3 else 1
    file_size = os.path.getsize(image_path) / 1024

    print("Image Name:", image_file)
    print("Width:", width)
    print("Height:", height)
    print("Channels:", channels)
    print("File Size:", round(file_size, 2), "KB")

    # Save original image
    cv2.imwrite(os.path.join(save_folder, "original.jpg"), image)

    # 2. Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(os.path.join(save_folder, "grayscale.jpg"), gray)

    # 3. Resize image
    small = cv2.resize(image, (width // 2, height // 2))
    large = cv2.resize(image, (width * 2, height * 2))

    cv2.imwrite(os.path.join(save_folder, "small.jpg"), small)
    cv2.imwrite(os.path.join(save_folder, "large.jpg"), large)

    # 4. Crop different regions
    center_crop = image[
        height // 4: 3 * height // 4,
        width // 4: 3 * width // 4
    ]

    top_left_crop = image[
        0: height // 2,
        0: width // 2
    ]

    cv2.imwrite(os.path.join(save_folder, "center_crop.jpg"), center_crop)
    cv2.imwrite(os.path.join(save_folder, "top_left_crop.jpg"), top_left_crop)

    # 5. Rotate image
    rotate_90 = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    rotate_180 = cv2.rotate(image, cv2.ROTATE_180)
    rotate_270 = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)

    cv2.imwrite(os.path.join(save_folder, "rotate_90.jpg"), rotate_90)
    cv2.imwrite(os.path.join(save_folder, "rotate_180.jpg"), rotate_180)
    cv2.imwrite(os.path.join(save_folder, "rotate_270.jpg"), rotate_270)

    # 6. Flip image
    horizontal = cv2.flip(image, 1)
    vertical = cv2.flip(image, 0)

    cv2.imwrite(os.path.join(save_folder, "horizontal_flip.jpg"), horizontal)
    cv2.imwrite(os.path.join(save_folder, "vertical_flip.jpg"), vertical)

    # 7. Draw shapes
    shapes = image.copy()

    # Rectangle
    cv2.rectangle(shapes, (20, 20), (width // 2, height // 2),
                  (0, 255, 0), 3)

    # Circle
    cv2.circle(shapes, (width // 2, height // 2), 50,
               (255, 0, 0), 3)

    # Line
    cv2.line(shapes, (0, 0), (width - 1, height - 1),
             (0, 0, 255), 3)

    # Polygon
    points = [
        [width // 2, 20],
        [width - 20, height // 2],
        [width // 2, height - 20],
        [20, height // 2]
    ]

    import numpy as np
    points = np.array(points, dtype=np.int32)
    cv2.polylines(shapes, [points], True, (0, 255, 255), 3)

    # Add name and date
    cv2.putText(
        shapes,
        "Saba Noor " + today,
        (20, height - 20),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2
    )

    cv2.imwrite(os.path.join(save_folder, "shapes_and_text.jpg"), shapes)

    print("All operations completed for:", image_file)

print("\nAll images processed successfully!")
print("Check the output folder.")
