sentence = "food was not good"

words = sentence.split() # food/was/not/good(Tokens)

for index, word in enumerate(words): # explain 'enumerate'
    print("Position ", index+1, ":", word)