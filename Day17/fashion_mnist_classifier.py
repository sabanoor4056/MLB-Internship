import os
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
# Create output folder beside this script
folder = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(folder, "outputs")
os.makedirs(output_folder, exist_ok=True)
# Fashion MNIST class names
class_names = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]
# Step 1: Load dataset
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
print("Training images:", x_train.shape)
print("Testing images:", x_test.shape)
# Step 2: Display 10 sample images
plt.figure(figsize=(12, 5))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_train[i], cmap="gray")
    plt.title(class_names[y_train[i]])
    plt.axis("off")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "sample_images.png"))
plt.show()
# Step 3: Normalize images
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
# Add channel dimension
x_train = x_train.reshape(-1, 28, 28, 1)
x_test = x_test.reshape(-1, 28, 28, 1)
# Step 4: Build CNN model
model = Sequential([
    tf.keras.Input(shape=(28, 28, 1)),
    Conv2D(32, (3, 3), activation="relu"),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation="relu"),
    Dense(10, activation="softmax")
])
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)
model.summary()
# Step 5: Train model
history = model.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.2
)
# Save the trained model
model.save(os.path.join(output_folder, "fashion_cnn.keras"))
# Step 6: Evaluate model
train_loss, train_accuracy = model.evaluate(
    x_train, y_train, verbose=0
)
test_loss, test_accuracy = model.evaluate(
    x_test, y_test, verbose=0
)
print("\nTraining Accuracy:", round(train_accuracy * 100, 2), "%")
print("Training Loss:", round(train_loss, 4))
print("Testing Accuracy:", round(test_accuracy * 100, 2), "%")
print("Testing Loss:", round(test_loss, 4))
# Step 7: Plot accuracy
plt.figure()
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("Training and Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.savefig(os.path.join(output_folder, "accuracy_graph.png"))
plt.show()
# Step 8: Plot loss
plt.figure()
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("Training and Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.savefig(os.path.join(output_folder, "loss_graph.png"))
plt.show()
# Step 9: Predict test images
probabilities = model.predict(x_test, verbose=0)
predictions = np.argmax(probabilities, axis=1)
# Step 10: Display confusion matrix
matrix = confusion_matrix(y_test, predictions)

display = ConfusionMatrixDisplay(
    confusion_matrix=matrix,
    display_labels=class_names
)
fig, ax = plt.subplots(figsize=(12, 12))
display.plot(ax=ax, xticks_rotation=45, cmap="Blues")
plt.title("Fashion MNIST Confusion Matrix")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "confusion_matrix.png"))
plt.show()
# Step 11: Find correct and incorrect predictions
correct = np.where(predictions == y_test)[0]
incorrect = np.where(predictions != y_test)[0]
# Display 10 correctly classified images
plt.figure(figsize=(12, 5))
for i in range(min(10, len(correct))):
    index = correct[i]
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_test[index].squeeze(), cmap="gray")
    plt.title("Predicted: " + class_names[predictions[index]])
    plt.axis("off")
plt.suptitle("10 Correct Predictions")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "correct_predictions.png"))
plt.show()
# Display 10 incorrectly classified images
plt.figure(figsize=(12, 6))
for i in range(min(10, len(incorrect))):
    index = incorrect[i]
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_test[index].squeeze(), cmap="gray")
    plt.title(
        "Pred: " + class_names[predictions[index]]
        + "\nActual: " + class_names[y_test[index]],
        fontsize=8
    )
    plt.axis("off")
plt.suptitle("10 Incorrect Predictions")
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "incorrect_predictions.png"))
plt.show()
print("\nProject completed successfully!")
print("All graphs and prediction images are saved in outputs.")
