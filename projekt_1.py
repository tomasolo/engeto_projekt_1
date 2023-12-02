'''
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Tomas Musil
email: musil.tomas@gmail.com
discord: musil.tomas
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# separator for console output
separator = 40 * '-'

# registered users and passwords
users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

# get username and password
username = input('username: ').lower()
password = input('password: ')

# check if registered username
if username in users and password == users[username]:
    print(separator)
    print(f'Welcome to the app, {username}')
    print(f'We have {len(TEXTS)} texts to be analyzed.')
    print(separator)
    text_num = input('Enter a number btw. 1 and 3 to select: ')

    # testing validity of input
    if text_num.isdecimal() and int(text_num) in range(1, len(TEXTS) + 1):
        text_num = int(text_num)
    else:
        print('invalid input, terminating the program..')
        quit()
else:
    print('unregistered user, terminating the program..')
    quit()

# text split and cleaning of words
words_raw = TEXTS[text_num - 1].split()
words = []

for word in words_raw:
    words.append(word.strip(".,:;"))

# text analysis
words_count = len(words)
counter_istitle = 0
counter_isupper = 0
counter_islower = 0
counter_isdecimal = 0
sum = 0
word_occ = {}

for word in words:
    # summary of words
    if word.istitle():
        counter_istitle += 1
    elif word.isupper():
        counter_isupper += 1
    elif word.islower():
        counter_islower += 1
    elif word.isdecimal():
        counter_isdecimal += 1
        sum += int(word)
        
    # occurrence of words
    word_len = len(word)
    if word_len not in word_occ:
        word_occ[word_len] = 1
    else:
        word_occ[word_len] += 1

# print summary
print(separator)
print(f'There are {words_count} words in the selected text.')
print(f'There are {counter_istitle} titlecase words.')
print(f'There are {counter_isupper} uppercase words.')
print(f'There are {counter_islower} lowercase words.')
print(f'There are {counter_isdecimal} numeric strings.')
print(f'The sum of all the numbers {sum}')
print(separator)

# print occurence summary
colums = [3, 32] # -> number of column characters: LEN | OCCURENCES | NR.
print(f'{'LEN'.rjust(colums[0])}|{'OCCURENCES'.center(colums[1])}|NR.')
print(separator)

for char_count in sorted(word_occ.keys()):
    stars = '*' * word_occ[char_count]
    print(f'''{str(char_count).rjust(colums[0])}|{
        str(stars).ljust(colums[1])}|{word_occ[char_count]}''')