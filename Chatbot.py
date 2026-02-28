chatting =True
while chatting:
    print('welcome i hope your day been so far , how can i help ')
    hello = input('ask me any question ').strip().lower()
    if hello=='greeting':
        print('hello man , how are you ')
    elif hello=='name':
        print('my name is chatbot what is your name ')
    elif hello =='help menu ':
        print('question you  can ask to chatbot /n you can ask name /n you can ask mood / and bla bal shit ')
    elif hello=='mood ':
        print ('im in a good mood wht avout you ')
    elif hello=='joke':
        print('hahahahhahahh')   
    elif hello =='bye':
        break    
    else:
        print("cholo aaj k liye bahot h"  )               
