# Python and I
A repository that I created to save the earliest codes or programs that I wrote while learning how to program in python

The following is a brief description of the programs. The [README file](../bash_scripts/README.md) of the **bash_scripts** directory contains a simple instruction on how to run any of these programs as scripts on your locale, *in case you find them useful and wish to use any*.

## 0. Slicing python strings
In this program I was practicing how to slice strings in python, you will understand better if you take a look at the content of the file [0-pld.py](./0-pld.py). I actually wrote it while taking a PLD session, hence the name given to the file.

## 1. Make the message ASCII
The python script prints a prompt, receives a message (as texts) inputed by the user, and prints the same message as ASCII values, thereby making it a secrete or hidden message

## 2. Decode the secret message
The script reverses what is done by the script previously described above; it changes the ASCII values back to the text that was initially converted to ASCII

## 3. Register customer
A program that, I believe, could be very much better and simpler than this; it allows the user to register new customers and outputs the names of all the newly registered customer as an ordered list

## 4. OOP -- Resgister PLD topics
As a beginner, I was at this point just trying to learn by practice, Object Oriented Programming in python.

I learned how to:
- create a class
- use some magic methods
- create instances
- define some functions ***and so on***

## 5. Encrypt a message
This program encrypts the string passed to it by moving all alphabets and numbers seven times from its relative position (e.g; **a** will be **h** and **0** will be **7**)

The program does not move any character that is neither an uppercase alphabet (A...Z) or a lowercase alphabet (a...z) or a digit (0...9) because appropriate checks are placed. The program also performs the shift within a defined range. For example, it will not replace an uppercase with a lowercase alphabet.

Thanks to **Derek Banas**; he thought me and I owned the code

## 6. Decrypt the message
This program reverses the action of [5-encrypted.py](./5-encrypted.py) described above
