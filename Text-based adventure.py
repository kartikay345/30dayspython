player = True
print('welcome to the game world today is your day ')
print('so today we are going to explore the forest')

while player:
    start = input('would like to go through the land or by river: ').strip().lower()

    if start == 'river':
        print('haha, you have to swim for 2 hour')
    elif start == 'land':
        print('lets go straight and try to find something useful for the night')
    else:
        print('answer what is asked')
        continue  # go back to the start question again

    choice = input('okay you found the temple, would you like to go there by front gate or by back gate? ').strip().lower()

    if choice == 'front':
        print("The front gate is trapped... Game Over!")
        player = False
    elif choice == 'back':
        print("You sneaked in safely... You win!")
        player = False
    else:
        print("Type only: front or back")

