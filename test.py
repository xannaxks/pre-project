import os # Importing necessary modules/packages

menu = [
    '1. List all tasks',
    '2. Add new task',
    '3. Update existing task',
    '4. Remove existing task',
    '5. Exit'
] # Menu options

tasks = [] # List to store tasks
totalOperations = 0 # Variable to count total amount of operations

while True: # Loop to process options

    # Adding one to total amount of operations
    if totalOperations > 0: # If there is something outputted on screen already, then we need to clean
        os.system('pause') # Waits for user to press any button
        os.system('cls') # Clears the screen
    totalOperations += 1

    # Listing options and accepting users option
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
              i+1, '. ', 'Description: ', tasks[i]['description'], '\n',
              i+1, '. ', 'Start time: ', tasks[i]['starting_time'], '\n',
              i+1, '. ', 'Ending time: ', tasks[i]['ending_time'], '\n',
              i+1, '. ', 'Total duration: ', tasks[i]['duration'], '\n', sep='')
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
        description = str(input('Please enter the description of the task: '))
        startHour = int(input('Please enter the starting hour of the task: '))
        startMinute = int(input('Please enter the starting minute of the task: '))
        endHour = int(input('Please enter the ending hour of the task: '))
        endMinute = int(input('Please enter the ending minute of the task: '))

        # Validating time format
        if (startHour > 23 or startHour < 0 or startMinute < 0 or startMinute > 59 or endHour > 23 or endHour < 0 or endMinute > 59 or endMinute < 0):
            print('\nInvalid Time')
            continue
        if (endHour < startHour) or (endHour == startHour and endMinute < startMinute):
            print('\nTask can not end before starting')
            continue

        # Calculating total duration
        duration = endHour * 60 + endMinute - startHour * 60 - startMinute

        # Storing new task / updated task, using dictionary
        newTask = {
            'title' : title,
            'description' : description,
            'starting_time' : str(str(startHour) + ': ' + str(startMinute)),
            'ending_time' : str(str(endHour) + ': ' + str(endMinute)),
            'duration' : str(duration//60) + ' hour(s) and ' + str(duration%60) + ' minute(s)',
            'start_hour' : startHour,
            'start_minute' : startMinute,
            'end_hour' : endHour,
            'end_minute' : endMinute
        }

        # If user choose updating, removing old version of task
        if idx != -1:
            tasks.pop(idx)

        # Finding the place of the task, to make list ordered by staring time
        isAdded = False
        for i in range(len(tasks)-1, -1, -1):
            if (newTask['start_hour'] < tasks[i]['start_hour']) or (newTask['start_hour'] == tasks[i]['start_hour'] and newTask['start_minute'] <= tasks[i]['start_minute']):
                tasks.insert(i, newTask)
                isAdded = True
                break
        if not isAdded:
            if len(tasks) == 0 or (tasks[len(tasks)-1]['start_hour'] < newTask['start_hour']) or (tasks[len(tasks)-1]['start_hour'] == newTask['start_hour'] and tasks[len(tasks)-1]['start_minute'] <= newTask['start_minute']):
                tasks.append(newTask)
            else:
                tasks.insert(0, newTask)

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




