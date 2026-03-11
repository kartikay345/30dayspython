grocery_list=[]# empty list for the grocery things to add
shopping =True

while shopping :
    already_in_=False
    total_number=0
    name=input('what thing whould you like to buy today (stage3)\n')# for the thing we want to buy 
    qtt=int(input('how many of them would you like to buy' ))# how many of them they need 
    haha= {'item':name,'quantity':qtt} # for the list 
    
    
    for i in grocery_list:  # to icrease the number if already exists
        if i['item']==name:
            i['quantity']+=qtt
            already_in_=True
            break
    

    
    if already_in_==False:# if no append
        grocery_list.append(haha)

    print('='*10,'here your list','='*10)
    print(f"{'ITEM':<15} | {'QUANTITY':<10}") 
    print("-" * 30)
    for thing in grocery_list:
        print(f"{thing['item']:<15} | {thing['quantity']:<10}")
        
    for j in grocery_list:# for the total number of items in the cart
        total_number += j['quantity']    

    print(f"these are the total number of things in your cart \n {total_number}" )    