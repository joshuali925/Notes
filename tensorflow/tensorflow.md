# imports
```python
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
```

# Week 1 - Intro
- https://github.com/lmoroney/dlaicourse/blob/master/Course%201%20-%20Part%202%20-%20Lesson%202%20-%20Notebook.ipynb
- http://playground.tensorflow.org/
## Linear regression
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

# Week 2 - Deep Neural Network
## Fashion MNIST data
```python
mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

training_images  = training_images / 255.0
test_images = test_images / 255.0

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(), tf.keras.layers.Dense(128, activation=tf.nn.relu), tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

model.compile(optimizer = tf.train.AdamOptimizer(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(training_images, training_labels, epochs=5)
model.evaluate(test_images, test_labels)
```
- always normalize input (make it between 0 and 1)
- `keras.layers.Flatten()` flattens 2D inputs into 1D
- hidden layer takes `m * n` inputs to `128` outputs
- last layer takes `128` inputs to `10` outputs (categories) each with probabilities from `0` to `1`
- **relu**: return `max(0, x)`
- **softmax**: return 1 for the category with the largest probability, 0 for others

## Callbacks
- at each end of epochs, stop training if a threshold is reached (avoid overfitting)
- `logs.get('loss')` is the loss, `logs.get('acc')` is the accuracy
```python
class myCallback(tf.keras.callbacks.Callback):
    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('loss')<0.4):
            print("\nReached 60% accuracy so cancelling training!")
            self.model.stop_training = True
...
callbacks = myCallback()
model.fit(training_images, training_labels, epochs=5, callbacks=[callbacks])
```

# Week 3 - Convolution Neural Network
- convolution works like a filter for images to emphasis certain features
- use `model.summary()` to inspect each layer
```python
tf.keras.layers.Conv2D(<num_filters>, (3, 3), activation='relu', input_shape=(m, n, <color_depth>)),
tf.keras.layers.MaxPooling2D(2, 2),
```
- create `3` pixels by `3` pixels filters
- for every `2` pixels by `2` pixels, pools (keeps) the one with the largest value (size of image /= 4)

