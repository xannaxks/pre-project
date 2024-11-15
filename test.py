import os
import time

menu = [
    '1. List all tasks',
    '2. Add new task', 
    '3. Update existing task', 
    '4. Remove existing task', 
    '5. Exit'
] # Menu options

tasks = [] # List to store tasks

while True: # Loop to process options

    # Listing options and accepting users option
    print('-- TASK MANAGER --\n')
    for i in menu:
        print(i)
    x = int(input('\nPlease select the option: '))
    print('')

    # Error handling
    if (x < 1) or (x > 5):
        print('Invalid option')
        continue
    elif(x == 5):
        print('Quiting...')
        break

    # Printing already existing tasks
    print('Total amount of tasks:', len(tasks))
    for i in range(len(tasks)):
        print(i+1, '. ', tasks[i], sep='')
    print('')

    # Processing option, the user choose
    if(x == 2):
        newTask = str(input('Type ur task here: '))
        tasks.append(newTask)
        print('\nSuccesfully added')
    elif(x == 3):
        updateIdx = int(input('Type task number u want to update: '))
        updateText = str(input('Type the text to update: '))
        if (updateIdx < 1) or (updateIdx > len(tasks)):
            print('\nIndex of task out of range')
        else:
            tasks[updateIdx-1] = updateText
            print('\nSuccesfully updated')
    elif(x == 4):
        deleteIdx = int(input('Type task number u want to delete: '))
        if (deleteIdx < 1) or (deleteIdx > len(tasks)):
            print('\nIndex of task out of range')
        else:
            tasks.pop(deleteIdx-1)
            print('\nSuccesfully deleted')

    # Clearing the screen and repeating all this again
    os.system('pause')
    os.system('cls')




