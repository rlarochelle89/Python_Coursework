#This is the number guessing game.
import random

print('Hi there! What is your name?')
name = input() #This requests the name from the user and stores it in a variable
print('Hello ' + name + ', I am thinking of a number between -10 and 10. Can you guess it?')

my_num = random.randint(-10,10)
attempt = 1

while attempt <= 6: #Now the game will loop until attempt = 6
    guess = input()
    try:
        if int(guess) > my_num and attempt < 6: #I need the and clause because for the last guess, something else happens.
            print('Nope, that guess is too high. Try again!')
            attempt = attempt + 1
        elif int(guess) < my_num and attempt < 6:
            print('Nope, that guess is too low. Try again!')
            attempt = attempt + 1
        elif int(guess) == my_num: #I don't need an and clause here because after 6 incorrect guesses we go to the else clause. 
            print('Exactly! My number was ' + str(my_num) + '. Nice job!')
            print('You guessed my number in ' + str(attempt) + ' attempts.')
            attempt = 7 #This ends the loop because now attempt is > 6
        else: #This only happens when the attempt = 6 and the guess is incorrect. 
            print('Not quite. The number I was thinking of was',my_num,'.')
    except:
        print('There was an error. Please use numerals when guessing your number. Numbers are integers between -10 and 10.')
        
