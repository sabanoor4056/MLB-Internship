
import cv2
import numpy as np
import os
# Find the Day25 folder
base_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Image path
image_path = os.path.join(base_folder, "input_images", "image.jpg")

# Output folder
output_folder = os.path.join(base_folder, "output_images")
os.makedirs(output_folder, exist_ok=True)

# Read image
img = cv2.imread(image_path)

if img is None:
    print("Image not found!")
    print("Check your image name and input_images folder.")
    exit()

# Sharpening filter
kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

sharp = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original", img)
cv2.imshow("Sharpened", sharp)

cv2.imwrite("../output_images/sharpened.jpg", sharp)
cv2.imwrite(os.path.join(output_folder, "sharpened.jpg"), sharp)
print("Images saved successfully!")
cv2.waitKey(0)
cv2.destroyAllWindows()
