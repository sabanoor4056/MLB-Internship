# Loading and Preprocessing Cats vs Dogs Dataset
import tensorflow as tf
import tensorflow_datasets as tfds
import matplotlib.pyplot as plt

# Step 1: Load the Cats vs Dogs dataset

print("Loading Cats vs Dogs dataset...")
dataset, info = tfds.load(
    "cats_vs_dogs",
    with_info=True,
    as_supervised=True
)

print("\nDataset loaded successfully!")


# Step 2: Display dataset information

print("\nDataset Information:")
print("Total Images:",
      info.splits["train"].num_examples)

print("Classes:",
      info.features["label"].names)


# Step 3: Get the training dataset

full_dataset = dataset["train"]

# Shuffle the dataset
full_dataset = full_dataset.shuffle(
    buffer_size=1000,
    seed=42
)


# Step 4: Split dataset into training and validation

total_images = info.splits["train"].num_examples
train_size = int(total_images * 0.80)

# 80% training images
train_dataset = full_dataset.take(train_size)

# 20% validation images
validation_dataset = full_dataset.skip(train_size)
print("\nDataset Split Completed!")
print("Training Images:", train_size)
print("Validation Images:", total_images - train_size)


# Step 5: Resize and preprocess images

def preprocess_image(image, label):

    # Resize image
    image = tf.image.resize(
        image,
        (224, 224)
    )

    # Convert image into float32
    image = tf.cast(image, tf.float32)
    return image, label


# Apply preprocessing to training data
train_dataset = train_dataset.map(
    preprocess_image,
    num_parallel_calls=tf.data.AUTOTUNE
)

# Apply preprocessing to validation data
validation_dataset = validation_dataset.map(
    preprocess_image,
    num_parallel_calls=tf.data.AUTOTUNE
)
print("\nImage preprocessing completed!")


# Step 6: Create batches

BATCH_SIZE = 32
train_dataset = train_dataset.batch(BATCH_SIZE)
validation_dataset = validation_dataset.batch(BATCH_SIZE)
print("\nBatch preparation completed!")


# Step 7: Prefetch data for better performance

train_dataset = train_dataset.prefetch(
    tf.data.AUTOTUNE
)
validation_dataset = validation_dataset.prefetch(
    tf.data.AUTOTUNE
)


# Step 8: Display sample images

class_names = info.features["label"].names
print("\nDisplaying sample images...")
for images, labels in train_dataset.take(1):
    plt.figure(figsize=(10, 8))
    for i in range(9):
        plt.subplot(3, 3, i + 1)

        # Display image
        plt.imshow(
            images[i].numpy().astype("uint8")
        )

        # Get image label
        label = class_names[int(labels[i].numpy())]
        plt.title(label)
        plt.axis("off")
    plt.tight_layout()
    plt.show()


# Step 9: Display final dataset shapes

for images, labels in train_dataset.take(1):
    print("\nTraining Batch Shape:", images.shape)
    print("Training Labels Shape:", labels.shape)

print("\nPractice 2 Completed Successfully!")
