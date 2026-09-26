import tensorflow as tf

inputs = tf.constant([1.0, 2.0, 3.0])

weights = tf.constant([0.5, -0.2, 0.8])

bais = tf.constant(0.1)

weighted_sum = tf.reduce_sum(inputs * weights) + bais

print("\nInputs:", inputs.numpy()) # 1.0, 2.0, 3.0
print("Weights:", weights.numpy()) # 0.5, -0.2, 0.8
print("Bias:", bais.numpy()) # 0.1

print("Weighted Sum:", weighted_sum.numpy()) # 2.6

output = tf.sigmoid(weighted_sum) # 0.93

print("Output is:", output.numpy())