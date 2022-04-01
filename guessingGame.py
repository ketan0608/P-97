import random
chances=5
guess=input('Guess a number between 3 and 9\t')
number=random.randint(3,9)
if guess==number:
    print('Yaa you won')
elif chances>=1:
    print('Ohno! you lost.Try again.')
    chances=chances-1
    

