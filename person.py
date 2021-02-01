#Question.C & Question.D
class Person:
    def __init__(self, name, age, height): 
            self.name = name # setting object variable name 
            self.age = age # setting the object variable age
            self.height = height # setting the object variable height

    # method which returns the input values with the specified format in assignment question
    def printValuesOfObjectVariable(self):
           return self.name + " is " + self.age + " years old"
    
    #Question.D
    def __repr__(self):
            return self.name + " is " + self.age + " years old " + self.height +" cm tall"

#Defining object "new_person" for the class Person 
new_person=Person(name='Joe',age='34',height='184')

#invoking the init method and printing the answer for Question.C
print("************************************************************")
print(new_person.printValuesOfObjectVariable())

#invoking the repr method and printing the answer for Question.D
print()
new_person=Person(name='Bob',age='17',height='182')
print(new_person.__repr__())
print("************************************************************")

