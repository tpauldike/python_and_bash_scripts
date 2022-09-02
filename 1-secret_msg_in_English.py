#!/usr/bin/python3
'''
  A program that converts messages written in text to
ASCII codes, thereby making it a secret message.
     Author: Topman Paul-Dike
'''
uppercase = input('Enter your message (alphbets only) to hide it in codes,\n'
                  'please separate each word with double spaces:\n$: ')
uppercase = uppercase.upper()

print('The secret message is:')
for i in range(0, len(uppercase), 1):
    secret = ord(uppercase[i])
    if (uppercase[i] >= 'A') and (uppercase[i] <= 'Z'):
        print(secret, end = "")
    else:
        print('{}'.format(uppercase[i]), end = "")
print()
