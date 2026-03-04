Account = 'kartikay'
banking = True
balance = 0

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
        ))

        if ask == 1:
            print('here your current balance:', balance)

        elif ask == 2:
            withdraw_question = float(input('how much money you would like to withdraw: '))

            if withdraw_question <= 0:
                print("Amount must be greater than 0.")
            elif balance >= withdraw_question:
                balance -= withdraw_question
                print('you have got your money now')
                print('here is your remaining balance:', balance)
            else:
                print("Insufficient balance.")

        elif ask == 3:
            deposit_question = float(input('how much money would you like to deposit: '))

            if deposit_question <= 0:
                print('amount must be greater than 0')
            else:
                balance += deposit_question
                print('you deposited this much money:', deposit_question)
                print('here is your current balance:', balance)

        elif ask == 4:
            banking = False
            print("Thanks for using the bank system. Bye!")

        else:
            print("Please choose 1, 2, 3, or 4.")

else:
    print('sorry either you dont have any account here ')