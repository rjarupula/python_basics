
class Person:

    #create your class here
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print(self):
        print("The name of the person is {} and the age is {}.".format(self.name, self.age))
        
#input values for Name and Age variable
name = input()
age = input()
p = Person(name, age) # initialize the Object of a Class
p.print() #Calling function using Class Object
