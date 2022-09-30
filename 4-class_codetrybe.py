#!/usr/bin/python3

class Codetrybe:
    '''
Trying to play around to see how well I can manipulate objects in python.
This class holds some information about some members of CodeTrybe
    '''

# The constructor
    def __init__(self, name, sex, cohort, team):
        self.name = name
        self.sex = sex
        self.cohort = cohort
        self.team = team

# Information meant for fellow developers
    def __repr__(self):
        return f"{self.name} ({self.sex}) from cohort {self.cohort} is in the {self.team} Team"

# What the end user is going to see
    def __str__(self):
        return f"{self.name}\t-- {self.team} Team"

    def add_topics(self):
        '''
        A method that enables the registration of PLD topics
        '''
        topics = []
        enter_topic = input("Enter a new PLD topic or enter 'q' to quit: ")
        next_topic = ""
        topics.append(enter_topic)
        while next_topic != 'q':
            next_topic = input("Enter the next topic or 'q' to quit: ")
            topics.append(next_topic)
        if next_topic == 'q':
            topics.pop()
        print('\nYou have successfully registered the following topic(s):')
        for topic in topics:
            print(f'{topics.index(topic)+1}', end=". ")
            print(topic)
        print()
        return topics




Judyn = Codetrybe('Judyn', 'M', '9', 'Junior')
Hadiza = Codetrybe('Hadiza', 'F', '8', 'Senior')
Deborah = Codetrybe('Deborah', 'F', '8', 'Senior')
Faruq = Codetrybe('Faruq', 'M', '9', 'Junior')
Faruq.email = 'faruq@mail.com'
Anwulika = Codetrybe('Anwulika', 'F', '9', 'Junior')
Abiodun = Codetrybe('Abiodun', 'M', '8', 'Senior')

print(Judyn)
print(Hadiza)
print(Deborah)
print(f'{Faruq} ({Faruq.email})')

print(Codetrybe.__repr__(Anwulika))
print(Abiodun.__repr__())
print()

Abiodun.pld = Abiodun.add_topics()

print(f'Mr. Abiodun will take', end=" ")
last_topic = Abiodun.pld[-1]
Abiodun.pld.pop()

if len(Abiodun.pld) == 0:
    print(last_topic + ' only.')
elif len(Abiodun.pld) == 1:
    print(f'{Abiodun.pld[0]} and {last_topic}')
else:
    for topic in Abiodun.pld:
        print(topic, end=", ")
    print('and {}'.format(last_topic), end=".")
print()
