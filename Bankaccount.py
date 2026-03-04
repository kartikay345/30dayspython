Account = 'kartikay'
banking = True
balance = 0
transaction =[]# to store the history of the all the trsacstion done in history

user_detail = input('hey what would like to do today \n tell me your account name: ').strip().lower()
print('so your account name is ', user_detail)

if user_detail == Account:
    while banking:
        ask = int(input(
            'what would you like to do today \n'
            'press the following number \n'
            '1) to see the current balance of your account\n'
            '2) to withdraw some money\n'
            '3) to deposit some money\n'
            '4) exit\n'
            "5) view transaction"
        ))

        if ask == 1:# to check the current balance of the account 
            print('here your current balance:', balance)

        elif ask == 2:# if the user press 2 withdraw logic
            withdraw_question = float(input('how much money you would like to withdraw: '))

            if withdraw_question <= 0:
                print("Amount must be greater than 0.")
            elif balance >= withdraw_question:
                balance -= withdraw_question
                print('you have got your money now')
                print('here is your remaining balance:', balance)  
                transaction.append(f"Withdraw: -{withdraw_question} | Balance: {balance}")
            else:
                print("Insufficient balance.")

        elif ask == 3:# deposit logic 
            deposit_question = float(input('how much money would you like to deposit: '))

            if deposit_question <= 0:
                print('amount must be greater than 0')
            else:
                balance += deposit_question
                print('you deposited this much money:', deposit_question)
                print('here is your current balance:', balance)
                transaction.append(f" Deposit +{deposit_question} Balance:{balance} ") 

        elif ask == 4:# to break the loop
            banking = False
            print("Thanks for using the bank system. Bye!")

        elif ask ==5:    
            if not transaction: # if the trasaction is empty 
                print ('no transation yet')
            else :
                print(' here is your transaction history ')
                for i in transaction:
                    print (i)

        else:
            print("Please choose 1, 2, 3, 4, or 5.")

else:
    print('sorry either you dont have any account here ')