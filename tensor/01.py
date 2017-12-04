import tensorflow as tf

node0 = tf.constant(3, tf.float32)
node1 = tf.constant(4, tf.float32)
node2 = tf.add(node0, node1)
print(node0)
print(node1)
print(node2)
hello = tf.constant("foo!")

sess = tf.Session()

print(sess.run(node0))
print(sess.run(node1))
print(sess.run(node2))
