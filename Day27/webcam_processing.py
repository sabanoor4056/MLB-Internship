
import cv2
import os

# Get the location of this Python file
base_folder = os.path.dirname(os.path.abspath(__file__))

# Use existing output_videos folder inside Day27
output_folder = os.path.join(base_folder, "output_videos")

# Create folder only if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Video saving path
video_path = os.path.join(
    output_folder, "webcam_output.mp4"
)

# Open webcam using DirectShow
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Check webcam
if not cap.isOpened():
    print("Webcam not found!")
    exit()

print("Webcam opened successfully!")

# Read first frame
ret, frame = cap.read()

if not ret:
    print("Cannot capture webcam frame!")
    cap.release()
    exit()

# Get webcam dimensions
height, width = frame.shape[:2]

fps = 20

print("Width:", width)
print("Height:", height)

# Create output video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

out = cv2.VideoWriter(
    video_path,
    fourcc,
    fps,
    (width, height),
    False
)

# Check video writer
if not out.isOpened():
    print("Cannot create output video!")
    cap.release()
    exit()

print("Recording started!")
print("Press Q to stop recording")

while True:

    # Read webcam frame
    ret, frame = cap.read()

    if not ret:
        print("Cannot read webcam frame!")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(
        frame, cv2.COLOR_BGR2GRAY
    )

    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(
        gray, (5, 5), 0
    )

    # Apply Canny Edge Detection
    edges = cv2.Canny(
        blur, 100, 200
    )

    # Display original video
    cv2.imshow("Live Webcam", frame)

    # Display processed video
    cv2.imshow("Edge Detection", edges)

    # Save processed frame
    out.write(edges)

    # Press Q to stop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

# Check saved video
if os.path.exists(video_path):

    file_size = os.path.getsize(video_path)

    print("\nWebcam video saved successfully!")
    print("Saved location:", video_path)
    print("File size:", file_size, "bytes")

else:
    print("Video was not saved!")
