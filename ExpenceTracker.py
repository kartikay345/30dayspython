all_expenses=[]
user_question=float(input('what is starting budget'))
going_on=True
while going_on:
    user_item=input('what was the name of the item').capitalize().strip()
    price_amount=float(input('what was the price of the item you bought'))
    category_of_the_item=input('what was the category of the item').capitalize().strip()
    
    current_entry={
            'Item': user_item,
        'Amount': price_amount,
        'Category': category_of_the_item
    
    }
    all_expenses.append(current_entry)
    totalspend=0# for the total of the money spend
    for x in all_expenses:
        totalspend +=x['Amount']
        
    print(f"here is your total spend money  {totalspend}")

    remaining_value =user_question-totalspend # for the remaining value 
    print('here is your monthy budget money left ',remaining_value)
    # logic if the user went out of budget 
    if totalspend>user_question:
        print('warning , ahhhhhh this month is going to be hard for you take care bro ')
    else:
        print('no worries bro , you are still safe')
    # if the user want to exit the loop 
    choice= input('would you like to add another expence (y/n)').lower().strip()
    if choice=='y':
        print('='*10+'Thats my boy' +'='*10 )
    elif choice =='n':
        print('hope to see you next time ')
        going_on=False


category_summary = {}

for expense in all_expenses:
    cat = expense['Category']
    amt = expense['Amount']
    
    if cat in category_summary:
        category_summary[cat] += amt # Add to the existing total
    else:
        category_summary[cat] = amt  # Create the drawer and put the first amount in

print("\n" + "="*10 + " FINAL CATEGORY REPORT " + "="*10)
for category, total in category_summary.items():
    print(f"{category}: ${total:.2f}")  
print("="*44)        

