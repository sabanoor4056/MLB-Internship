
from ultralytics import YOLO
from pathlib import Path

# Get Day-23 folder location
base_folder = Path(__file__).parent

# Set YOLO model path inside Day-23
model_path = base_folder / "yolov8n.pt"

# Download model if it does not exist
if not model_path.exists():

    print("Downloading YOLOv8 model...")

    model = YOLO("yolov8n.pt")

    # Save model inside Day-23
    model.save(str(model_path))

    print("Model saved inside Day-23!")

else:

    print("Loading YOLOv8 model from Day-23...")

    model = YOLO(str(model_path))

print("YOLOv8 model loaded successfully!")

# Input images folder
image_folder = base_folder / "input_images"

# Check input folder
if not image_folder.exists():
    print("Input images folder not found!")
    exit()

# Get all images
image_files = list(image_folder.glob("*"))

# Filter image files
image_files = [
    file for file in image_files
    if file.suffix.lower() in [".jpg", ".jpeg", ".png"]
]

if len(image_files) == 0:
    print("No images found! Please add images.")
    exit()

print("Total images found:", len(image_files))

# Perform object detection
results = model.predict(
    source=[str(file) for file in image_files],
    save=True,
    project=str(base_folder / "output_images"),
    name="multiple_images"
)

print("Object detection completed!")
print("Check the output_images folder.")
