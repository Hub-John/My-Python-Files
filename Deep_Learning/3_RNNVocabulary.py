sentences = [       # sentences
    "food was good",
    "food was bad",
    "food was not good"
]

vocabulary = []     # all unique value

for sentence in sentences:
    words = sentence.split()

    for word in words:
        if word not in vocabulary:
            vocabulary.append(word)

for index, x in enumerate(vocabulary): # what is 'enumerate'
    print("Position ", index+1, ":", x)