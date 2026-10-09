# Numberic encoding

from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [       # sentences
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(sentences)

sequences = tokenizer.texts_to_sequences(sentences)

print("--------------------------------------------------")
for sentance, sequence in zip(sentences, sequences):
    print("Sentance: ", sentance)
    print("Sequence: ", sequences)
    print("--------------------------------------------------")