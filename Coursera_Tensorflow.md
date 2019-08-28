# Week 1
- https://github.com/lmoroney/dlaicourse/blob/master/Course%201%20-%20Part%202%20-%20Lesson%202%20-%20Notebook.ipynb
- http://playground.tensorflow.org/
## Linear regression
```python
import tensorflow as tf
import numpy as np
from tensorflow import keras

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
