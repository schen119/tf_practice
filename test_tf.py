import tensorflow as tf
import os


l = [1, 2, 3]
l.__iter__()
os.environ["CUDA_VISIBLE_DEVICES"] = "0"


m1 = tf.constant([[2, 2]])   # m1= 1*2
m2 = tf.constant([[3], [3]]) # m2 =2*1
m3 = tf.constant([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
mul_result = tf.matmul(m2,m1)
print(mul_result)



hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))

print(sess.run(m3))