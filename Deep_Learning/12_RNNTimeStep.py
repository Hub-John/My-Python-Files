sentence = "food was not good"

# Time step 1 2 3 4
# Tokens    1 2 5 3
# Embedding []

words = sentence.split()

print("_"*60)
print("\nActual Sentence is:", words)
print("_"*60)

for index, word in enumerate(words):
    print("\nTime Step:", index+1, word)

print("_"*50)