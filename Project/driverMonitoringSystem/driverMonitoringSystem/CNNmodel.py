import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense, Activation

# creates and returns neural network model
def create_model(inputWidth, inputHeight, ch, outputNo):
    
    tf.keras.backend.set_floatx('float64')

    model = Sequential()

    model.add(Conv2D(16, (3, 3), activation='relu', input_shape=(inputWidth, inputHeight, ch)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.25))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.25))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(outputNo)) 
    model.add(Activation('sigmoid'))

    model.compile(optimizer="adam",loss='mean_squared_error', metrics=["accuracy"])

    model.summary()

    return model