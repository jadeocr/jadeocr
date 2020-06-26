import os
import tensorflow as tf

print('Starting Tensorflow test!')
sess = tf.Session()
test_computation = sess.run(tf.constant(123)*tf.constant(456))
print('The above should return "56088". The result was ' + str(test_computation))


print('Starting GPU test')
with tf.device('/gpu:0'):
 a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3], name='a')
 b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2], name='b')
 c = tf.matmul(a, b)
# Creates a session with log_device_placement set to True.
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
# Runs the op.
print sess.run

print('GPU Test Success!')
