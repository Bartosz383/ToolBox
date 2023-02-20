import random

class MathExcerciseRandomizer():
    def __init__(self):
        self.a = random.randint(1,10)
        self.b = random.randint(1,10)

    def RandomNumbers(self):
        print("add, subtract, multiply and divide the two numbers ", self.a, " ", self.b)
        return

    def Adding(self):
        c = self.a + self.b
        print("The result of the addition is ", c)

    def Substraction(self):
        c = self.a - self.b
        print("The result of the substraction is ", c)

    def Multiplication(self):
        c = self.a * self.b
        print("The result of the multiplication is ", c)

    def Division(self):
        c = self.a / self.b
        print("The result of the division is ", c)

    def Powering(self):
        c = self.a ** self.b
        print("The result of the powering is ", c)

