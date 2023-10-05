#!/usr/bin/env python3
# A program that decrypts what was encrypted by '5-encrypt.py'
encrypted = input("Paste the encrypted message that you wish to decrypt:\n:$ ")
shift = 7
decrypted = ""

for words in encrypted:
    if words.isalpha():
        code = ord(words)
        code -= shift
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
        decrypted += chr(code)
    elif words.isdigit():
        code = ord(words)
        code -= shift
        if code > ord('9'):
            code -= 10
        if code < ord('0'):
            code += 10
        decrypted += chr(code)
    else:
        decrypted += words
print("Message Decrypted!\n---\n", decrypted, end="\n---\n")
