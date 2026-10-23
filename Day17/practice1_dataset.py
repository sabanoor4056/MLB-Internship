import matplotlib.pyplot as plt
from tensorflow.keras.datasets import fashion_mnist
# Load the Fashion MNIST dataset
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
# Fashion MNIST class names
class_names = [
    "T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
    "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"
]
print("Training images:", x_train.shape)
print("Testing images:", x_test.shape)
# Display 10 sample images
plt.figure(figsize=(12, 5))
for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_train[i], cmap="gray")
    plt.title(class_names[y_train[i]])
    plt.axis("off")
plt.tight_layout()
plt.show()
# Normalize images
x_train = x_train / 255.0
x_test = x_test / 255.0
print("Normalization completed!")
print("Pixel value after normalization:", x_train[0][0][0])
