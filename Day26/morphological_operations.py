
import cv2
import numpy as np
import os

# 1. Get Day26 folder location
base_folder = os.path.dirname(os.path.abspath(__file__))

# Input image path
image_path = os.path.join(
    base_folder, "input_images", "document1.jpg"
)

# Output folder path
output_folder = os.path.join(
    base_folder, "output_images"
)

# Create output folder
os.makedirs(output_folder, exist_ok=True)

# 2. Read image
image = cv2.imread(image_path)

if image is None:
    print("Image not found!")
    exit()

print("Image loaded successfully!")

# 3. Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 4. Convert to binary image
_, binary = cv2.threshold(
    gray, 127, 255, cv2.THRESH_BINARY
)

# 5. Create kernel
kernel = np.ones((5, 5), np.uint8)

# 6. Erosion
erosion = cv2.erode(binary, kernel, iterations=1)

# 7. Dilation
dilation = cv2.dilate(binary, kernel, iterations=1)

# 8. Opening
opening = cv2.morphologyEx(
    binary, cv2.MORPH_OPEN, kernel
)

# 9. Closing
closing = cv2.morphologyEx(
    binary, cv2.MORPH_CLOSE, kernel
)

# 10. Morphological Gradient
gradient = cv2.morphologyEx(
    binary, cv2.MORPH_GRADIENT, kernel
)

# 11. Top Hat
top_hat = cv2.morphologyEx(
    binary, cv2.MORPH_TOPHAT, kernel
)

# 12. Black Hat
black_hat = cv2.morphologyEx(
    binary, cv2.MORPH_BLACKHAT, kernel
)

# 13. Display results
cv2.imshow("Original Binary", binary)
cv2.imshow("Erosion", erosion)
cv2.imshow("Dilation", dilation)
cv2.imshow("Opening", opening)
cv2.imshow("Closing", closing)
cv2.imshow("Gradient", gradient)
cv2.imshow("Top Hat", top_hat)
cv2.imshow("Black Hat", black_hat)

# 14. Save all images in Day26/output_images

cv2.imwrite(os.path.join(output_folder, "binary.jpg"), binary)
cv2.imwrite(os.path.join(output_folder, "erosion.jpg"), erosion)
cv2.imwrite(os.path.join(output_folder, "dilation.jpg"), dilation)
cv2.imwrite(os.path.join(output_folder, "opening.jpg"), opening)
cv2.imwrite(os.path.join(output_folder, "closing.jpg"), closing)
cv2.imwrite(os.path.join(output_folder, "gradient.jpg"), gradient)
cv2.imwrite(os.path.join(output_folder, "top_hat.jpg"), top_hat)
cv2.imwrite(os.path.join(output_folder, "black_hat.jpg"), black_hat)

# 15. Finish
print("All morphological operations completed!")

print("Images saved in:", output_folder)

cv2.waitKey(0)
cv2.destroyAllWindows()
