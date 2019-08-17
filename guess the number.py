import random

guessesTaken = 0
print('Hello, What is your name?')
name = input()

number = random.randint(1, 20)
print("Well, %s, I am thinking of a number between 1 and 20" % name)

for guessesTaken in range(6):
    print('Take a guess')
    guess = int(input())

    if guess < number:
        print('Too low ma friend')

    if guess > number:
        print('Too high ma friend')

    if guess == number:
        guessesTaken = guessesTaken + 1
        print("Good job, %s, you guessed my number in %s guesses!" % (name, guessesTaken))
        exit()

print("%s, you've had too many guesses. The correct number was %s" % (name, number))