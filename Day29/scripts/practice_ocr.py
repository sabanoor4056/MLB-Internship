
import easyocr
import os

# Get the Day29 project folder automatically
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

# Create folder paths
input_folder = os.path.join(BASE_DIR, "input_images")
output_folder = os.path.join(BASE_DIR, "output_text")

# Check if input folder exists
if not os.path.exists(input_folder):
    print("Input folder not found!")
    print("Expected location:", input_folder)
    exit()

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Initialize EasyOCR
reader = easyocr.Reader(['en'], gpu=False)

# Get image files
images = os.listdir(input_folder)

if not images:
    print("No images found in input_images folder!")
    exit()

# Process images
for filename in images:

    if filename.lower().endswith(
        ('.jpg', '.jpeg', '.png')
    ):

        image_path = os.path.join(
            input_folder, filename
        )

        print("\nProcessing:", filename)

        results = reader.readtext(image_path)

        extracted_text = []

        for result in results:
            extracted_text.append(result[1])

        text = "\n".join(extracted_text)

        print("\nExtracted Text:")
        print(text)

        # Save extracted text
        output_name = os.path.splitext(filename)[0] + ".txt"

        output_path = os.path.join(
            output_folder, output_name
        )

        with open(output_path, "w", encoding="utf-8") as file:
            file.write(text)

        print("Saved:", output_path)

print("\nAll images processed successfully!")
