import random

secret = random.randint(1, 100)
attempts = 0
guessing = True
print (secret)

while guessing:
    ask=int(input('try your bestto guess the number'))
    if ask ==secret:
        print ('well done you got it genuis')
    elif ask> secret:
        print ('too high try agian ')    
    elif ask<secret:
        print('too low ')
    else :
        print('numbers only')        