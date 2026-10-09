# Step: 1 - Import required libraries

from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences


# Step: 2 - Configuration of values
VOCAB_SIZE = 10000 # consider most frequent 10000 unique words
MAX_LENGTH = 200 # consider max 200


# Step: 3 - Load IMDB dataset
print("Movie Review Sentiments Analysis using LSTM")

print("Loading the data")

(X_train, Y_train), (X_test, Y_test) = imdb.load_data(
    num_words = VOCAB_SIZE
)

print("IMDB dataset loaded sucessfully")

print("Number of Training reviews:", len(X_train))
print("Number of Testing reviews:", len(X_test))

##############################################
# X_train   Reviews use for training
# Y_test    Actual sentiments of training
# X_train   Reviews used for testing
# Y_test    Actual sentiments of testing

# Sentiments
# 0 = Negative Sentiments
# 1 = Positive Sentiments
##############################################

# Step: 4 - Load the word dictonary
word_index = imdb.get_word_index()

##############################################
# Dictonary contains mapping of word and its corresposing number
# Drisham is good movie  -> (20 56 78 43)
# 20 -> Drisham
# 56 -> is
# 78 -> good
# 43 -> movie
##############################################


# Step: 5 - Create reverse dictionary
reverse_word_index = {}

for word, index in word_index.items():
    reverse_word_index[index*3] = word


# Step: 6 - Funtion to decode the review(number to word)

def DecodeReview(encoded_review):
    words = []

    for number in encoded_review:
        if number >= 3: # ignore first 3
            word = reverse_word_index.get(number, "?")
            words.append(word)
    return " ".join(words) # Join the list of words


# Step: 7 - Display Sample reviews

print("----------------- Sample reviews --------------------")

for i in range(3, 7):
    review = DecodeReview(X_train[i])

    print("_"*40)
    print("Review Number: ", i+1)
    print("Review: ")
    print(review)

    print("_"*40)

    if Y_train[i] == 1:
        print("Sentiment : Positive")
    else:
        print("Sentiment : Negative")


# Step: 8 - Adding Padding (X_train)

X_train_padded = pad_sequences(
     X_train,
     maxlen = MAX_LENGTH
)

X_test_padded = pad_sequences(
    X_test,
    maxlen = MAX_LENGTH
)

print("Training data shape:", X_train_padded.shape)
print("Testing data shape:", X_test_padded.shape)


# Step: 9 - Create LSTM Model

model = Sequential()

model.add(
    Embedding(
        input_dim=VOCAB_SIZE,
        output_dim=32 # Each word is represented in 32 values
    )
)

model.add(
    LSTM(
        units = 64 # Size of LSTM hidden state
    )
)

model.add(
    Dense(
        units=1,
        activation="sigmoid"
    )
)


# Project Architecture
# Review -> Embedding -> LSTM -> Dense -> Sigmoid -> Positive / Negative


# Step: 10 - 

model.compile(
    optimizer = "adam", 
    loss = "binary_crossentropy", #
    metrics = ["accuracy"] # measure classification accuracy
)

print("Model compile successfully")


# Step: 11 - Train the model

print("Model training")

model.fit(
    X_train_padded,     # Input training reviws
    Y_train,            # Actual sentiments labels
    epochs = 3,         # complete dataset gets processes 3 times
    batch_size = 64,     # Process 64 reviews in one batch
    validation_split = 0.2 # Use 20% training for validation
)

print("Model training gets completed")

# Step: 12 - Evaluate the model

accuracy = model.evaluate(
    X_test_padded,  # Testing reviews
    Y_test,         # Actual testing labels
    verbose = 0     # Don't display the process bar
)

print("Testing accuracy:", accuracy)


# Step: 13 - Predict the review

TEST_REVIEW_NUMBER = 0

original_review = X_test[TEST_REVIEW_NUMBER]
decoded_review = DecodeReview(original_review)

print("Review given to the model")
print(decoded_review)


# Step: 14 - Get the actual sentiment
actual_value = Y_test[TEST_REVIEW_NUMBER]

if actual_value == 1:
    actual_sentiment = "POSITIVE"
else:
    actual_sentiment = "NEGATIVE"

print("Actual Sentiment : ",actual_sentiment)


# Step: 15 - Predict the sentiment

review_for_prediction = X_test_padded[TEST_REVIEW_NUMBER : TEST_REVIEW_NUMBER + 1]

prediction = model.predict(
    review_for_prediction,
    verbose = 0
)

probabality = prediction[0][0]

if probabality >= 0.5:
    predcited_sentiment = "POSITIVE"
else:
    predcited_sentiment = "NEGATIVE"

print("-"*40)

print("Fianl Result")

print("-"*40)

print("Prediction Probablity : ",probabality)
print("Actual sentiment : ",actual_sentiment)
print("Predicted sentiment : ",predcited_sentiment)

print("-"*40)