to_do_list = [] # Stage 1 of the file , now we are going for level 2 where we gonna make proffesional 
listing = True

while listing:
    ask = input("Do you want to (A)dd a task, (V)iew tasks,(R)emove tasks or (Q)uit? ").capitalize().strip()
    
    if ask == 'A':
        new_task = input("What task would you like to add? ")
        to_do_list.append(new_task)
        print(f"Added: {new_task}")

    elif ask == 'V':
        print('\n' + '='*10 + " TO-DO LIST " + '='*10)
        for i in to_do_list:
            print(i)
    elif ask == 'Q':
        print("Closing program... Stay productive!")
        listing = False 
    elif ask =='R':
        print('='*30,'To-DO-list','='*30)  
        ask2=input('which task would you like to remove ')  
        if ask2 in to_do_list :
            to_do_list.remove(ask2)
        else:
            print('oops seems like this is not in your list ')    