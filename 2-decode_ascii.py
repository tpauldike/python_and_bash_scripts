#!/usr/bin/python3
'''
   A program that decodes messages written in ASCII codes and changes them
into readable characters
'''
secret = input('Paste the codes to be interpreted below:\n>>> ').split()
codes = []
readable = []

print('\nTHE MESSAGE HIDDEN IN THE CODES IS:')
for code in secret:
    codes.append(code)
for i in codes:
    readable.append(int(i))
for message in readable:
    print(chr(message), end='')
print('\n')
