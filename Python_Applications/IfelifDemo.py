print("------------------------------------------------------------") # print("_"*40)
print("----------------- Ticket Priceing Software -----------------")
print("------------------------------------------------------------")

print("Please enter your age: ")
Age = int(input()) #57

if(Age <= 5): # false
    print("Your ticket is free!")
elif(Age > 5 and Age <= 18): # True and False
    print("Ticket Price: 900")
elif(Age > 18 and Age <= 40): # True and False
    print("Ticket Price: 1200")
else:
    print("Ticket Price: 500") # True