import os # Importing necessary modules/packages

menu = [
    '1. List all tasks',
    '2. Add new task',
    '3. Update existing task',
    '4. Remove existing task',
    '5. Exit'
] # Menu options

tasks = [] # List to store tasks

while True: # Loop to process options

    os.system('cls') # Clears the screen

    # Listing options and accepting users optio
    print('----------------------')
    print('|                    |')
    print('|   TASK   MANAGER   |')
    print('|                    |')
    print('----------------------\n')

    # Printing menu
    for i in menu:
        print(i)

    # User inputs option
    x = int(input('\nPlease select the option: '))
    print('')
    print('----------------------\n')

    # Printing already existing tasks
    print('\nFollowing tasks already exist:\n')
    for i in range(len(tasks)):
        print(i+1, '. ', 'Title: ', tasks[i]['title'], '\n',
              i+1, '. ', 'Start time: ', tasks[i]['starting_time'], '\n', sep='')
    print('\n----------------------\n')

    # Error handling for invalid menu options
    if (x < 1) or (x > 5):
        print('Invalid option')
        continue

    # Exiting option
    if (x == 5):
        print('Quiting...')
        break

    # Processing option, the user choose
    if (x == 2 or x == 3): # Processing adding and updating task

        # Asking for index of updating task, if user choose 3
        idx = -1
        if(x == 3):
            idx = int(input('\nPlease enter the index of task, u want to update: '))
            if (idx < 1) or (idx > len(tasks)):
                print('Invalid index')
                continue
            idx -= 1

        # Values for new tasks or updating task
        title = str(input('\nPlease enter the title of the task: '))
        startHour = int(input('Please enter the starting hour of the task: '))
        startMinute = int(input('Please enter the starting minute of the task: '))

        # Validating time format
        if (startHour > 23 or startHour < 0 or startMinute < 0 or startMinute > 59 ):
            print('\nInvalid Time')
            os.system("pause")
            continue

        # Storing new task / updated task, using dictionary
        newTask = {
            'title' : title,
            'starting_time' : str(str(startHour) + ': ' + str(startMinute)),
            'start_hour' : startHour,
            'start_minute' : startMinute,
        }

        # If user choose updating, removing old version of task
        if idx != -1:
            tasks.pop(idx)

        # Adding new task
        tasks.append(newTask)

        # Printing Message
        if (x == 2):
            print('\nSuccessfully added new task')
        else:
            print('\nTask was successfully updated')

    if (x == 4): # If user choose delete option
        # Asking for index
        deleteIdx = int(input('\nType task number u want to delete: '))

        # Invalid index error handling
        if (deleteIdx < 1) or (deleteIdx > len(tasks)):
            print('\nIndex of task out of range')
        else:
            # Performing delete, if index provided by user is correct
            tasks.pop(deleteIdx-1)
            print('\nSuccessfully deleted')

    os.system('pause') # Waits for user to press any button