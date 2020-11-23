class Test:
    classVar = 'hello'

    def __init__(self, name):
        self.name = name

    def printRecord(self):
        print(' Hi your name is {}'.format(self.name))


t1 = Test('first')
t2 = Test('second')
print(t1.__dict__)

print(Test.__dict__)


# t1.printRecord()
# t2.printRecord()
# print(t1.classVar)
# print(t2.classVar)
# print(Test.classVar)
