
import cv2
import os

# Find the project folder
base_folder = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Image path
image_path = os.path.join(
    base_folder, "input_images", "image.jpg"
)

# Output folder
output_folder = os.path.join(
    base_folder, "output_images"
)

os.makedirs(output_folder, exist_ok=True)

# Read image
img = cv2.imread(image_path)

if img is None:
    print("Image not found!")
    print("Check your image name and folder.")
    exit()

# Get image dimensions
height, width = img.shape[:2]

# Find center
center = (width // 2, height // 2)

# Rotate by 45 degrees
matrix = cv2.getRotationMatrix2D(center, 45, 1)

rotated = cv2.warpAffine(
    img, matrix, (width, height)
)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Rotated Image", rotated)

# Save image
cv2.imwrite(
    os.path.join(output_folder, "rotated.jpg"),
    rotated
)

print("Image rotated successfully!")

cv2.waitKey(0)
cv2.destroyAllWindows()
