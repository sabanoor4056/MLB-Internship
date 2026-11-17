
import cv2
import os
import numpy as np

# Input and output folders
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INPUT_FOLDER = os.path.join(BASE_DIR, "input_images")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output_images")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def segment_image(image_path):

    # 1. Read image
    image = cv2.imread(image_path)

    if image is None:
        raise ValueError("Image could not be loaded")

    # 2. Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 3. Binary Thresholding
    _, binary = cv2.threshold(
        gray, 127, 255, cv2.THRESH_BINARY
    )

    # 4. Adaptive Thresholding
    adaptive = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    # 5. Otsu Thresholding
    _, otsu = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # 6. Simple foreground/background segmentation
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    _, foreground_mask = cv2.threshold(
        blurred,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # Keep original object and remove background
    foreground = cv2.bitwise_and(
        image,
        image,
        mask=foreground_mask
    )

    return {
        "Original": image,
        "Grayscale": gray,
        "Binary": binary,
        "Adaptive": adaptive,
        "Otsu": otsu,
        "Foreground": foreground
    }


# Process all images in input folder
if __name__ == "__main__":

    for filename in os.listdir(INPUT_FOLDER):

        if filename.lower().endswith(
            (".jpg", ".jpeg", ".png")
        ):

            image_path = os.path.join(
                INPUT_FOLDER, filename
            )

            results = segment_image(image_path)

            name = os.path.splitext(filename)[0]

            for method, output in results.items():

                output_path = os.path.join(
                    OUTPUT_FOLDER,
                    f"{name}_{method}.png"
                )

                cv2.imwrite(output_path, output)

            print(f"Processed: {filename}")

    print("All images processed successfully!")
