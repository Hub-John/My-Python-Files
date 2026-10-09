import numpy as np

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense

# Step: 1 - Load the data
train_sentences = [
    "\nfood was good",
    "food was bad",
    "food was excellent",
    "food was terriable",
    "service was good",
    "service was bad",
    "service was excellent",
    "service was terriable",
    "ambience was good",
    "ambience was bad",
    "ambience was excellent",
    "ambience was terriable"
]

train_labels = [
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0,
    1,
    0
]

# Step: 2 - Tokenization
tokenizer = Tokenizer(oov_token = "<OOV>")
tokenizer.fit_on_texts(train_sentences)


# Step: 3 - Convert traing data into sequence
train_sequence = tokenizer.texts_to_sequences(train_sentences)

print("_"*50)
print("\nTraining sequences")
print("_"*50)


# Step: 4 - Apply padding
max_length = 4

X_train = pad_sequences(
    train_sequence,
    maxlen = max_length, 
    padding = "pre"
)

Y_train = np.array(train_labels)

print("\nPadded training data:")
print(X_train)

print("\nTraining labels:")
print(Y_train)
print("_"*50)