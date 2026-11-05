
import cv2
import numpy as np
import os

# Find Day25 folder automatically
day_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Input and output folders
input_folder = os.path.join(day_folder, "input_images")
output_folder = os.path.join(day_folder, "output_images")

os.makedirs(output_folder, exist_ok=True)

# Try reading document.jpg first
image_path = os.path.join(input_folder, "document.jpg")

img = cv2.imread(image_path)

# If document.jpg cannot be read, try image.jpg
if img is None:
    image_path = os.path.join(input_folder, "image.jpg")
    img = cv2.imread(image_path)

# Check image
if img is None:
    print("Unable to read image!")
    print("Please check the image file.")
    exit()

print("Image loaded successfully!")
print("Image name:", os.path.basename(image_path))

# Get image dimensions
height, width = img.shape[:2]

# Translation matrix
matrix = np.float32([
    [1, 0, 100],
    [0, 1, 50]
])

# Apply translation
result = cv2.warpAffine(img, matrix, (width, height))

# Show images
cv2.imshow("Original Image", img)
cv2.imshow("Translated Image", result)

# Save result
output_path = os.path.join(output_folder, "translated.jpg")

cv2.imwrite(output_path, result)

print("Translation completed!")
print("Saved at:", output_path)

cv2.waitKey(0)
cv2.destroyAllWindows()
