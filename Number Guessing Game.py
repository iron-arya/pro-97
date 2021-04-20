print("Number Guessing Game")

#importing randit from random
from random import randint
guessesTaken = 0
print("What's your Name?")
myName=input()
#Telling the computer to pick a number between 1 and 15
number=randint(1,15)
print("Hello!,", myName,",I am thinking a number between 1 and 15")
print("You have only 8 chances to predict ME")
while guessesTaken < 8:
    print("Guess the number which I tought")
    guess = int(input())
    guessesTaken = guessesTaken + 1

#creating condition for checking whether the guessed number too high or too low
    if guess > number :
        print("Your guess was too high: Guess a number lesser than ",guess) 
    if guess < number :
        print("Your guess was too low: Guess a number higher than ",guess)
    if guess == number :
        break

if guess == number:
  guessesTaken = str(guessesTaken)
  print('Good job,' + myName + '! You guessed the correct number in '+ guessesTaken +' guesses!')


if guess != number:
  number = str(number)
  print('Sorry...You ran out of 8 guesses!')
  print("Please try again Later")