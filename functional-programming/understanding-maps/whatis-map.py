'''
map() loops over the items of an input iterable (or iterables) and returns an iterator that 
results from applying a transformation function to every item in the original input iterable.

map() takes a function object and an iterable (or multiple iterables) as arguments and returns 
an iterator that yields transformed items on demand. The function’s signature is defined as 
follows:
Syntax:

map(function, iterable[, iterable1, iterable2,..., iterableN])

map() applies function to each item in iterable in a loop and returns a new iterator that yields
transformed items on demand. function can be any Python function that takes a number of arguments
equal to the number of iterables you pass to map().

The operation that map() performs is commonly known as a mapping because it maps every item in an
input iterable to a new item in a resulting iterable. To do that, map() applies a transformation 
function to all the items in the input iterable.

'''

'''
    1. Using for loop
'''

numbers = [1, 2, 3, 4, 5]
# squareNumbers = []
# for num in numbers:
#     squareNumbers.append(num ** 2)
# print(squareNumbers)

'''
2. Using list comprehension
'''
# squareNumbers = [num ** 2 for num in numbers]
# print(squareNumbers)

'''
3. Using map
'''


def squareNumbers(num):
    return num ** 2


squared = map(squareNumbers, numbers)
print(squared)
print(list(squared))
