import random

secret = random.randint(1, 100)
attempts = 0
guessing = True

while guessing:
    ask = input('try to guess the number ').strip()

    if ask.isdigit():
        ask = int(ask)

        if ask == secret:
            print('you are such a genius for that')
            guessing = False

        elif ask > secret:
            print('too high')
            continue

        elif ask < secret:
            print('too low')
            continue
    else:
        print('numbers only')