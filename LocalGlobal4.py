no = 11

def Display():
    global no # Refer Global Variable
    no = 21 
    print("From Display:", no) # local variable changes global value

print("Before:", no)
Display() # Because of display function local variable it change Global variable
print("After:", no)