
import cv2
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

# Create output folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# 2. Read Image
image = cv2.imread(image_path)

if image is None:
    print("Image not found! Check input_images folder.")
    exit()

print("Image loaded successfully!")

# 3. Convert to Grayscale


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)

cv2.imwrite(
    os.path.join(output_folder, "grayscale.jpg"), gray
)

# 4. Apply Gaussian Blur

blur = cv2.GaussianBlur(gray, (5, 5), 0)

cv2.imshow("Gaussian Blur", blur)

cv2.imwrite(
    os.path.join(output_folder, "blur.jpg"), blur
)

# 5. Sobel Edge Detection

# Sobel X
sobel_x = cv2.Sobel(
    blur, cv2.CV_64F, 1, 0, ksize=3
)

# Sobel Y
sobel_y = cv2.Sobel(
    blur, cv2.CV_64F, 0, 1, ksize=3
)

# Convert images
sobel_x = cv2.convertScaleAbs(sobel_x)
sobel_y = cv2.convertScaleAbs(sobel_y)

# Combine X and Y
sobel = cv2.addWeighted(
    sobel_x, 0.5, sobel_y, 0.5, 0
)

cv2.imshow("Sobel X", sobel_x)
cv2.imshow("Sobel Y", sobel_y)
cv2.imshow("Sobel Combined", sobel)

cv2.imwrite(
    os.path.join(output_folder, "sobel.jpg"), sobel
)

# 6. Laplacian Edge Detection


laplacian = cv2.Laplacian(
    blur, cv2.CV_64F
)

laplacian = cv2.convertScaleAbs(laplacian)

cv2.imshow("Laplacian Edges", laplacian)

cv2.imwrite(
    os.path.join(output_folder, "laplacian.jpg"),
    laplacian
)


# 7. Canny Edge Detection


canny = cv2.Canny(blur, 50, 150)

cv2.imshow("Canny Edges", canny)

cv2.imwrite(
    os.path.join(output_folder, "canny.jpg"), canny
)

# 8. Finish
print("All operations completed successfully!")
print("All images saved in Day26/output_images folder.")

cv2.waitKey(0)
cv2.destroyAllWindows()
