class Demo:
    # Class Variables
    Value1 = 10
    Value2 = 20

    def __init__(self):
        # Instance Variable
        self.No1 = 11
        self.No2 = 22

    # Instance Method
    def fun(self):
        print("Inside instance method name as fun")
        print(self.No1)
        print(self.No2)
        print(Demo.Value1)
        print(Demo.Value2)

    # Class Method
    @classmethod
    def gun(cls):
        print("Inside class method name as gun")
        # print(Demo.No1) Not Allowed
        # print(Demo.No2) Not Allowed
        print(cls.Value1)
        print(cls.Value2)

    # Static Method
    @staticmethod
    def sun():
        print("Inside static method name as sun")
        print(Demo.Value1) # static method it should not access intstance variable
        print(Demo.Value2)
        

Demo.sun()