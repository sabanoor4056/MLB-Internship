import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense
import os
# Get the folder where this Python file is saved
folder = os.path.dirname(os.path.abspath(__file__))
# 1. Load the dataset
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
# Clothing labels
labels = [
    "T-shirt", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]
# 2. Explore the dataset
print("Training images:", x_train.shape)
print("Testing images:", x_test.shape)
print("First image label:", labels[y_train[0]])
# Display one sample image
plt.imshow(x_train[0], cmap="gray")
plt.title(labels[y_train[0]])
plt.axis("off")
plt.savefig(os.path.join(folder, "sample_image.png"))
plt.show(block=False)
plt.pause(2)
plt.close()
# 3. Normalize pixel values
x_train = x_train / 255.0
x_test = x_test / 255.0
# 4. Build the ANN model
model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation="relu"),
    Dense(10, activation="softmax")
])
# 5. Compile the model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)
# Display model structure
model.summary()
# 6. Train the model
history = model.fit(
    x_train,
    y_train,
    epochs=5,
    validation_split=0.2
)
# 7. Evaluate the model
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print("Final training accuracy:",
      history.history["accuracy"][-1] * 100, "%")
print("Testing accuracy:", test_accuracy * 100, "%")
# 8. Plot training and validation accuracy
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("Training and Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.savefig(os.path.join(folder, "accuracy.png"))
plt.show()
# 9. Predict five test images
predictions = model.predict(x_test[:5])
predicted_labels = np.argmax(predictions, axis=1)
plt.figure(figsize=(12, 4))
for i in range(5):
    plt.subplot(1, 5, i + 1)
    plt.imshow(x_test[i], cmap="gray")
    plt.title(
        "Predicted: " + labels[predicted_labels[i]] +
        "\nActual: " + labels[y_test[i]],
        fontsize=8
    )
    plt.axis("off")
    print("Predicted:", labels[predicted_labels[i]])
    print("Actual:", labels[y_test[i]])
plt.tight_layout()
plt.savefig(os.path.join(folder, "predictions.png"))
plt.show()
