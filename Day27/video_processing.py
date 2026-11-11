
import cv2
import os

# Get the folder where this Python file is located
base_folder = os.path.dirname(os.path.abspath(__file__))

# Set input video path
video_path = os.path.join(
    base_folder, "input_videos", "input.mp4"
)

# Open video
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Video not found!")
    print("Please check this location:")
    print(video_path)
    exit()

print("Video opened successfully!")


# Check if video opened
if not cap.isOpened():
    print("Error: Video not found!")
    exit()

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print("Video FPS:", fps)
print("Video Width:", width)
print("Video Height:", height)
print("Total Frames:", total_frames)

# Create video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")

# Create output folder path
output_folder = os.path.join(base_folder, "output_videos")

# Create folder if it does not exist
os.makedirs(output_folder, exist_ok=True)

# Set output video path
output_path = os.path.join(output_folder, "processed.mp4")

# Create video writer
out = cv2.VideoWriter(
    output_path,
    fourcc,
    fps if fps > 0 else 20,
    (width, height),
    False
)

# Check video writer
if not out.isOpened():
    print("Error: Cannot create output video!")
    cap.release()
    exit()

print("Output video location:", output_path)

# Read video frame by frame
while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Canny Edge Detection
    edges = cv2.Canny(blur, 100, 200)

    # Display original video
    cv2.imshow("Original Video", frame)

    # Display processed video
    cv2.imshow("Processed Video", edges)

    # Save processed frame
    out.write(edges)

    # Press q to stop
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print("Processed video saved successfully!")
