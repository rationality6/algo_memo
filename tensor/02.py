import tensorflow as tf

node0 = tf.placeholder(tf.float32)
# node1 = tf.placeholder(tf.float32)

print(node0)
# print(node1)

hello = tf.constant("foo!")

sess = tf.Session()

print(sess.run(node0, feed_dict=4))
# print(sess.run(node1, feed_dict={a: [1, 3], b: [2, 4]}))
