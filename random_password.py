import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?'

length = input('Enter the password length:')
length = int(length)

count = input('Enter the number of password:')
count = int(count)

for p in range(count):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
