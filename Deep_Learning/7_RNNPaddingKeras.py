from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = [       # sentences
    "food was good",
    "food was bad",
    "food was not good"
]

tokenizer = Tokenizer()

tokenizer.fit_on_texts(sentences)

sequences = tokenizer.texts_to_sequences(sentences)

print("\nOriginal Sequences:\n")
for sequence in sequences:
    print(sequence, "length -", len(sequence))

print("\nAll sequences are of different lengths.\n")

max_length = 4

padded_sequances = pad_sequences(
    sequences,
    maxlen = max_length,
    padding = "pre"
)

print("-----------------------------------")
for sentance, sequence, padded in zip(sentences, sequences, padded_sequances):
    print("Sentance: ", sentance)
    print("Original sequences: ", sequence)
    print("Padded sequences", padded)
    print("-----------------------------------")
