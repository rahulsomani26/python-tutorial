'''
Dictionary comprehension is an elegant and concise way to create dictionaries.
Syntax
dictionary = {key: value for vars in iterable}

'''

myDict = {}  # myDict = dict()

for num in range(1, 10):
    myDict[num] = num*num
print(myDict)


newDict = {num: num * num for num in range(1, 10)}
print(newDict)
print(newDict.items())
