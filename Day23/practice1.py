
from ultralytics import YOLO
from pathlib import Path

# Get the Day23 folder location
project_folder = Path(__file__).parent

# Set model path inside Day23
model_path = project_folder / "yolov8n.pt"

# Download and save YOLOv8 model inside Day23
if not model_path.exists():
    model = YOLO("yolov8n.pt")
    model.save(str(model_path))
    print("YOLOv8 model saved inside Day23!")
else:
    model = YOLO(str(model_path))
    print("YOLOv8 model loaded from Day23!")

# Input image path
image_path = project_folder / "input_images" / "image1.jpg"

# Perform object detection
results = model.predict(
    source=str(image_path),
    save=True,
    project=str(project_folder / "output_images"),
    name="single_image"
)

print("Object detection completed!")
print("Output image saved successfully!")
