# Transfer Learning using MobileNetV2
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
# Step 1: Load the pre-trained MobileNetV2 model
base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(224, 224, 3)
)
print("MobileNetV2 model loaded successfully!")
# Step 2: Explore model architecture

print("\nModel Summary:")
base_model.summary()

# Step 3: Freeze the base model layers

base_model.trainable = False
print("\nBase model layers are frozen!")

# Step 4: Add our own classification head

x = base_model.output

# Convert feature maps into a single vector
x = GlobalAveragePooling2D()(x)

# Add a classification layer
x = Dense(128, activation="relu")(x)

# Output layer for two classes
output = Dense(2, activation="softmax")(x)

# Step 5: Create the final model

model = Model(
    inputs=base_model.input,
    outputs=output
)

# Step 6: Compile the model

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# Step 7: Display final model

print("\nFinal Model Summary:")
model.summary()
print("\nTrainable layers:", sum(
    layer.trainable for layer in model.layers
))
print("\nPractice 1 completed successfully!")
