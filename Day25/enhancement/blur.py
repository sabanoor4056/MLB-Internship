
import cv2
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


# Gaussian Blur
gaussian = cv2.GaussianBlur(img, (5, 5), 0)

# Median Blur
median = cv2.medianBlur(img, 5)

# Bilateral Filter
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

cv2.imshow("Original", img)
cv2.imshow("Gaussian Blur", gaussian)
cv2.imshow("Median Blur", median)
cv2.imshow("Bilateral Filter", bilateral)

cv2.imwrite("../output_images/gaussian.jpg", gaussian)
cv2.imwrite("../output_images/median.jpg", median)
cv2.imwrite("../output_images/bilateral.jpg", bilateral)
cv2.imwrite(os.path.join(output_folder, "gaussian.jpg"), gaussian)
cv2.imwrite(os.path.join(output_folder, "median.jpg"), median)
cv2.imwrite(os.path.join(output_folder, "bilateral.jpg"), bilateral)
print("Images saved successfully!")
cv2.waitKey(0)
cv2.destroyAllWindows()
