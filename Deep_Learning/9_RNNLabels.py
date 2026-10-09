sentences = [
    "food was good",
    "food was bad",
    "food was not good"
]

labels = [1,0,0]

print("-------------------------------")
for sentence , label in zip(sentences,labels):
    print("Sentance:",sentence)
    print("Label: ",label)

    if label == 1:
        print("Meaning: Positive sentiment")
    else:
        print("Meaning: Negative sentiment")

    print("-------------------------------")