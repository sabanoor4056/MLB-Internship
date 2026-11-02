# Cats vs Dogs Image Classifier
# Using Transfer Learning and MobileNetV2
import os
import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.layers import (
    Input,
    Dense,
    GlobalAveragePooling2D
)
from tensorflow.keras.models import Model
# Get the location of current Python file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create outputs folder inside Day-22
OUTPUT_FOLDER = os.path.join(BASE_DIR, "outputs")

os.makedirs(OUTPUT_FOLDER, exist_ok=True)

print("Output folder location:", OUTPUT_FOLDER)

# 1. Basic Settings

IMAGE_SIZE = 224
BATCH_SIZE = 32
EPOCHS = 5
os.makedirs("outputs", exist_ok=True)
print("Cats vs Dogs Project Started!")

# 2. Load Dataset

print("Loading dataset...")
dataset, info = tfds.load(
    "cats_vs_dogs",
    with_info=True,
    as_supervised=True
)
dataset = dataset["train"]
class_names = info.features["label"].names
print("Dataset loaded successfully!")
print("Total images:", info.splits["train"].num_examples)
print("Classes:", class_names)


# 3. Split Dataset


total_images = info.splits["train"].num_examples
dataset = dataset.shuffle(
    total_images,
    seed=42,
    reshuffle_each_iteration=False
)

train_size = int(total_images * 0.80)
train_dataset = dataset.take(train_size)
validation_dataset = dataset.skip(train_size)
print("Training images:", train_size)
print("Validation images:", total_images - train_size)


# 4. Preprocess Images


def preprocess_image(image, label):

    image = tf.image.resize(
        image,
        (IMAGE_SIZE, IMAGE_SIZE)
    )
    image = tf.cast(image, tf.float32)
    return image, label

train_dataset = train_dataset.map(
    preprocess_image,
    num_parallel_calls=tf.data.AUTOTUNE
)

validation_dataset = validation_dataset.map(
    preprocess_image,
    num_parallel_calls=tf.data.AUTOTUNE
)



# 5. Batch and Prefetch


train_dataset = train_dataset.batch(BATCH_SIZE)
validation_dataset = validation_dataset.batch(BATCH_SIZE)
train_dataset = train_dataset.prefetch(
    tf.data.AUTOTUNE
)
validation_dataset = validation_dataset.prefetch(
    tf.data.AUTOTUNE
)
print("Image preprocessing completed!")


# 6. Load MobileNetV2


print("Loading MobileNetV2...")
base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(224, 224, 3)
)

# Freeze base model
base_model.trainable = False
print("MobileNetV2 loaded successfully!")

# 7. Build Classification Model


inputs = Input(shape=(224, 224, 3))

# Preprocess images for MobileNetV2
x = preprocess_input(inputs)

# Extract image features
x = base_model(x, training=False)

# Add classification layer
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation="relu")(x)

# Output layer for Cats and Dogs
outputs = Dense(1, activation="sigmoid")(x)
model = Model(inputs, outputs)

# 8. Compile Model

model.compile(
    optimizer=tf.keras.optimizers.Adam(
        learning_rate=0.001
    ),
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
print("Model compiled successfully!")
model.summary()


# 9. Train Model

print("Training started...")
history = model.fit(
    train_dataset,
    validation_data=validation_dataset,
    epochs=EPOCHS
)
print("Training completed!")

# 10. Evaluate Model

loss, accuracy = model.evaluate(validation_dataset)
print("Validation Loss:", round(loss, 4))
print(
    "Validation Accuracy:",
    round(accuracy * 100, 2),
    "%"
)


# 11. Plot Accuracy and Loss

plt.figure(figsize=(12, 5))

# Accuracy graph
plt.subplot(1, 2, 1)
plt.plot(history.history["accuracy"], label="Training Accuracy")
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")
plt.title("Model Accuracy")
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.legend()

# Loss graph
plt.subplot(1, 2, 2)
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.title("Model Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_FOLDER, "accuracy_loss.png"))
plt.show()

# 12. Sample Predictions

print("Showing sample predictions...")
for images, labels in validation_dataset.take(1):
    predictions = model.predict(images, verbose=0)
    plt.figure(figsize=(12, 10))
    for i in range(9):
        plt.subplot(3, 3, i + 1)
        plt.imshow(
            images[i].numpy().astype("uint8")
        )
        actual = class_names[int(labels[i].numpy())]
        if predictions[i][0] >= 0.5:
            predicted = class_names[1]
        else:
            predicted = class_names[0]
        plt.title(
            f"Actual: {actual}\nPredicted: {predicted}"
        )
        plt.axis("off")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_FOLDER, "sample_predictions.png"))
    plt.show()

# 13. Save Model
model.save(os.path.join(OUTPUT_FOLDER, "cats_vs_dogs_model.keras"))
print("Model saved successfully!")
print("All tasks completed!")
