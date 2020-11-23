def myFunction(name, age, gender):

    return name.lower(), age, gender


# myList = ['RAJ', 34, 'Male']
# print(id(myList))

# print(hex(id(myList)))
# print(hex(id(myList[0])))
# print(hex(id(myList[1])))

# print(id(myList[2]))

# name, age, gender = myFunction(*myList)
# print(name, age, gender)
# print(*name, age, *gender)

# num = []
# print(id(num))
# num = [1, 2, 3, 9]
# print(id(num))

# name = []
# address = []
# print(id(name))
# print(id(address))

# name = ['rahul', 'somani']
# print(id(name))

# print(id(name[0]))
# print(id(name[1]))

# name = []
# print(id(name))

def add(x, y, m):
    return (x + y+m)


num = [1, 2, 3]
print(add(*num))


numd = {'x': 1, 'y': 2, 'm': 3}
print(add(**numd))
print(add(*numd))
print(add(x=1, y=5, m=0))
