#!/usr/bin/python3
'''
   A program that converts a message written in ASCII codes to letters
when the codes are pasted as the input. This works excellently for
uppercases written with double spaces between each single word.
'''
secret = input('Paste the codes to be interpreted below:\n:# ')

for i in range(0, len(secret)-1, 2):
    if (secret[i] == ' '):
        print(' ', end = "")
        continue
    message = (secret[i] + secret[i+1])
    convert = int(message)
    decoded = chr(convert)
    print(str(decoded), end = "")

print()
