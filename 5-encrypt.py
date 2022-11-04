#!/usr/bin/env python3
# A program that encrypts a message ny shifting the characters 7 times
message = input("Enter the message you wish to encrypt:\n:$ ")
shift = 7
secret = ""

for words in message:
    if words.isalpha():
        code = ord(words)
        code += shift
        if words.isupper():
            if code > ord('Z'):
                code -= 26
            if code < ord('A'):
                code += 26
        else:
            if code > ord('z'):
                code -= 26
            if code < ord('a'):
                code += 26
        secret += chr(code)
    elif words.isdigit():
        code = ord(words)
        code += shift
        if code > ord('9'):
            code -= 10
        if code < ord('0'):
            code += 10
        secret += chr(code)
    else:
        secret += words
print("Message Encrypted!\n---\n", secret, end="\n---\n")
