import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

import tensorflow as tf
import matplotlib.pyplot as plt
import csv
import numpy as np


x_graph = []
y_graph = []

with open('co2.csv','r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x_graph.append(float(row[0]))
        y_graph.append(float(row[1]))

plt.plot(x_graph,y_graph, label='Emission values')
plt.xlabel('Year')
plt.ylabel('Emission')
plt.title('Carbon-dioxide Emission\n(metric tons per capita)')
plt.legend()
plt.show()



# Model parameters
m = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
# Model input and output
x = tf.placeholder(tf.float32)
linear_model = m * x + b
y = tf.placeholder(tf.float32)

# loss
loss = tf.reduce_sum(tf.square(linear_model - y)) # sum of the squares
# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)


# training data
x_train = [0, 1, 2, 3]
y_train = [1, 2, 3, 4]

# training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init) # reset values to wrong
for i in range(1000):
  sess.run(train, {x: x_train, y: y_train})

# evaluate training accuracy
curr_m, curr_b, curr_loss = sess.run([m, b, loss], {x: x_train, y: y_train})
print("m: %s b: %s loss: %s"%(curr_m, curr_b, curr_loss))
