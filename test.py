import random

table = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] # gaming table

isFinished = False # whether game finished or not
Turn = True # indicator of turn

for _ in range(1000): # iterations
    if not isFinished: # if game still not finished
        if Turn: # if its user's turn

            # printing game table
            for i in range(0, len(table)):
                if i % 3 == 0 and i != 0:
                    print('') #
                print(table[i], end = ' ')
            print('')

        if Turn: # if its user's turn
            x = int(input('Enter number of cell: ')) # asking to input cell number
            x -= 1 # subtracting one, cuz of zero indexing
            if x < 0 or x > 8: # checking whether cell number between allowed range
                print('Cell number out of range') # print error
            elif table[x] == 'X' or table[x] == 'O': # checking whether cell is not used yet
                print('Invalid cell number') # print error
            else:
                # marking cell as used and turn to pc
                table[x] = 'X'
                Turn = False
        else: # if its pcs move
            PCMove = random.choice([i for i in range(0, len(table)) if table[i] != 'X' and table[i] != 'O']) # selecting random cell from not used ones
            table[PCMove] = 'O' # marking as used
            Turn = True # turn to user

        if((table[0] == table[1] and table[1] == table[2] and table[0] == 'X') # checking whether user won or not
                or (table[3] == table[4] and table[4] == table[5] and table[3] == 'X')
                or (table[6] == table[7] and table[7] == table[8] and table[6] == 'X')
                or (table[0] == table[3] and table[3] == table[6] and table[0] == 'X')
                or (table[1] == table[4] and table[4] == table[7] and table[1] == 'X')
                or (table[2] == table[5] and table[5] == table[8] and table[2] == 'X')
                or (table[0] == table[4] and table[4] == table[8] and table[0] == 'X')
                or (table[2] == table[4] and table[4] == table[6] and table[2] == 'X')):
            isFinished = True # indicating that game finished
            print('U won') # printing message
        elif((table[0] == table[1] and table[1] == table[2] and table[0] == 'O') # checking whether pc won or not
             or (table[3] == table[4] and table[4] == table[5] and table[3] == 'O')
             or (table[6] == table[7] and table[7] == table[8] and table[6] == 'O')
             or (table[0] == table[3] and table[3] == table[6] and table[0] == 'O')
             or (table[1] == table[4] and table[4] == table[7] and table[1] == 'O')
             or (table[2] == table[5] and table[5] == table[8] and table[2] == 'O')
             or (table[0] == table[4] and table[4] == table[8] and table[0] == 'O')
             or (table[2] == table[4] and table[4] == table[6] and table[2] == 'O')):
            isFinished = True # indicating that game finished
            print('Pc won') # printing message
        elif table.count('X') + table.count('O') == 9: # checking whether its draw or not
            isFinished = True # indicating that game finished
            print('Draw') # printing message

        if isFinished: # if game has just finished, print game table one last time
            print('Final Result: ')
            for i in range(0, len(table)):
                if i % 3 == 0 and i != 0:
                    print('')
                print(table[i], end = ' ')
            print('')

