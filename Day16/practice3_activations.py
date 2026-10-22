from tensorflow import keras
from tensorflow.keras import layers
functions = ["relu", "sigmoid", "tanh"]
for function in functions:
    print("\nActivation Function:", function)
    model = keras.Sequential([
        keras.Input(shape=(10,)),
        layers.Dense(8, activation=function),
        layers.Dense(1, activation="sigmoid")
    ])
    model.summary()
