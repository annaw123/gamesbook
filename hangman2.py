import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''']

def getSecretWord():
    # This function returns a random string from the passed list of strings
    print('Hullo there! What is your secret word? ')
    while True:
        secretWord = input().lower()
        allOkay = True
        for i in range(len(secretWord)):
            if secretWord[i] not in 'abcdefghijklmnopqrstuvwxyz':
                print('No numbers or spaces allowed you sneaky badger')
                allOkay = False
                break
        if allOkay:
            for i in range(40):
                print()
            return secretWord

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters: ', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): #Replace blanks with correctly guessed letters.
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: #Show the secret word with spaces in between each letter.
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player enters a single letter and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter. ')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter you numpty')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('enter a LETTER  you banana :)')
        else:
            return guess

def playAgain():
    # This function returns true if the player wants to play again.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N  2')
missedLetters = ''
correctLetters = ''
secretWord = getSecretWord()
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    #LEt the player enter a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #Check the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('yes! the secret word is "' + secretWord + '"! you have won and I have lost!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        #Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses! You have lost and I have won! The correct word is ', secretWord)
            gameIsDone = True

    #Ask the player if they want to play again, but only if the game is done.
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = getSecretWord()
        else:
            print('byeee')
            break