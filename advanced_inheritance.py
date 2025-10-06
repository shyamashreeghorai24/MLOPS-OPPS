class Parent:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

#derived class
class Child(Parent):
    def play(self):
        print(f"{self.name} is playing")

child = Child("Alice")
child.greet()
child.play() 
# Multilevel Inheritance
class Grandparent:
    def __init__(self,name):
        self.name = name
    def tell_story(self):
        print(f"{self.name} tell us a story")

class Parent(Grandparent):
    def work(self):
        print(f"{self.name} is working")

class Child(Parent):
    def play(self):
        print(f"{self.name} is playing")        
                                 
child = Child("alice")
child.tell_story()
child.work()
child.play()                                 
# Hirarchical Inheritance

class Parent:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"Hello, my name is {self.name}")    

class Child1(Parent):
    def play(self):
        print(f"{self.name} is playing.")

class Child2(Parent):
    def study(self):
        print(f"{self.name}is studying.")    

child1 = Child1("Bob")
child1.greet()
child1.play()
child2 = Child2("Jon")     
child2.greet()
child2.study()  
# Multiple Inheritance,Diamond Problem
class A:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print(f"Hello, my name is {self.name}")

class B(A):
    def greet(self):
        print(f"This is from B,{self.name}")
        super().greet()

class C(A):
    def greet(self):
        print(f"This is from C,{self.name}")
        super().greet()

class D(B,C):
    def greet(self):
        print(f"This is from D,{self.name}")   
        super().greet()                     
d1 = D("Bob")
d1.greet()

# Hybrid Inheritance
class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print(f"{self.name} makes a sound")

#Intermediate class 2 (Hirarchical)
class Mammal(Animal):
    def feed(self):
        print(f"{self.name} is feeding milk.")

#Intermeidate class 2 (multiple)
class Bird(Animal):
    def fly(self):
        print(f"{self.name} is flying")

#Derived class(Multiple Inheritance)
class Bat(Mammal, Bird):
    def __init__(self,name):
        Mammal.__init__(self,name) #Explicitely calling the constructure

    def noctural(self):
        print(f"{self.name} is noctural")     

bat = Bat("Bruce")
bat.sound()
bat.feed()
bat.fly()
bat.noctural()                                  