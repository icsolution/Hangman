import random

print('H A N G M A N')

play = True
while play:
    start = input('Type "play" to play the game, "exit" to quit: ')
    if start == 'play':
        play = False


words = ['python', 'java', 'kotlin', 'javascript']
answer = 'java' # random.choice(words)

hint = len(answer) * '-'
lives = 8
tried = ''

while lives > 0 and hint != answer:
    guess = input(f'\n{hint}\nInput a letter: ')
    if len(guess) != 1:
        print('You should input a single letter')
    elif guess.isupper() or not guess.isalpha():
        print('Please enter a lowercase English letter')
    elif guess in answer and guess not in tried:
        for index, letter in enumerate(answer):
            if letter == guess:
                hint = list(hint)
                hint[index] = letter
                hint = ''.join(hint)
                tried += guess
    elif guess in tried:
        print("You've already guessed this letter")
    else:
        print("That letter doesn't appear in the word")
        lives -= 1
        tried += guess

if lives > 0 and hint == answer:
    print(f'You guessed the word {hint}!\nYou survived!')
else:
    print('You lost!')
