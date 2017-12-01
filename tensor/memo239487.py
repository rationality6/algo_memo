import tensorflow as tf
# print(tf.__version__)

# hello = tf.constant("Hello, TensorFlow!")
# sess = tf.Session()
# print(sess.run(hello))

# node1 = tf.constant(3.0, tf.float32)
# node2 = tf.constant(4.0)
# node3 = tf.add(node1, node2)
#
# print("node1:", node1, "node2:", node2)
# print("node3: ", node3)
#
# sess = tf.Session()
# print("sess.run(node1, node2): ", sess.run([node1, node2]))
# print("sess.run(node3): ", sess.run(node3))

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b

sess = tf.Session()

print(sess.run(adder_node, feed_dict={a: 3, b: 4.5}))
print(sess.run(adder_node, feed_dict={a: [1, 3], b: [2, 4]}))

x_train = [1, 2, 3]
y_train = [1, 2, 3]

W = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')

hypothesis = x_train * W + b

cost = tf.reduce_mean(tf.square(hypothesis - y_train))

arr0 = [6, 8, 7, 9, 93]
print((1 / len(arr0)) * sum(arr0))
print(sum(arr0) / len(arr0))
