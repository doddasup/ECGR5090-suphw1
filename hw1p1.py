#!/usr/bin/env python
import numpy
import matplotlib.pyplot as plt
from person import * 

list_of_names = ['Roger', 'Mary', 'Luisa', 'Elvis']
list_of_ages  = [23, 24, 19, 86]
list_of_heights_cm = [175, 162, 178, 182]
###########################################################################
#Question. A & B
#List Declaration to collect name Length
nameLength = []
print("************************************************************")
print("PFB the result of hw1p1.py script execution")
print()
for name in list_of_names:
  print("The name {:} is {:} letters long".format(name, len(name)))
  
  #Appending the name length to list
  nameLength.append(len(name))
  
#printing the name Length list 
print("************************************************************")
print("list of lengths of names printed below")
print()
print(nameLength)
print("************************************************************")
###########################################################################
#Question .F
#Converting list of ages to array using numpy
arrayOfAges = numpy.array(list_of_ages)

#Converting list of heights to array using numpy 
arrayOfHeight = numpy.array(list_of_heights_cm)

#Printing arrays of Ages and Heights
print("PFB the array of Ages")
print()
print(arrayOfAges)
print()
print("PFB the array of height")
print()
print(arrayOfHeight)
print("************************************************************")
###########################################################################
#Question.G
#Calculating the mean of ages using numpy
meanOfAges = numpy.mean(list_of_ages)
print("PFB the mean of ages calculated using numpy.mean")
print()
print(meanOfAges)
print()

print("Printing the ages in list_of_ages with f-statement")
print()
count=1
#Printing the ages with f statement
for item in list_of_ages:
    print(f"Printing No:{count} value in the list_of_ages {item}")
    count=count+1
print("************************************************************")
###########################################################################
#Question.H
x = list_of_ages
y = list_of_heights_cm

#Plotting graph 
plt.scatter(x, y);


#X-axis label
plt.xlabel('Age') 
#Y-axis label
plt.ylabel('Height')
#Graph title  
plt.title('Age-Height Graph') 
# function to show the plot 
plt.show()
print("************************************************************")
###########################################################################

#Question. E
#Creating Dictionary with name as key and new_person object's return result as value 
print("Printing the dictionary created with name as value and person object as keys")
print()
people = dict.fromkeys(list_of_names,new_person.printValuesOfObjectVariable())
print(people)
print()