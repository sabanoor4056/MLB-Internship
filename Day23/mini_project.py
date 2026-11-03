
from pathlib import Path
from ultralytics import YOLO

# Get Day-23 folder location
base_folder = Path(__file__).parent

# Load the already saved YOLO model
model_path = base_folder / "yolov8n.pt"

if model_path.exists():
    print("Loading saved YOLO model...")
    model = YOLO(str(model_path))
else:
    print("Downloading YOLOv8 model...")
    model = YOLO("yolov8n.pt")
    model.save(str(model_path))
    print("Model saved successfully!")

print("YOLO model loaded successfully!")

# Dataset folder
dataset_path = base_folder / "dataset" / "Vehicle-Detection"
print("Day23 folder:", base_folder)
print("Dataset path:", dataset_path)
print("Dataset exists:", dataset_path.exists())

if dataset_path.exists():
    print("Dataset contents:")
    for item in dataset_path.iterdir():
        print(item.name)
# Find test images
image_folder = dataset_path / "test" / "images"

# If test folder is not available, use validation folder
if not image_folder.exists():
    image_folder = dataset_path / "valid" / "images"

# Check image folder
if not image_folder.exists():
    print("Dataset images folder not found!")
    exit()

# Get image files
image_files = list(image_folder.glob("*"))

# Select only image files
image_files = [
    file for file in image_files
    if file.suffix.lower() in [".jpg", ".jpeg", ".png"]
]

# Select first 20 images
image_files = image_files[:20]

if len(image_files) == 0:
    print("No images found!")
    exit()

print("Total images:", len(image_files))

# Perform object detection
results = model.predict(
    source=[str(file) for file in image_files],
    conf=0.25,
    save=True,
    project=str(base_folder / "output_images"),
    name="vehicle_detection",
    exist_ok=True
)

# Display detection results
for result in results:

    print("\nImage:", Path(result.path).name)

    for box in result.boxes:

        class_id = int(box.cls[0])

        object_name = model.names[class_id]

        confidence = float(box.conf[0])

        print("Object:", object_name)
        print("Confidence:", round(confidence * 100, 2), "%")

print("\nObject detection completed!")
print("Check the output_images folder.")
