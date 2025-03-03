#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
print(str_text[str_text.find("object-oriented"):str_text.find("programming") + len("programming")] + str_text[str_text.rfind("Python") - 5:])
