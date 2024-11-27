import os

def print_starting():
    print('----------------------')
    print('|                    |')
    print('|   TASK   MANAGER   |')
    print('|                    |')
    print('----------------------\n')

menu = [
    '1. List all tasks',
    '2. Add new task',
    '3. Update existing task',
    '4. Remove existing task',
    '5. Exit'
]

def print_menu():
    for i in menu:
        print(i)

tasks = [] 

def print_existing_tasks():
    print('\nFollowing tasks already exist:\n')
    for i in range(len(tasks)):
        key = next(iter(tasks[i].keys()))
        print(i + 1, '. ', key, '\n', i + 1, '. ', tasks[i][key], '\n', sep='')
    print('\n----------------------\n')

def check_time(startHour, startMinute):
    if (startHour > 23 or startHour < 0 or startMinute < 0 or startMinute > 59 ):
        print('\nInvalid Time')
        os.system("pause")
        return False
    return True

def format_time(startHour, startMinute):
    if startHour < 10:
        startHour = '0' + str(startHour)
    else:
        startHour = str(startHour)
    if startMinute < 10:
        startMinute = '0' + str(startMinute)
    else:
        startMinute = str(startMinute)
    return startHour + ':' + startMinute

while True:

    os.system('cls') 
    
    print_starting()
    print_menu()

    x = int(input('\nPlease select the option: '))
    print('')
    print('----------------------\n')

    print_existing_tasks()

    if (x < 1) or (x > 5):
        print('Invalid option')
        continue

    if (x == 5):
        print('Quiting...')
        break

    if (x == 2 or x == 3): 

        isDelete = None
        if (x == 3):
            isDelete = int(input('\nPlease enter the id of task, u want to update: '))
            if (isDelete < 1) or (isDelete > len(tasks)):
                print('\nInvalid index')
                os.system('pause')
                continue

        title = str(input('\nPlease enter the title of the task: '))
        startHour = int(input('Please enter the starting hour of the task: '))
        startMinute = int(input('Please enter the starting minute of the task: '))

        if not check_time(startHour, startMinute):
            continue
        
        startTime = format_time(startHour, startMinute)
        newTask = {
            title: startTime
        }
        if isDelete != None:
            tasks.pop(isDelete - 1)
        tasks.append(newTask)
        if x == 3:
            print('\nSuccesfully updated')
        else:
            print('\nSuccessfully added new task')

    if (x == 4): 
        deleteIdx = int(input('\nType task number u want to delete: '))

        if (deleteIdx < 1) or (deleteIdx > len(tasks)):
            print('\nIndex of task out of range')
        else:
            tasks.pop(deleteIdx-1)
            print('\nSuccessfully deleted')

    os.system('pause')