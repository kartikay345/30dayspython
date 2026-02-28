import random
playing =True
print('welcome to the truth and dare game')
truth = ['are you virgin ','what is your body coutn ', 'how many relationship have you been ', 'what is your favourite postiion ']
dare=['go home','call your mom and say you are drunk ',' call your parents and let them know about you relationship']
while playing:
    ask=input ('what will you choose truth or dare').strip().lower()
    chosese=random.choice('truth','dare')
    