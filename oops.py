# class example

class Car:
    # attributes
    brand = "Toyota"
    color = "White"

    # method
    def info(self):
        print("Brand:", self.brand)
        print("Color:", self.color)



# object creation
c = Car()
c.info()





# object example

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)

s1 = Student("Himanshu", 101)
s1.show()




# ENCAPSULATION example

class Bank:
    def __init__(self):
        self.balance = 5000        # public
        self._accountNo = 123456   # protected
        self.__pin = 4321          # private

    def show(self):
        print("Balance:", self.balance)
        print("Account No:", self._accountNo)
        print("PIN:", self.__pin)

b = Bank()
b.show()

print(b.balance)        # public → allowed
print(b._accountNo)     # protected → allowed but not recommended
print(b._Bank__pin)     # private → allowed using name mangling




# INHERITANCE example

  #A) Single Inheritance

  class A:
    def display(self):
        print("Parent Class")

class B(A):
    def show(self):
        print("Child Class")

b = B()
b.display()
b.show()
  


  #B) Multilevel Inheritance

  class A:
    def a(self):
        print("A class")

class B(A):
    def b(self):
        print("B class")

class C(B):
    def c(self):
        print("C class")

c = C()
c.a()
c.b()
c.c()




#C) Multiple Inheritance

class A:
    def a(self):
        print("A class")

class B:
    def b(self):
        print("B class")

class C(A, B):
    pass

c = C()
c.a()
c.b()


#D) Hierarchical Inheritance

class Parent:
    def home(self):
        print("Parent Home")

class Child1(Parent):
    pass

class Child2(Parent):
    pass

c1 = Child1()
c2 = Child2()

c1.home()
c2.home()



#E) Hybrid Inheritance

class A:
    def a(self):
        print("A")

class B(A):
    def b(self):
        print("B")

class C(A):
    def c(self):
        print("C")

class D(B, C):
    def d(self):
        print("D")

d = D()
d.a()
d.b()
d.c()
d.d()




#POLYMORPHISM example

#A) Method Overriding
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

d = Dog()
d.sound()



#B) Same function, different behavior

def add(a, b, c=0):
    return a + b + c

print(add(5, 10))     
print(add(5, 10, 20))



#C) Polymorphism with Class Methods

class Cat:
    def sound(self):
        print("Meow")

class Cow:
    def sound(self):
        print("Moo")

def animal_sound(animal):
    animal.sound()

animal_sound(Cat())
animal_sound(Cow())



#ABSTRACTION

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

s = Square(5)
print("Area:", s.area())




#CONSTRUCTOR example

class Student:
    def __init__(self, name):
        self.name = name
        print("Constructor called")

s = Student("Himanshu")



#DESTRUCTOR example

class Demo:
    def __init__(self):
        print("Object Created")

    def __del__(self):
        print("Object Destroyed")

d = Demo()
del d



