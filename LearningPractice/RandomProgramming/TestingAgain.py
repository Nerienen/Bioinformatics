import tensorflow as tf
import keras
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import seaborn as sns
import sklearn

plt.style.use('seaborn-v0_8-darkgrid')

#print(plt.style.available)

# house with 1000 square feet(sqft) sold for $300,000 
# and a house with 2000 square feet sold for $500,000. 
# These two points will constitute our data or training set. 
# In this lab, the units of size are 1000 sqft and the units 
# of price are 1000s of dollars.
# predict price for other houses - say, a house with 1200 sqft. 


# x_train is the input variable (size in square feet)
# y_train is the target (dollars)

x_train = np.array([1000, 2000], dtype=np.float32)
y_train = np.array([300000, 500000], dtype=np.float32)

print(f"x_train = {x_train}")
print(f"y_train = {y_train}")

plt.clf()  # Clear the current figure


# Plot the data points
plt.scatter(x_train, y_train, marker='x', c='r')
# Set the title
plt.title("Housing Prices")
# Set the y-axis label
plt.ylabel('Price (dollars)')
# Set the x-axis label
plt.xlabel('Size (sqft)')

# show the plot
plt.show()

print(len(x_train), len(y_train))  # Should both be 2

# define variables for weight and bias, initialized randomly
w = tf.Variable(tf.random.normal(shape=[]))
b = tf.Variable(tf.random.normal(shape=[]))

learning_rate = 1e-7  # small because values are large
optimizer = tf.optimizers.SGD(learning_rate)

# define linear model
def linear_model(x):
    return w * x + b

# Define loss function (mean squared error)
def loss_fn(y_true, y_pred):
    return tf.reduce_mean(tf.square(y_true - y_pred))

# m is the number of training examples

# training step function
def train_step(x, y):
    with tf.GradientTape() as tape:
        predictions = linear_model(x)
        loss = loss_fn(y, predictions)
    gradients = tape.gradient(loss, [w, b])
    optimizer.apply_gradients(zip(gradients, [w, b]))
    return loss

# training loop
epochs = 2000
for epoch in range(epochs):
    loss = train_step(x_train, y_train)
    if epoch % 200 == 0:
        print(f"Epoch {epoch}, Loss: {loss.numpy()}, w: {w.numpy()}, b: {b.numpy()}")

print(f"Trained weight (w): {w.numpy()}")
print(f"Trained bias (b): {b.numpy()}")

# Predict for training data and plot
y_pred = linear_model(x_train)

plt.plot(x_train, y_pred, c='b', label='Model Prediction')
plt.scatter(x_train, y_train, marker='x', c='r', label='Actual Values')
plt.title("Housing Prices")
plt.ylabel('Price (dollars)')
plt.xlabel('Size (sqft)')
plt.legend()
plt.show()

print ("predicting trained line")

# Predict price for 1200 sqft house
x_i = 1200.0
predicted_price = linear_model(x_i).numpy()
print(f"Predicted price for house with {x_i} sqft: ${predicted_price:.0f} dollars")
print("training complete")
# A tuple is a fundamental data structure in programming, representing an ordered, immutable collection of items



# You will use (x (𝑖), y (𝑖) to denote the  𝑖𝑡ℎ training example. Since Python is zero indexed, (x (0), y (0)) is (1.0, 300.0) and (x (1) , y (1) ) is (2.0, 500.0).

# To access a value in a Numpy array, one indexes the array with the desired offset. For example the syntax to access location zero of x_train is x_train[0]. Run the next code block below to get the  𝑖𝑡ℎ
  # training example.
