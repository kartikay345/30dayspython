future_accounts = {}   # stores all users
main_running = True

while main_running:
    user = int(input(
        "heya hows your day going so far \n"
        "what would like to do today \n"
        "1) create account\n"
        "2) log in\n"
        "3) exit\n"
        "Enter: "
    ))

    # ---------- CREATE ACCOUNT ----------
    if user == 1:
        user_question = input("by what name would you like to create an account: ").strip().lower()

        if user_question in future_accounts:
            print("already exists")
        else:
            future_accounts[user_question] = {"balance": 0.0, "transactions": []}
            print("account successfully created:", user_question)

    # ---------- LOG IN ----------
    elif user == 2:
        login_name = input("enter your account name to log in: ").strip().lower()

        if login_name not in future_accounts:
            print("sorry, no account found with that name. please create one first.")
        else:
            banking = True
            current_user = login_name

            while banking:
                ask = int(input(
                    "\nwhat would you like to do today \n"
                    "press the following number \n"
                    "1) see current balance\n"
                    "2) withdraw money\n"
                    "3) deposit money\n"
                    "4) view transactions\n"
                    "5) logout\n"
                    "Enter: "
                ))

                
                balance = future_accounts[current_user]["balance"]
                transactions = future_accounts[current_user]["transactions"]

                if ask == 1:
                    print("here is your current balance:", balance)

                elif ask == 2:
                    withdraw_question = float(input("how much money would you like to withdraw: "))

                    if withdraw_question <= 0:
                        print("Amount must be greater than 0.")
                    elif balance >= withdraw_question:
                        balance -= withdraw_question
                        transactions.append(f"Withdraw: -{withdraw_question} | Balance: {balance}")
                        print("you have got your money now")
                        print("here is your remaining balance:", balance)
                    else:
                        print("Insufficient balance.")

                elif ask == 3:
                    deposit_question = float(input("how much money would you like to deposit: "))

                    if deposit_question <= 0:
                        print("amount must be greater than 0")
                    else:
                        balance += deposit_question
                        transactions.append(f"Deposit: +{deposit_question} | Balance: {balance}")
                        print("you deposited this much money:", deposit_question)
                        print("here is your current balance:", balance)

                elif ask == 4:
                    if not transactions:
                        print("no transaction yet")
                    else:
                        print("here is your transaction history:")
                        for t in transactions:
                            print(t)

                elif ask == 5:
                    banking = False
                    print("logged out.")

                else:
                    print("Please choose 1, 2, 3, 4, or 5.")

                # save updated values back to this user
                future_accounts[current_user]["balance"] = balance
                future_accounts[current_user]["transactions"] = transactions

    # ---------- EXIT ----------
    elif user == 3:
        main_running = False
        print("thank you for giving us your time")

    else:
        print("Please choose 1, 2, or 3.")