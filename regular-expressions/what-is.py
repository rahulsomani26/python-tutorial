import re

'''regular expressions  re '''


''' Convention method '''


# myNumber = 'rahul210638822somani'
# numberFromString = myNumber.find('8210638822')
# if numberFromString < len(myNumber):
#     print(f' Found 8210638822 at position {numberFromString}')
# else:
#     print(' Not found')


''' using regular expressions '''


# myNumber = 'rahul8210638822somani'
# numberFromString = re.search('8210638822', myNumber)
# print(numberFromString)
# if numberFromString:
#     print(' Found a match')
# else:
#     print(' No match found ')


'''
no such great use. Isnt't it 
so,what is so great in regular expressions.
well, The real power of regex matching in Python emerges when <regex> contains 
special characters called metacharacters. These have a unique meaning to the regex
matching engine and vastly enhance the capability of the search.

Consider again the problem of how to determine whether a string contains any three 
consecutive decimal digit characters.

In a regex, a set of characters specified in square brackets ([]) makes up a 
character class. This metacharacter sequence matches any single character that is in the
class, as demonstrated in the following example:
'''


# aString = 'what1234is'
# pattern = '[0-9]'
# match = re.search(pattern, aString)
# print(match)

# print(re.search('[0-9][0-9][0-9][0-9]', aString))

# myNumber = 'xhello8210638822and78why89not?'
# pattern = '[0-9]+'
# match = re.search(pattern, myNumber)
# print(match)

# myvalue = '\nthis'
# pattern = r'.'
# match = re.search(pattern, myvalue)
# print(match)

'''
 metacharacter 
 The dot (.) metacharacter matches any character except a newline, so it functions like a wildcard:
'''


'''

Metacharacharacter * 
matches zero or more repetitions
'''

# myValue = 'This is the life of a spy and one of is a miracle'
# ''' Find how many times 'of' repeats'''
# pattern = 'of*'
# match = re.search(pattern, myValue)
# print(match)


'''

Metacharacharacter []
 Characters contained in square brackets ([]) represent a character class—an enumerated set
 of characters to match from.
 A character class metacharacter sequence will match any single character contained in the class.
'''
# myDogName = 'arrowThebow'
# pattern = 'arrow..[ebX]'
# match = re.search(pattern, myDogName)
# print(match)

'''
A character class can also contain a range of characters separated by a hyphen (-),
in which case it matches any single character within the range. 
For example, [a-z] matches any lowercase alphabetic character between 'a' and 'z', inclusive:
'''


myName = 'rahulsomani'
myMail = 'somani.classes@outlook.com'
myNumber = '+918210638822'

# pattern1 = r'[a-z]*'
# print(re.search(pattern1, myName))

# pattern2 = r'8.1[0-9]+'
# print(re.search(pattern2, myNumber))

# myUpperName = 'RAHULsOMANI'
# pattern = '[a-z].'
# print(re.search(pattern, myUpperName))


# password = 'ThisisLife@123'
# pattern = '[a-z]@[0-9][0-9][0-9]'
# pattern = '[a-z]@[0-9]+'
# pattern = '[a-z]@[0-9]*'
# pattern = '[a-z]@[0-9]..'


# result = re.search(pattern, password)
# print(result)


'''
You can complement a character class by specifying ^ as the first character,
in which case it matches any character that isn’t in the set. 
In the following example, [^0-9] matches any character that isn’t a digit:
'''
# print(re.search('[^0-9]', 'rahul1234'))
# print(re.search('[^0-9]+', 'rahul1234'))
# print(re.search('[^0-9]*', 'rahul1234'))
# print(re.search('[^0-9].', 'rahul1234'))


# print(re.search('[:^]', 'rahu^sima%^'))
# print(re.search(r'\^', 'rahu^sima%^'))


'''
 
Match based on whether a character is a word character.

\w matches any alphanumeric word character.
Word characters are uppercase and lowercase letters, digits,
and the underscore (_) character, so \w is essentially shorthand for [a-zA-Z0-9_]:
'''

print(re.search('\w', 'Rahul_somani_123'))
# print(re.search('[a-zA-Z0-9_]', 'Rahul_somani_123'))
