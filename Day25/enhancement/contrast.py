
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

# Increase contrast
result = cv2.convertScaleAbs(img, alpha=1.5, beta=0)

cv2.imshow("Original", img)
cv2.imshow("High Contrast", result)

cv2.imwrite("../output_images/contrast.jpg", result)
cv2.imwrite(os.path.join(output_folder, "contrast.jpg"), result)

print("Images saved successfully!")
cv2.waitKey(0)
cv2.destroyAllWindows()
