
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

# Get the folder where this Python file is located
project_folder = Path(__file__).parent

# Set image path
image_path = project_folder / "input_images" / "image1.jpg"

# Check if image exists
if not image_path.exists():
    print("Image not found!")
    print("Please put image1.jpg inside the input_images folder.")

else:
    # Perform object detection
    results = model.predict(source=str(image_path))

    # Display detection information
    for result in results:

        for box in result.boxes:

            # Get class ID
            class_id = int(box.cls[0])

            # Get object name
            object_name = model.names[class_id]

            # Get confidence score
            confidence = float(box.conf[0])

            # Get bounding box coordinates
            coordinates = box.xyxy[0].tolist()

            print("Object:", object_name)
            print("Class ID:", class_id)
            print("Confidence:", round(confidence * 100, 2), "%")
            print("Bounding Box:", coordinates)
            print("----------------------")

    print("Detection completed!")
