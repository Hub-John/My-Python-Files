import tensorflow as tf

tensor1 = tf.constant([10,20,30])
tensor2 = tf.constant([1,2,3])

addition = tf.add(tensor1, tensor2)
print("\nAdditon is - ", addition) # 11, 22, 22

substraction = tf.subtract(tensor1, tensor2)
print("\nSubstraction is - ", substraction) # 9,18,27

multiplication = tf.multiply(tensor1, tensor2)
print("\nMultiplication is - ", multiplication) # 10,40,90

division = tf.divide(tensor1, tensor2)
print("\nDivision is - ", division) # 10.0, 10.0, 10.0

square = tf.square(tensor1)
print("\nSquare is - ", square) # 100, 400, 900

sum = tf.reduce_sum(tensor1)
print("\nSum is - ", sum) # 60

mean = tf.reduce_mean(tensor1)
print("\nMean is - ", mean) # 20