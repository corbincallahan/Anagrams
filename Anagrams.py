from collections import Counter
from datetime import date
import random
import time

random.seed(str(date.today()))

def scramble(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

with open("Dictionary.txt", "r") as dictFile:
    words = [line.strip() for line in dictFile]

def wordsOfLen(num):
    return list(filter(lambda x: len(x) == num, words))

maxLength = 6
minLength = 3

maxLengthWords = list(filter(lambda x: len(x) == maxLength, words))
maxLengthWord = random.choice(maxLengthWords)
letters = scramble(maxLengthWord)
lettersCounter = Counter(letters)

def isAnagram(word):
    wordCounter = Counter(word)
    return [wordCounter[letter] <= lettersCounter[letter] for letter in wordCounter].count(False) == 0

validWords = dict()
for i in range(minLength, maxLength + 1):
    iLength = list(filter(isAnagram, wordsOfLen(i)))
    if(len(iLength) != 0):
        validWords[i] = iLength

lengthsGuessed = dict()
for length in validWords.keys():
    lengthsGuessed[length] = False

startTime = time.time()
checkMark = u'\u2713'
while(list(lengthsGuessed.values()).count(False) != 0):
    print(' '.join(letters))
    [print(f"{i} {checkMark if lengthsGuessed[i] else 'x'}    ", end="") for i in lengthsGuessed]
    print()
    guess = input("Guess a word: ")
    if(len(guess) in validWords.keys() and guess in validWords[len(guess)]):
        print(u'\u2713')
        lengthsGuessed[len(guess)] = True
    else:
        print('x')

print(f"Completed in {time.time() - startTime} seconds")