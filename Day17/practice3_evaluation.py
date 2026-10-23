import os
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import load_model
# Find the folder where this Python file is saved
folder = os.path.dirname(os.path.abspath(__file__))
# Find the outputs folder inside Day17
output_folder = os.path.join(folder, "outputs")
# Find the saved CNN model
model_path = os.path.join(output_folder, "fashion_cnn.keras")
# Check if the model exists
if not os.path.exists(model_path):
    print("Model not found!")
    print("Please run practice2_cnn.py first.")
    print("Expected location:", model_path)
    raise SystemExit
# Load the Fashion MNIST dataset
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
# Normalize images
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
# Prepare images for CNN
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)
# Load the trained model
model = load_model(model_path)
print("Model loaded successfully!")
# Evaluate training data
train_loss, train_accuracy = model.evaluate(
    x_train, y_train, verbose=0
)
# Evaluate testing data
test_loss, test_accuracy = model.evaluate(
    x_test, y_test, verbose=0
)
print("\nTraining Accuracy:", round(train_accuracy * 100, 2), "%")
print("Training Loss:", round(train_loss, 4))
print("Testing Accuracy:", round(test_accuracy * 100, 2), "%")
print("Testing Loss:", round(test_loss, 4))
# Clothing class names
class_names = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]
# Predict the first 10 test images
predictions = model.predict(x_test[:10], verbose=0)
predicted_labels = np.argmax(predictions, axis=1)
# Display and save predictions
plt.figure(figsize=(12, 6))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_test[i].squeeze(), cmap="gray")
    predicted = class_names[predicted_labels[i]]
    actual = class_names[y_test[i]]
    plt.title(
        f"Predicted: {predicted}\nActual: {actual}",
        fontsize=8
    )
    plt.axis("off")
plt.tight_layout()
# Save image inside Day17/outputs
image_path = os.path.join(output_folder, "practice3_predictions.png")
plt.savefig(image_path, dpi=150, bbox_inches="tight")
plt.show()
plt.close()
print("\nPredictions completed!")
print("Prediction image saved at:", image_path)
