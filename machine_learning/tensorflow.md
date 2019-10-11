```python
import tensorflow as tf
import numpy as np

import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras import layers
from tensorflow.keras import Model

from tensorflow.keras.applications.inception_v3 import InceptionV3
```

# TensorFlow in Practice
## Week 1 - Intro
- https://github.com/lmoroney/dlaicourse/blob/master/Course%201%20-%20Part%202%20-%20Lesson%202%20-%20Notebook.ipynb
- http://playground.tensorflow.org/
### Linear regression
- `keras.layers.Dense(n)` is a layer with `n` neurons
```python
def house_model(y_new):
    # y = 0.5 + 0.5 * x
    xs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.float)
    ys = np.array([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5], dtype=np.float)
    model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer='sgd', loss='mean_squared_error')
    model.fit(xs, ys, epochs=500)
    return model.predict(y_new)[0]

prediction = house_model([7.0])
print(prediction)
```

## Week 2 - Deep Neural Network
### Fashion MNIST data
```python
mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

training_images  = training_images / 255.0
test_images = test_images / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation=tf.nn.relu),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

model.compile(optimizer = tf.train.AdamOptimizer(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=5)
model.evaluate(test_images, test_labels)
```
- always normalize input (make it between `0` and `1`)
- `keras.layers.Flatten()` flattens 2D inputs into 1D
- hidden layer takes `m` x `n` inputs to `128` outputs
- last layer takes `128` inputs to `10` outputs (categories) each with probabilities from `0` to `1`
- **relu**: return `max(0, x)`
- **softmax**: return 1 for the category with the largest probability, 0 for others
### Callbacks
- at each end of epochs, stop training if a threshold is reached (avoid overfitting)
- `logs.get('loss')` is the loss, `logs.get('acc')` is the accuracy
```python
class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if logs.get('loss') < 0.4:
            print("\nReached 60% accuracy so cancelling training!")
            self.model.stop_training = True
...
callbacks = myCallback()
model.fit(training_images, training_labels, epochs=5, callbacks=[callbacks])
```

## Week 3-4 - Convolution Neural Network, Real data with ImageDataGenerator
### Model definition
- for **binary** classification
    - use `sigmoid` on a single output neuron instead of `softmax`
    - use `binary_crossentropy` instead of `sparse_categorical_crossentropy`
    - can use the `adam` optimizer, or `RMSprop`
```python
model = tf.keras.models.Sequential(
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),  # fourth convolutions
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
)
model.summary()
model.compile(
    loss='binary_crossentropy',
    optimizer=RMSprop(lr=0.001),  # learning rate
    metrics=['acc']
)
```
- convolution works like a filter for images to emphasis certain features (clear, distinct) regardless of the position
- first layer takes inputs of `300` x `300`, each has `3` parameters (`rgb` in this case)
- create `64` filters, each `3` pixels by `3` pixels 
- for every `2` pixels by `2` pixels, pools (keeps) the one with the largest value (`size of image /= 4`)
- use `model.summary()` to inspect each layer, requires `input_shape()` specified on first layer
### ImageDataGenerator class
- use generators to get data from source for better customization
- use `fit_generator()` instead of `fit()`
```python
train_datagen = ImageDataGenerator(rescale=1.0/255)
validation_datagen = ImageDataGenerator(rescale=1.0/255)
```
- load from directory
    - auto labels input based on directory
```python
train_generator = train_datagen.flow_from_directory(
    '/train_parent/',  # parent directory of the subdirectory of images
                       # i.e. /train_parent/class_1/img_1, /train_parent/class_2/img_1
    target_size=(300, 300),  # image resolution, will resize when loaded
    batch_size=128,
    class_mode='binary',  # use binary for binary_crossentropy
)
validation_generator = validation_datagen.flow_from_directory(
    '/validation_parent/',
    target_size=(300, 300),
    batch_size=32,
    class_mode='binary',
)
```
- when loading from arrays instead of directory
```python
train_generator = train_datagen.flow(
    training_images,  # shape = (number of samples, dim_x, dim_y, 1)
    training_labels,
    batch_size=32,
)
validation_generator = validation_datagen.flow(
    testing_images,
    testing_labels,
    batch_size=32,
)
```
- train the model by using `fit_generator`
```python
history = model.fit_generator(
    train_generator,
    steps_per_epoch=8,  # steps_per_epoch * batch_size = number of samples
    epochs=15,
    verbose=1  # 0: silent, 1: animation bar, 2: less information, else: only shows epoch count
    validation_data=validation_generator,
    validation_steps=8
)
```


# Convolutional Neural Networks in TensorFlow
## Week 2 - Augmentation
- augmentation creates additional data by rotating/transforming the current dataset, thus increases the size and diversity of dataset
- avoids overfitting to improve performance
- introduces randomness, but doesn't work well if the test datasets doesn't have the same randomness
- use `ImageDataGenerator` to transform on the fly (won't save results)
```python
train_datagen = ImageDataGenerator(
    rescale=1./255,  # scale down
    rotation_range=40,  # rotate in a random direction up to 40 degrees, maximum 180
    width_shift_range=0.2,
    height_shift_range=0.2,  # move image up to 20% so that it's no longer centered
    shear_range=0.2,  # shear image up to 20%
    zoom_range=0.2,  # zoom image up to 20%
    horizontal_flip=True,  # randomly flips image horizontally
    fill_mode='nearest'  # fills pixels lost by operation
)
validation_datagen = ImageDataGenerator(rescale=1./255)
```

## Week 3 - Transfer Learning
- load pre-trained models, use some layers and retrain some layers
### The Inception model
### Load the model
```python
!wget --no-check-certificate \
    https://storage.googleapis.com/mledu-datasets/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5 \
    -O /tmp/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5
local_weights_file = '/tmp/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'

pre_trained_model = InceptionV3(input_shape=(150, 150, 3), include_top=False, weights=None)
pre_trained_model.load_weights(local_weights_file)

for layer in pre_trained_model.layers:
    layer.trainable = False
pre_trained_model.summary()
```
- use snapshot downloaded instead of built-in weights
- no top layer, use convolutions
- for each layer, lock states (freeze, not trainable)
### Add other layers to the model
```python
last_output = pre_trained_model.get_layer('mixed7').output
x = layers.Flatten()(last_output)
x = layers.Dense(1024, activation='relu')(x)
x = layers.Dropout(0.2)(x)
x = layers.Dense(1, activation='sigmoid')(x)

model = Model(pre_trained_model.input, x) 
model.compile(optimizer = RMSprop(lr=0.0001), 
              loss = 'binary_crossentropy', 
              metrics = ['acc'])
```
- use `mixed7` as the last layer of the pre-trained model
- add other layers, same idea as previously
- `Dropout` layer randomly eliminates 20% of the neurons
- `Dropout` reduces overfitting because neighbor neurons can have similar weights and skew the model

## Week 4 - Multiclass Classifications
- use `categorical` for `class_mode` in `ImageDataGenerator` instead of `binary`
- change output layer of the model to `3` if there are `3` classes, change `activation` to `softmax`
- use `categorical_crossentropy` or `sparse_categorical_crossentropy` when compiling the model instaed of `binary_crossentropy`
