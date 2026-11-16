
import easyocr
import cv2
import os
from PIL import Image

# Initialize EasyOCR
reader = easyocr.Reader(['en'], gpu=False)


def extract_text(image_path):

    # Check if image exists
    if not os.path.exists(image_path):
        print("Image not found!")
        return

    # Read image
    image = cv2.imread(image_path)

    if image is None:
        print("Could not open image!")
        return

    # Display original image using Pillow
    original_image = Image.open(image_path)
    original_image.show()

    # Extract text using EasyOCR
    results = reader.readtext(image_path, detail=0)

    extracted_text = "\n".join(results)

    # Display extracted text
    print("\nExtracted Text:")
    print("-------------------------")
    print(extracted_text)

    # Get Day29 main folder path
    base_folder = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    # Use existing output_text folder
    output_folder = os.path.join(
        base_folder, "output_text"
    )

    # Save extracted text
    output_path = os.path.join(
        output_folder, "extracted_text.txt"
    )

    with open(
        output_path, "w", encoding="utf-8"
    ) as file:
        file.write(extracted_text)

    print("\nText saved successfully!")
    print("Saved location:", output_path)


# Ask user for image path
path = input("Enter image path: ")

extract_text(path)
