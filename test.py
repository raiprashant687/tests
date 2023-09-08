# def fibonacci(n):
#     a = 0
#     b =1
#     print(a)
#     print(b)
#     for i in range(2,n):
#         a, b = b, a + b
#         print(b)
#
#
#
#
#
# fibonacci(7)

# def factorial(n):
#     if n ==1:
#         return 1
#     elif n ==0:
#         return 1
#     elif n>1:
#         return (n*factorial(n-1))
#
# print(factorial(5))
from abc import ABC,abstractmethod

class Name(ABC):
    @abstractmethod
    def printName(self):
        pass

class SirName(Name):
    def printName(self):
        print("I am printing the Name")

x = SirName()
x.printName()