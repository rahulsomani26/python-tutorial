'''
Python do not have variables 
They have names 
Objects are stored with names, given a reference and a label 
Each object can have more than one name ???
'''

l = [1, 2]
print(type(l))
print(isinstance(l, object))  # Everything is an object
a = l
l.append(3)
a = l

print(l is a)
print(a is l)
print(id(a), id(l))
