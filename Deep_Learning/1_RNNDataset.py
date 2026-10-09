sentences = [ # sentences
    "food was good",
    "food was bad",
    "food was not good"
]

labels = [1,0,0] # sentiments

print("-----------------------------")
for sentence, label in zip(sentences, labels): # what is zip?
    sentiment = "Positive" if label == 1 else "Negative" # conditions

    print("Sentence: ",sentence)
    print("Label: ",label)
    print("Meaning: ",sentiment)
    print("-----------------------------")