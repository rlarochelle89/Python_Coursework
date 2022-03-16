#This is the number guessing game.
import random

print('Hi there! What is your name?')
name = input() #This requests the name from the user and stores it in a variable
print('Hello ' + name + ', I am thinking of a number between -10 and 10. Can you guess it?')

my_num = random.randint(-10,10)

for attempt in range(1,7):
    guess = input()
    try:
        if int(guess) == my_num:
            print ('Great job! You are right, my number was', str(my_num) + '.') #make sure the str() is there to change int to string
            break
        elif int(guess) > my_num and attempt < 6: #still need the and clause because on the last attempt, a wrong answer should go to else
            print ('Nope, that guess is too high. Try again!')
        elif int(guess) < my_num and attempt < 6:
            print ('Nope, that guess is too low. Try again!')
        else:
            print ('Nope, sorry.')
    except:
        print('Invalid input. Make sure you type numerals instead of letters.')
if guess == my_num:
    print ('You guessed my number in', str(attempt), 'attempts.')
elif guess != my_num:
    print ('My number was actually', str(my_num) + '.')
