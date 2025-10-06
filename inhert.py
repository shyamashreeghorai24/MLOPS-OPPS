# 
#simple inheritance
# class Animal:
#     def __init__(self,name):
#         self._name=name

#     def speak(self):
#         print(f"{self._name} makes a sound.")

# class dog(Animal):
#     def speak(self):
#         print(f"{self._name} makes a sound.")  

# an1 = Animal("Generic Animal")
# print(an1.speak())

# dg1 = dog("Bull Dog")
# dg1.speak()
#simple inheritance
# class Animal:
#     def __init__(self,name):
#         self.__name=name

#     def speak(self):
#         print(f"{self.__name} makes a sound.")

# class dog(Animal):
#     def speak(self):
#         print(f"{self.__name} makes a sound.")  
 
# class Animal:
#     def __init__(self,name):
#         self.name=name

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# class dog(Animal):
#     def __init__(self):
#         self.behaviour="friendly" #
#     def speak(self):
#         print(f"{self.name} makes a sound.He is very {self.behaviour}")
# # an1 = Animal("Generic Animal")
# print(an1.speak())

# dg1 = dog()
# dg1.speak()   
#super keyword
# class Animal:
#     def __init__(self):
#         self.name="Buddy"

#     def speak(self):
#         print(f"{self.name} makes a sound.")

#derived class
# class Dog(Animal):
#     def __init__(self,breed):
#         super().__init__()
#         self.breed = breed 

#     def speak(self):
#         super().speak() #call the base class method
#         print(f"{self.name} barks. It is a {self.breed}.")

#create a instance of Dog
# dog = Dog("Golden Retriver")
# dog.speak()                            

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