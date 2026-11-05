
import cv2
import numpy as np
import os

# Get the current script folder
current_folder = os.path.dirname(os.path.abspath(__file__))

# Go to input_images folder
image_path = os.path.join(
    current_folder,
    "..",
    "input_images",
    "image.jpg"
)

# Read image
img = cv2.imread(image_path)

if img is None:
    print("Image not found! Check image name and location.")
    exit()

print("Image loaded successfully!")

height, width = img.shape[:2]

points1 = np.float32([
    [50, 50],
    [200, 50],
    [50, 200]
])

points2 = np.float32([
    [10, 100],
    [200, 50],
    [100, 250]
])

matrix = cv2.getAffineTransform(points1, points2)

result = cv2.warpAffine(img, matrix, (width, height))

cv2.imshow("Original Image", img)
cv2.imshow("Affine Transformation", result)

cv2.imwrite(
    os.path.join(current_folder, "..", "output_images", "affine.jpg"),
    result
)

cv2.waitKey(0)
cv2.destroyAllWindows()





import cv2
import os

# Get current folder
print("Current folder:", os.getcwd())

# Correct image path
image_path = r"C:\Users\saban\OneDrive\Documents\MLB-Internship\MLB-Internship\Day25\input_images\tilted_document.jpg"

# Check image
print("Image exists:", os.path.exists(image_path))

# Read image
img = cv2.imread(image_path)

if img is None:
    print("Image not found!")

else:
    print("Image loaded successfully!")

    cv2.imshow("My Document", img)
    cv2.imwrite(
    os.path.join(current_folder, "..", "output_images", "tilted_document.jpg"),
    result
)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
