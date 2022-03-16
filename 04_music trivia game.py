import requests
import json
import random

print('This is a trivia game. Play as long as you want.')

input('When you are ready, press "enter".')

while True:

    r = requests.get('https://opentdb.com/api.php?amount=1&category=12&difficulty=easy&type=multiple')
    trivia = json.loads(r.text)

    question = trivia['results'][0]['question']
    correct_answer = trivia['results'][0]['correct_answer']
    answers = trivia['results'][0]['incorrect_answers']
    answers.insert(random.randint(0,2), correct_answer)

    print(question)
    print('Your choices are:')
    print(answers)
    guess = input('Your answer: ')

    if guess == correct_answer:
        print ('Good job! The correct answer was', '"'+correct_answer+'".')
    else:
        print ("I'm sorry. The correct answer was",'"'+correct_answer+'".')

    again = input('Do you want to play again? (Type "no" to quit) ').lower()
    if again == 'no':
        break

print ('This was fun, thanks for playing!')
print ('Ray, if you want to see the json library easier, use pprint.pprint(library)')
