from tensorflow import keras
from tensorflow.keras import layers
model = keras.Sequential([
keras.Input(shape=(10,)),
layers.Dense(8, activation="relu"),
layers.Dense(1, activation="sigmoid")
])
model.summary()

