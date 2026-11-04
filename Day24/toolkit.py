
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt



# 1. CREATE OUTPUT FOLDER

# Get the location of this Python file
BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Create output folder beside this Python file
OUTPUT_FOLDER = os.path.join(BASE_FOLDER, "output")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("Output folder:", OUTPUT_FOLDER)



# 2. LOAD IMAGE


image_path = input("Enter image path: ")

# If relative path is entered, use Python file location
if not os.path.isabs(image_path):
    image_path = os.path.join(BASE_FOLDER, image_path)

image = cv2.imread(image_path)

if image is None:
    print("Image not found! Please check the image path.")
    exit()

# Keep original image unchanged
original = image.copy()

# Working image
processed = image.copy()

print("Image loaded successfully!")



# 3. GRAYSCALE


def grayscale():
    global processed

    if len(processed.shape) == 3:

        processed = cv2.cvtColor(
            processed,
            cv2.COLOR_BGR2GRAY
        )

        print("Image converted to grayscale!")

    else:
        print("Image is already grayscale!")


# 4. RESIZE IMAGE


def resize():
    global processed

    try:
        width = int(input("Enter new width: "))
        height = int(input("Enter new height: "))

        if width <= 0 or height <= 0:
            print("Width and height must be greater than zero!")
            return

        processed = cv2.resize(
            processed,
            (width, height)
        )

        print("Image resized successfully!")

    except ValueError:
        print("Please enter valid numbers!")


# 5. ROTATE IMAGE


def rotate():
    global processed

    print("1. Rotate 90 degrees")
    print("2. Rotate 180 degrees")
    print("3. Rotate 270 degrees")

    choice = input("Enter choice: ")

    if choice == "1":

        processed = cv2.rotate(
            processed,
            cv2.ROTATE_90_CLOCKWISE
        )

    elif choice == "2":

        processed = cv2.rotate(
            processed,
            cv2.ROTATE_180
        )

    elif choice == "3":

        processed = cv2.rotate(
            processed,
            cv2.ROTATE_90_COUNTERCLOCKWISE
        )

    else:
        print("Invalid choice!")
        return

    print("Image rotated successfully!")



# 6. FLIP IMAGE


def flip():
    global processed

    print("1. Horizontal Flip")
    print("2. Vertical Flip")

    choice = input("Enter choice: ")

    if choice == "1":

        processed = cv2.flip(processed, 1)

    elif choice == "2":

        processed = cv2.flip(processed, 0)

    else:
        print("Invalid choice!")
        return

    print("Image flipped successfully!")


# 7. CROP IMAGE


def crop():
    global processed

    height, width = processed.shape[:2]

    try:
        print("Enter crop coordinates.")

        x1 = int(input("Starting X: "))
        y1 = int(input("Starting Y: "))
        x2 = int(input("Ending X: "))
        y2 = int(input("Ending Y: "))

        if (
            x1 < 0 or y1 < 0 or
            x2 > width or y2 > height or
            x1 >= x2 or y1 >= y2
        ):
            print("Invalid crop coordinates!")
            return

        processed = processed[y1:y2, x1:x2]

        print("Image cropped successfully!")

    except ValueError:
        print("Please enter valid numbers!")


# 8. DRAW SHAPES


