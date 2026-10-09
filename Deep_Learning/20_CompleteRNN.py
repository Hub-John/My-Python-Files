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


# Step: 5 - Calculate vocabulary size
vocab_size = len(tokenizer.word_index) + 1
print("\nVocabulary size:", vocab_size)
print("_"*50)

# Step: 6 - Build
model = Sequential()

model.add(
    Embedding(
        input_dim=vocab_size,
        output_dim=8
        # input_length=max_length
    )
)

model.add(
    SimpleRNN(
        units = 8,
        activation = "tanh"
    )
)

model.add(
    Dense(
        units=1,
        activation="sigmoid"
    )
)

# Step: 7 - Compile the model
model.compile(
    optimizer = "adam",
    loss = "binary_crossentropy",
    metrics = ["accuracy"]
)

# Step: 8 - Display model
model.build(input_shape = (None, max_length))
print("\nModel architecture\n")
model.summary()
print("_"*100)

# Step: 9 - Train the model
history = model.fit(
    X_train,
    Y_train,
    epochs = 100,
    verbose = 1
)
print("\nModel training complete")
print("_"*100)

# Step: 10 - Create unseen data
test_sentences = [
    "Service was amazing",
    "Service was horriable",
    "Exprience was excellent",
    "Exprience was terriable"
]

# Step: 11 - convert text to sequence
test_sequences = tokenizer.texts_to_sequences(test_sentences)

X_test = pad_sequences(
    test_sequences,
    maxlen = max_length,
    padding = "pre"
)

# Step: 12 - Predict the sentiment
for text, sequence, padded in zip(test_sentences, test_sequences, X_test):
    input_data = np.array([padded])

    prediction = model.predict(input_data, verbose=0)

    probability = float(prediction[0][0])

    print("\nSentence:", text)
    print("Sequence:", sequence)
    print("Padded sequence:", padded)
    print("Prediction:", probability)

    if probability >= 0.5:
        print("Sentiment: Positive")
    else:
        print("Sentiment: Negative")


print("_"*100)