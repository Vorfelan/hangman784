import random

# TASK 1
word_list = ['banana','apple','bluberry','watermelon','kiwi']
print(word_list)

# TASK 2
word = random.choice(word_list)
print(word)

# TASK 3
guess = input('Please choose a letter: ')

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print("Oops! That is not a valid input.")

