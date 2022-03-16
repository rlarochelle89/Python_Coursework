import time as t
import matplotlib.pyplot as plt



print ('This program helps the user type words faster.')

word = 'random'



while True:
    ready = input('Are you ready to practice? Type "yes" to begin. ').lower()
    if ready == 'yes':
        break
    else:
        print ('It seems like you are not yet ready.')
        continue


    
print ('The word is', '"'+word+'".', 'In ten seconds, type the word 5 times and press enter after each time. You will be timed.')
t.sleep(10)
print ('Ready in 5...')
t.sleep(1)
print ('4...')
t.sleep(1)
print ('3...')
t.sleep(1)
print ('2...')
t.sleep(1)
print ('1...')
t.sleep(1)

time_begin = t.time()
try0 = input('Go! First try: ')
time0 = t.time()
try1 = input('Second try: ')
time1 = t.time()
try2 = input('Third try: ')
time2 = t.time()
try3 = input('Fourth try: ')
time3 = t.time()
try4 = input('Final try: ')
time4 = t.time()


trials = [try0, try1, try2, try3, try4]
count = 0
round_number = 0

for trial in trials:
    index = 0
    for char in trial:
        if char == word[index]:
            index = index + 1
        else:
            index = index + 1
            count = count + 1

print('You made',count,'mistakes total when typing the word','"'+word+'".')


x = [1, 2, 3, 4, 5]
Times = [round(time0 - time_begin,2), round(time1 - time0,2), round(time2 - time1,2), round(time3 - time2,2), round(time4 - time3,2)]
legend = ['Round 1', 'Round 2', 'Round 3', 'Round 4', 'Round 5']
plt.plot(x, Times)
plt.xticks(x, legend)
plt.ylabel('# of Seconds')
plt.title('Time it took to type '+word)
plt.show()