def draw_shapes():
    global processed

    height, width = processed.shape[:2]

    # Convert grayscale to color if needed
    if len(processed.shape) == 2:

        processed = cv2.cvtColor(
            processed,
            cv2.COLOR_GRAY2BGR
        )

    # Draw Rectangle
    cv2.rectangle(
        processed,
        (10, 10),
        (width // 2, height // 2),
        (0, 255, 0),
        3
    )

    # Draw Circle
    cv2.circle(
        processed,
        (width // 2, height // 2),
        min(50, width // 4, height // 4),
        (255, 0, 0),
        3
    )

    # Draw Line
    cv2.line(
        processed,
        (0, 0),
        (width - 1, height - 1),
        (0, 0, 255),
        3
    )

    # Draw Polygon
    points = np.array([
        [width // 2, 10],
        [width - 10, height // 2],
        [width // 2, height - 10],
        [10, height // 2]
    ], np.int32)

    cv2.polylines(
        processed,
        [points],
        True,
        (0, 255, 255),
        3
    )

    print("All shapes added successfully!")


# 9. ADD CUSTOM TEXT


def add_text():
    global processed

    # Convert grayscale to color if needed
    if len(processed.shape) == 2:

        processed = cv2.cvtColor(
            processed,
            cv2.COLOR_GRAY2BGR
        )

    text = input("Enter your text: ")

    cv2.putText(
        processed,
        text,
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    print("Text added successfully!")


# 10. BRIGHTNESS AND CONTRAST


def brightness_contrast():
    global processed

    try:
        brightness = int(
            input("Enter brightness (-100 to 100): ")
        )

        contrast = float(
            input("Enter contrast (example: 1.5): ")
        )

        if not -100 <= brightness <= 100 or contrast < 0:
            print("Invalid brightness or contrast!")
            return

        processed = cv2.convertScaleAbs(
            processed,
            alpha=contrast,
            beta=brightness
        )

        # Save adjusted image
        save_path = os.path.join(
            OUTPUT_FOLDER,
            "brightness_contrast.jpg"
        )

        cv2.imwrite(save_path, processed)

        print("Brightness and contrast adjusted!")
        print("Image saved at:", save_path)

    except ValueError:
        print("Please enter valid numbers!")


# 11. RGB AND BGR COMPARISON


def compare_rgb_bgr():

    # Convert original BGR image to RGB
    rgb = cv2.cvtColor(
        original,
        cv2.COLOR_BGR2RGB
    )

    plt.figure(figsize=(10, 5))

    # Display BGR directly (incorrect colors in Matplotlib)
    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("BGR Image")
    plt.axis("off")

    # Display correctly converted RGB image
    plt.subplot(1, 2, 2)
    plt.imshow(rgb)
    plt.title("RGB Image")
    plt.axis("off")

    plt.tight_layout()

    # Save comparison in correct output folder
    save_path = os.path.join(
        OUTPUT_FOLDER,
        "rgb_bgr_comparison.jpg"
    )

    plt.savefig(
        save_path,
        bbox_inches="tight"
    )

    plt.show()
    plt.close()

    print("RGB and BGR comparison saved!")
    print("Saved at:", save_path)


# 12. SHOW ORIGINAL AND PROCESSED

def show_images():

    # Make copies for display
    original_display = original.copy()
    processed_display = processed.copy()

    # Convert grayscale to BGR for display
    if len(original_display.shape) == 2:

        original_display = cv2.cvtColor(
            original_display,
            cv2.COLOR_GRAY2BGR
        )

    if len(processed_display.shape) == 2:

        processed_display = cv2.cvtColor(
            processed_display,
            cv2.COLOR_GRAY2BGR
        )

    # Resize both images to same height
    height = 400

    original_width = int(
        original_display.shape[1] *
        height / original_display.shape[0]
    )

    processed_width = int(
        processed_display.shape[1] *
        height / processed_display.shape[0]
    )

    original_display = cv2.resize(
        original_display,
        (original_width, height)
    )

    processed_display = cv2.resize(
        processed_display,
        (processed_width, height)
    )

    # Join images side by side
    combined = cv2.hconcat([
        original_display,
        processed_display
    ])

    # Save comparison
    save_path = os.path.join(
        OUTPUT_FOLDER,
        "original_processed_comparison.jpg"
    )

    cv2.imwrite(save_path, combined)

    print("Comparison image saved!")
    print("Saved at:", save_path)

    # Display images
    cv2.imshow(
        "Original and Processed Images",
        combined
    )

    cv2.waitKey(0)
    cv2.destroyAllWindows()


# 13. SAVE PROCESSED IMAGE


def save_image():

    filename = input(
        "Enter output filename (example: result.jpg): "
    )

    if not filename.lower().endswith(
        (".jpg", ".jpeg", ".png")
    ):
        print("Please use .jpg, .jpeg or .png!")
        return

    save_path = os.path.join(
        OUTPUT_FOLDER,
        filename
    )

    success = cv2.imwrite(
        save_path,
        processed
    )

    if success:

        print("Image saved successfully!")
        print("Saved at:", save_path)

    else:
        print("Image could not be saved!")

# 14. MAIN MENU


while True:

    print("\n========== IMAGE PROCESSING TOOLKIT ==========")

    print("1. Convert to Grayscale")
    print("2. Resize Image")
    print("3. Rotate Image")
    print("4. Flip Image")
    print("5. Crop Image")
    print("6. Draw Shapes")
    print("7. Add Custom Text")
    print("8. Adjust Brightness and Contrast")
    print("9. Compare RGB and BGR")
    print("10. Show Original and Processed Images")
    print("11. Save Processed Image")
    print("12. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        grayscale()

    elif choice == "2":
        resize()

    elif choice == "3":
        rotate()

    elif choice == "4":
        flip()

    elif choice == "5":
        crop()

    elif choice == "6":
        draw_shapes()

    elif choice == "7":
        add_text()

    elif choice == "8":
        brightness_contrast()

    elif choice == "9":
        compare_rgb_bgr()

    elif choice == "10":
        show_images()

    elif choice == "11":
        save_image()

    elif choice == "12":

        print("Thank you for using Image Processing Toolkit!")
        break

    else:
        print("Invalid choice! Please try again.")
