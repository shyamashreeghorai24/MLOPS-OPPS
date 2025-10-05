#iniriate a class
class employee:
    # special methos/magic method - constructor
    def __init__(self):
        print(id(self))
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 5000
        self.designation = "SDE"
        print("attributes/data have been initiated")

    def travel(self,destination):
        print("This travel function was called manually")
        print(f"Employeeis now travelling to {destination}")    

# creating an obj/instance of the class
sam = employee()   
print(id(sam))  
ram = employee()
print(id(ram))
# print(sam.id)
# print(sam.salary)
# print(sam.designation)   
# print(sam.travel("kerala"))
# print(type(sam))
sam.name = "sam kumar"
print(sam.name)