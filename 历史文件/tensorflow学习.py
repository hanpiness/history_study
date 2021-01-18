import tensorflow as tf
print(tf.__version__)
import tensorflow as tf
scalar = tf.constant(100)
vector = tf.constant([1,2,3,4,5])
matrix = tf.constant([[1,2,3],[4,5,6]])
cube_matrix = tf.constant([[[1],[2],[3]],[[4],[5,][6]],[[7],[8],[9]]])

print(scalar.shape)
print(vector.shape)
print(matrix.shape)
print(cube_matrix.get_shape())