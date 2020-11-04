import collections

GeoLocation = collections.namedtuple('GeoLocation', field_names=[
    'name',
    'age',
    'gender',
    'employed'
])

empBook = GeoLocation(name='rahul', age=38, gender='male', employed=True)
print(empBook.age)
print(empBook.employed)
# empBook.gender = 'female'
# test = empBook._asdict()

# print(test['name'])
