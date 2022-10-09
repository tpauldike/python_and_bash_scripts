#!/usr/bin/python3
'''
  A program that converts messages written in text to
ASCII codes, thereby making it a secret message.
     Author: Topman Paul-Dike
'''
secret = input('Enter your message to hide it in codes below:\n')
letters = []

print('The secret message in codes is:')
for letter in secret:
    letters.append(ord(letter))
for code in letters:
    print(code, end=' ')
print()
