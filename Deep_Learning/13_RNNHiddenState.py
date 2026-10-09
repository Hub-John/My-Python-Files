# Remember previous state(in memory)

words = ['food', 'was', 'not', 'good']

hidden_state = "empty memory"

print("_"*50)
print("\nInput Tokens: ", words)

print("_"*50)
print("\nIntial hidden state: ", hidden_state)
print("_"*50)

for index, word in enumerate(words):
    print("\nTime step: ",index+1)
    print("Current word: ", word)
    print("Previous memory: ", hidden_state)

    hidden_state = "memory after reading " + "'" + " ".join(words[:index + 1]) + "'"
    print("Updated memory: ", hidden_state)
    print("_"*50)