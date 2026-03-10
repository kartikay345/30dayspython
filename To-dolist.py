to_do_list = [] # Stage 1 of the file , now we are going for level 2 where we gonna make proffesional 

# now we are going to use enumerate 
#
listing = True

while listing:
    ask = input("Do you want to (A)dd a task, (V)iew tasks,(R)emove tasks or (Q)uit? new ").capitalize().strip()
    
    if ask == 'A':
        new_task = input("What task would you like to add? ")
        to_do_list.append(new_task)
        print(f"Added: {new_task}")

    elif ask == 'V':
        print('='*30,'to-do-list', '='*30)
        for index,task in enumerate(to_do_list,start=1):
            print(f"{index}.{task}")
    elif ask == 'Q':
        print("Closing program... Stay productive!")
        listing = False 
    elif ask =='R':
        print('='*10,'To-DO-list','='*10)  
        for index,task in enumerate(to_do_list,start=1):
            print(f"{index}.{task}")
        ask2=int(input('which task would you like to remove '))  
        removed_item = to_do_list.pop(ask2 - 1)
        
        print(f"Successfully removed: {removed_item}")  