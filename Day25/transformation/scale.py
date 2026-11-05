import cv2
import os

# Get the folder where this Python file is saved
base_folder = os.path.dirname(os.path.abspath(__file__))

# Correct input image path
image_path = os.path.join(base_folder, "..", "input_images", "image.jpg")

# Correct output folder path
output_folder = os.path.join(base_folder, "..", "output_images")

# Create output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Read image
img = cv2.imread(image_path)

if img is None:
    print("Image not found! Please check your image.")
else:
    # Resize image
    resized = cv2.resize(img, (400, 300))

    # Save image in output_images
    output_path = os.path.join(output_folder, "scaled_image.jpg")
    cv2.imwrite(output_path, resized)

    print("Image saved successfully!")
    print("Saved at:", output_path)