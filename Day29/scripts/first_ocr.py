
import easyocr
import os

# Create the OCR reader
reader = easyocr.Reader(['en'], gpu=False)

# Find the Day29 project folder automatically
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Image location
image_path = os.path.join(
    BASE_DIR,
    "input_images",
    "document.jpg"
)

# Check whether image exists
if not os.path.exists(image_path):
    print("ERROR: Image not found!")
    print("Expected image location:", image_path)

else:
    # Extract text from image
    results = reader.readtext(image_path)

    print("\nExtracted Text:\n")

    for result in results:
        print(result[1])

    print("\nOCR completed successfully!")
