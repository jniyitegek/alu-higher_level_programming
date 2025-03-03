#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[str.find(str.split()[5]):str.find(str.split()[7])] + str[str.find(str.split()[12]):str.find(str.split()[-len(str.split())+1])]
print(str)
