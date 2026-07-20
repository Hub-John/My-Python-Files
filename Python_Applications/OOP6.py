class Demo:
    # Class Variables
    Value1 = 10
    Value2 = 20

    def __init__(self):
        # Instance Variable
        self.No1 = 11
        self.No2 = 21

obj1 = Demo()
obj2 = Demo()

obj1.No1 = 0
print(obj1.No1) # 0
print(obj2.No1) # 11

obj1.Value1 = 0
print(Demo.Value1)