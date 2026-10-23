import os
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import fashion_mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
# Use the outputs folder inside Day17
folder = os.path.dirname(os.path.abspath(__file__))
output_folder = os.path.join(folder, "outputs")
# Create folder only if it does not exist
os.makedirs(output_folder, exist_ok=True)
# Load dataset
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
# Normalize images
x_train = x_train.astype("float32") / 255.0
x_test = x_test.astype("float32") / 255.0
# Prepare images for CNN
x_train = x_train.reshape(-1, 28, 28, 1)
# Build CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation="relu",
           input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation="relu"),
    Dense(10, activation="softmax")
])
# Compile model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)
# Train model
history = model.fit(
    x_train,
    y_train,
    epochs=5,
    batch_size=64,
    validation_split=0.2
)
# Save model inside Day17/outputs
model.save(os.path.join(output_folder, "fashion_cnn.keras"))
# Save accuracy graph
plt.figure()
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.title("Training Accuracy")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "training_accuracy.png"))
plt.close()
# Save loss graph
plt.figure()
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("Training Loss")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_folder, "training_loss.png"))
plt.close()
print("Training completed!")
print("Model and graphs saved in:", output_folder)
