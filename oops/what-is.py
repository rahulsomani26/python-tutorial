'''
class : It is a blueprint of an object , or a prototype 
 objects ; They have an existence 
classes have attributes, and methods(functions)
'''


class Employee:
    '''
    test documentation
    '''

    position = 'test'   # This is a class variable

    def __init__(self, name, age):
        self.name = name   # instance variable  ( object variable )
        self.age = age  # instance variable
        # self.pay=pay

    def myEmp(self):
        print(' Hi {}, your age is {}'.format(self.name, self.age))


# e1 = Employee('tst', 45)

emp1 = Employee('rahul', 38)

emp2 = Employee('ratnesh', 36)

print(emp1.position)
print(emp2.position)

# print(emp2.__dict__)
# print(Employee.__dict__)

# Employee.myEmp(emp2)
# emp2.myEmp()
# e1.myEmp()


# emp1.myEmp()
# emp2.myEmp()

# print(emp1.name)
# print(emp2.age)


# class Test:
#     def __init__(self):
#         print(" Initializer called")


# t = Test()
# p = Test()
# c = Test()
