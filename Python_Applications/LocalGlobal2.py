no = 11 # Global Varible

def Display():
    a = 21 # Local Variable
    print("From Display:", no)
    print("From display value of a is: ", a)

def Demo():
    print("From Demo:", no)
    print("From demo value of a is:", a) # Error

Display()
Demo()