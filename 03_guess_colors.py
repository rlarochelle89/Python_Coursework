import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'brown', 'black', 'white', 'silver', 'gold', 'gray']

while True: 

    win_color = colors[random.randint(0,len(colors)-1)]
    guess_color = input("I'm thinking of a color. Can you guess it: ").lower()

    while True:
        if guess_color == win_color:
            break
        else:
            guess_color = input('Nope. Try again: ').lower()

    print('Good job! The color was', win_color+'.')

    again = input('Do you want to play again? (Type "no" to quit) ').lower()

    if again == 'no':
        break

print('This was fun, thanks for playing!')
