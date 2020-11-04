

# print(users)
# del users[0]
# # print(users)

# for user in users:
#     if user[1] == 'This':
#         print(user)
#         print('End')
#         break
#     else:
#         pass

'''
   Dictionary Comprehension
   
# '''


users = [
    (0, 'Me', "mypassword"),
    (1, 'You', "yourpassword"),
    (2, 'This', "thispassword"),
    (3, 'There', "therepassword"),

]
newUser = {user[1]: user for user in users if user[1] == 'Me'}
print(newUser)

print(newUser.keys())
print(newUser.items())
