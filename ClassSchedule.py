scheduling=True
my_schedule ={
                'Monday':[],
                'Tuesday':[],
                'Wednesday':[],
                'Thursday':[],
                'Friday':[],
                'Saturday':[],
                'Sunday':[],
}
while scheduling:
    user=input('what would you like to do today (A)dd class,(V)iew class,(Q)uit').capitalize().strip()
    if user=='A':
        adding_question=input('for what day would you like to add the schedule').capitalize().strip()
        if adding_question in my_schedule:
            classes = input('what subject would you like to add')
            my_schedule[adding_question].append(classes)
            print('succesfully added')
    elif user=='V':
        print('\n '+'='*10 +'YOUR WEEKLY SCHEDULE'+'='*10)
        for day ,classs in my_schedule.items():
            if not  classs:
                print('haha no classes today')
            else:
                print({day})
                for subject in classs:
                    print({subject})

    elif user =='Q':
        print('see you tomorrow ')
        scheduling=False
        
    else:
        print ('oops , you did a typo ')
