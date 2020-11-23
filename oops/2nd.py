class Employee:
    '''
        Class employee of TCS
    '''
    companyName = 'TCS'  # class variable
    numberOfEmps = 0
    payHike = 1.03

    def __init__(self, first, last, dob):
        self.first_name = first  # instance variable
        self.last_name = last
        self.dob = dob
        Employee.numberOfEmps += 1

    def fullName(self):
        return '{} {}'.format(self.first_name.title(), self.last_name.title())

    def empCount(self):
        return self.numberOfEmps

    def printRecord(self):
        print('------{}------------------{}-----------------------{}'.format(
            self.first_name.title(), self.last_name.title(), self.dob))

    @classmethod
    def increaseHike(cls, hike_amount):
        cls.payHike = hike_amount

    @classmethod
    def fromString(cls, str_data):
        first, last, dob = str_data.split('-')
        return cls(first, last, dob)


'''
@classmethod
Transform a method into a class method.
A class method receives the class as implicit first argument, just like an 
instance method receives the instance. To declare a class method, use this idiom:

class C:
    @classmethod
    def f(cls, arg1, arg2, ...): ...


 


 
classmethods are also used as a form of alternative constructor ( constructs an object of a class)

'''


emp1 = Employee('amit', 'lal', '26/05/1988')
emp2 = Employee('durgesh', 'shreshta', '13/Aug/1960')

# print(Employee.payHike)
# print(emp1.payHike)
# print(emp2.payHike)

# emp1.increaseHike(1.05)

# print(emp1.payHike)
# print(emp2.payHike)


# print(emp1.fullName())
# emp2.printRecord()

# print(emp1.__dict__)
# emp1.companyName = 'Capgemini'
# print(emp1.__dict__)
# print(Employee.__dict__)
# print(Employee.empCount(emp2))
# print(emp1.empCount())

emp3 = Employee.fromString('rahul-somani-25/05/1978')
print(Employee.numberOfEmps)
print(emp3.__dict__)


class Developer(Employee):
    pass


dev1 = Developer('aqua', 'fina', '19-11-1989')
print(dev1.__dict__)
print(Developer.__dict__)
print(help(Developer))
