# Step: 1 - Import required libraries

from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences


# Step: 2 - Configuration of values

VOCAB_SIZE = 10000  # consider most frequent 10000 unique words
MAX_LENGTH = 200    # consider maximum 200 words in review


# Step: 3 - Load IMDB dataset

print("Movie Review Sentiments Analysis using LSTM")

print("Loading the data")

(X_train, Y_train), (X_test, Y_test) = imdb.load_data(num_words = VOCAB_SIZE)

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