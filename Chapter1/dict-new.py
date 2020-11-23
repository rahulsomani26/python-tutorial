class Company:
    comapnyName = 'TCS'  # class variables
    # numberOfEmployees = 0

    def __init__(self, name, age):     # initializer or constructor
        print(' object created')
        self.name = name   # class variables or instance variables
        self.age = age

    def __del__(self):  # destuctor
        print('object destroyed')


ob1 = Company('Rahul', 38)
ob2 = Company('me', 28)
# print(ob1.name)
ob1.age = 39
ob1.comapnyName = 'capgemini'
print(ob1.name, ob1.age, Company.comapnyName, ob1.comapnyName)
print(dir(ob1))

# print(ob1.comapnyName)
# print(ob2.comapnyName)
# print(dir(Company))
# print(dir(ob1))
