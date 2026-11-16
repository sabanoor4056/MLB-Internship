
import cv2
import easyocr
import os

# Find the Day29 project folder
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Image path
image_path = os.path.join(
    BASE_DIR, "input_images", "document.jpg"
)

# Output path
output_path = os.path.join(
    BASE_DIR, "output_text", "enhanced_image.jpg"
)

# Create OCR reader
reader = easyocr.Reader(['en'], gpu=False)

# Read image
image = cv2.imread(image_path)

if image is None:
    print("Image not found!")
    print("Expected location:", image_path)
    exit()

# Convert to grayscale
gray = cv2.cvtColor(
    image, cv2.COLOR_BGR2GRAY
)

# Improve contrast
enhanced = cv2.equalizeHist(gray)

# Save enhanced image
os.makedirs(os.path.dirname(output_path), exist_ok=True)

cv2.imwrite(output_path, enhanced)

# OCR on original image
print("\nOriginal Image Result:")

original_result = reader.readtext(
    image, detail=0
)

print("\n".join(original_result))

# OCR on enhanced image
print("\nEnhanced Image Result:")

enhanced_result = reader.readtext(
    enhanced, detail=0
)

print("\n".join(enhanced_result))

print("\nEnhanced image saved successfully!")
