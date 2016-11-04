import random
import os
import sys
import tty
import termios


def win():
    global Elements
    for i in range(len(Elements)):
        if Elements[i] == 2048:
            print("You won the game!")
            quit()

def right_loose():
    global Elements
    Loose = 0
    for i in range(len(Elements)):
        if Elements[i] == 0:
            Loose = 0
            break
        else:
            Loose = 1
    while Loose == 1:
        for i in range(0,2):
            if Elements[i] != Elements[i+1]:
                Loose = 2
                global Loose
                continue
            elif Elements[i] == Elements[i+1]:
                Loose = 0
                global Loose
                break
        if Loose == 0:
            break
        else:
            for i in range(3,5):
                if Elements[i] != Elements[i+1]:
                    Loose = 2
                    global Loose
                    continue
                elif Elements[i] == Elements[i+1]:
                    Loose = 0
                    global Loose
                    break
            if Loose == 0:
                break
            else:    
                for i in range(6,8):
                    if Elements[i] != Elements[i+1]:
                        Loose = 2
                        global Loose
                        continue
                    elif Elements[i] != Elements[i+1]:
                        Loose = 0
                        global Loose
                        break
                if Loose == 2:
                    print("You lost the game!")
                    quit()
                    break

def left_loose():
    global Elements
    Loose = 0
    for i in range(len(Elements)):
        if Elements[i] == 0:
            Loose = 0
            break
        else:
            Loose = 1
    while Loose == 1:
        for i in range(0,2):
            if Elements[i] != Elements[i+1]:
                Loose = 2
                global Loose
                continue
            elif Elements[i] == Elements[i+1]:
                Loose = 0
                global Loose
                break
        if Loose == 0:
            break
        else:
            for i in range(3,5):
                if Elements[i] != Elements[i+1]:
                    Loose = 2
                    global Loose
                    continue
                elif Elements[i] == Elements[i+1]:
                    Loose = 0
                    global Loose
                    break
            if Loose == 0:
                break
            else:    
                for i in range(6,8):
                    if Elements[i] != Elements[i+1]:
                        Loose = 2
                        global Loose
                        continue
                    elif Elements[i] != Elements[i+1]:
                        Loose = 0
                        global Loose
                        break
                if Loose == 2:
                    print("You lost the game!")
                    quit()
                    break

def up_loose():
    Loose = 0
    for i in range(len(Elements)):
        if Elements[i] == 0:
            Loose = 0
            break
        else:
            Loose = 1
    while Loose == 1:
        for i in range(0,2):
            if Column1[i] == Column1[i+1]:
                Loose = 0
                break
            elif Column2[i] == Column2[i+1]:
                Loose = 0
                break
            elif Column3[i] == Column3[i+1]:
                Loose = 0
                break
            else:
                Loose = 2
                continue
        if Loose == 2:
            print("You lost the game!")
            quit()
            break

def down_loose():
    Loose = 0
    for i in range(len(Elements)):
        if Elements[i] == 0:
            Loose = 0
            break
        else:
            Loose = 1
    while Loose == 1:
        for i in range(0,2):
            if Column1[i] == Column1[i+1]:
                Loose = 0
                break
            elif Column2[i] == Column2[i+1]:
                Loose = 0
                break
            elif Column3[i] == Column3[i+1]:
                Loose = 0
                break
            else:
                Loose = 2
                continue
        if Loose == 2:
            print("You lost the game!")
            quit()
            break

def new_element():
    global Elements
    NewIndex = random.randint(0, 8)
    odds = random.randint(1, 10)
    while True:
        if Elements[NewIndex] == 0:
            if 0 < odds < 6:
                Elements[NewIndex] = 2
                break
            if 5 < odds < 11:
                Elements[NewIndex] = 4
                break
        else:
            NewIndex = random.randint(0, 8)
            continue

def print_playground():
    global Elements
    print(Elements[0], "\t", Elements[1], "\t",Elements[2], "\n")
    print(Elements[3], "\t", Elements[4], "\t",Elements[5], "\n")
    print(Elements[6], "\t", Elements[7], "\t",Elements[8], "\n")

def create_column(index):
    global Elements
    Column = []
    for i in range(len(Elements)):
        if i % 3 == index - 1:
            Column.append(Elements[i])
    return Column

def append_columns():
    global Column1
    global Column2
    global Column3
    global Columns

    Columns = []
    for i in range(len(Column1)):
        Columns.append(Column1[i])
    for i in range(len(Column2)):
        Columns.append(Column2[i])
    for i in range(len(Column3)):
        Columns.append(Column3[i])
    return Columns

def create_row(index):
    global Columns
    Row = []
    for i in range(len(Elements)):
        if i % 3 == index - 1:
            Row.append(Columns[i])
    return Row

def append_rows():
    global Elements
    global Row1
    global Row2
    global Row3
    Row1 = create_row(1)
    Row2 = create_row(2)
    Row3 = create_row(3)
    Elements = []
    for i in range(len(Row1)):
        Elements.append(Row1[i])
    for i in range(len(Row2)):
        Elements.append(Row2[i])
    for i in range(len(Row3)):
        Elements.append(Row3[i])

def combine_right():
    global Elements

    for i in range(2, 0, -1):
        if Elements[i] == 0:
            continue
        if Elements[i] != 0:
            for j in range(i - 1, -1, -1):
                if Elements[j] == 0:
                    continue
                if Elements[j] != 0:
                    if Elements[j] != Elements[i]:
                        break
                    if Elements[j] == Elements[i]:
                        Elements[i] *= 2
                        Elements[j] = 0
                        break
        continue

    for i in range(5, 3, -1):
        if Elements[i] == 0:
            continue
        if Elements[i] != 0:
            for j in range(i - 1, 2, -1):
                if Elements[j] == 0:
                    continue
                if Elements[j] != 0:
                    if Elements[j] != Elements[i]:
                        break
                    if Elements[j] == Elements[i]:
                        Elements[i] *= 2
                        Elements[j] = 0
                        break
        continue

    for i in range(8, 6, -1):
        if Elements[i] == 0:
            continue
        if Elements[i] != 0:
            for j in range(i - 1, 5, -1):
                if Elements[j] == 0:
                    continue
                if Elements[j] != 0:
                    if Elements[j] != Elements[i]:
                        break
                    if Elements[j] == Elements[i]:
                        Elements[i] *= 2
                        Elements[j] = 0
                        break
        continue

def combine_left():
    global Elements
    
    for i in range(0, 2):
        if Elements[i] == 0:
            continue
        if Elements[i] != 0:
            for j in range(i + 1, 3):
                if Elements[j] == 0:
                    continue
                if Elements[j] != 0:
                    if Elements[j] != Elements[i]:
                        break
                    if Elements[j] == Elements[i]:
                        Elements[i] *= 2
                        Elements[j] = 0
                        break
        continue

    for i in range(3, 5):
        if Elements[i] == 0:
            continue
        if Elements[i] != 0:
            for j in range(i + 1, 6):
                if Elements[j] == 0:
                    continue
                if Elements[j] != 0:
                    if Elements[j] != Elements[i]:
                        break
                    if Elements[j] == Elements[i]:
                        Elements[i] *= 2
                        Elements[j] = 0
                        break
        continue

    for i in range(6, 8):
        if Elements[i] == 0:
            continue
        if Elements[i] != 0:
            for j in range(i + 1, 9):
                if Elements[j] == 0:
                    continue
                if Elements[j] != 0:
                    if Elements[j] != Elements[i]:
                        break
                    if Elements[j] == Elements[i]:
                        Elements[i] *= 2
                        Elements[j] = 0
                        break
        continue

def combine_up():
    global Column1
    global Column2
    global Column3
    global Row1
    global Row2
    global Row3
    Column1 = create_column(1)
    Column2 = create_column(2)
    Column3 = create_column(3)
    
    for i in range(0, 2):
        if Column1[i] == 0:
            continue
        if Column1[i] != 0:
            for j in range(i + 1, 3):
                if Column1[j] == 0:
                    continue
                if Column1[j] != 0:
                    if Column1[j] != Column1[i]:
                        break
                    if Column1[j] == Column1[i]:
                        Column1[i] *= 2
                        Column1[j] = 0
                        break
        continue

    for i in range(0, 2):
        if Column2[i] == 0:
            continue
        if Column2[i] != 0:
            for j in range(i + 1, 3):
                if Column2[j] == 0:
                    continue
                if Column2[j] != 0:
                    if Column2[j] != Column2[i]:
                        break
                    if Column2[j] == Column2[i]:
                        Column2[i] *= 2
                        Column2[j] = 0
                        break
        continue

    for i in range(0, 2):
        if Column3[i] == 0:
            continue
        if Column3[i] != 0:
            for j in range(i + 1, 3):
                if Column3[j] == 0:
                    continue
                if Column3[j] != 0:
                    if Column3[j] != Column3[i]:
                        break
                    if Column3[j] == Column3[i]:
                        Column3[i] *= 2
                        Column3[j] = 0
                        break
        continue

    append_columns()
    Row1 = create_row(1)
    Row2 = create_row(2)
    Row3 = create_row(3)
    append_rows

def combine_down():
    global Column1
    global Column2
    global Column3
    global Row1
    global Row2
    global Row3
    Column1 = create_column(1)
    Column2 = create_column(2)
    Column3 = create_column(3)

    for i in range(2, 0, -1):
        if Column1[i] == 0:
            continue
        if Column1[i] != 0:
            for j in range(i - 1, -1, -1):
                if Column1[j] == 0:
                    continue
                if Column1[j] != 0:
                    if Column1[j] != Column1[i]:
                        break
                    if Column1[j] == Column1[i]:
                        Column1[i] *= 2
                        Column1[j] = 0
                        break
        continue

    for i in range(2, 0, -1):
        if Column2[i] == 0:
            continue
        if Column2[i] != 0:
            for j in range(i - 1, -1, -1):
                if Column2[j] == 0:
                    continue
                if Column2[j] != 0:
                    if Column2[j] != Column2[i]:
                        break
                    if Column2[j] == Column2[i]:
                        Column2[i] *= 2
                        Column2[j] = 0
                        break
        continue

    for i in range(2, 0, -1):
        if Column3[i] == 0:
            continue
        if Column3[i] != 0:
            for j in range(i - 1, -1, -1):
                if Column3[j] == 0:
                    continue
                if Column3[j] != 0:
                    if Column3[j] != Column3[i]:
                        break
                    if Column3[j] == Column3[i]:
                        Column3[i] *= 2
                        Column3[j] = 0
                        break
        continue
    
    append_columns()
    Row1 = create_row(1)
    Row2 = create_row(2)
    Row3 = create_row(3)
    append_rows

def move_left():
    global Elements
    combine_left()
    for i in range(0, 2):
        while i < 2:
            if Elements[i] == 0 and Elements[i+1] != 0:
                Elements[i] = Elements[i+1]
                Elements[i+1] = 0
                i = 0
                continue
            else:
                i += 1
                continue

    for i in range(3,5):
        while i < 5:
            if Elements[i] == 0 and Elements[i+1] != 0:
                Elements[i] = Elements[i+1]
                Elements[i+1] = 0
                i = 3
                continue
            else:
                i += 1
                continue

    for i in range(6,8):
        while i < 8:
            if Elements[i] == 0 and Elements[i+1] != 0:
                Elements[i] = Elements[i+1]
                Elements[i+1] = 0
                i = 6
                continue
            else:
                i += 1
                continue

def move_right():
    global Elements
    combine_right()
    for i in range(2,0,-1):
        while i > 0:
            if Elements[i] == 0 and Elements[i-1] != 0:
                Elements[i] = Elements[i-1]
                Elements[i-1] = 0
                i = 2
                continue
            else:
                i -= 1
                continue

    for i in range(5,3,-1):
        while i > 3:
            if Elements[i] == 0 and Elements[i-1] != 0:
                Elements[i] = Elements[i-1]
                Elements[i-1] = 0
                i = 5
                continue
            else:
                i -= 1
                continue

    for i in range(8,6,-1):
        while i > 6:
            if Elements[i] == 0 and Elements[i-1] != 0:
                Elements[i] = Elements[i-1]
                Elements[i-1] = 0
                i = 8
                continue
            else:
                i -= 1
                continue

def move_up():
    global Elements
    global Column1
    global Column2
    global Column3
    global Columns
    combine_up()
    i = 0
    while i < 2:
        if Column1[i] == 0 and Column1[i+1] != 0:
            Column1[i] = Column1[i+1]
            Column1[i+1] = 0
            i=0
            continue
        if Column2[i] == 0 and Column2[i+1] != 0:
            Column2[i] = Column2[i+1]
            Column2[i+1] = 0
            i=0
            continue
        if Column3[i] == 0 and Column3[i+1] != 0:
            Column3[i] = Column3[i+1]
            Column3[i+1] = 0
            i=0
            continue
        else:
            i += 1
            continue
    append_columns()
    append_rows()
    # manage_zeros()

def move_down():
    global Elements
    global Column1
    global Column2
    global Column3
    global Columns
    combine_down()
    i = 2
    while i > 0:
        if Column1[i] == 0 and Column1[i-1] != 0:
            Column1[i] = Column1[i-1]
            Column1[i-1] = 0
            i = 2
            continue
        if Column2[i] == 0 and Column2[i-1] != 0:
            Column2[i] = Column2[i-1]
            Column2[i-1] = 0
            i = 2
            continue
        if Column3[i] == 0 and Column3[i-1] != 0:
            Column3[i] = Column3[i-1]
            Column3[i-1] = 0
            i = 2
            continue        
        else:
            i -= 1
            continue
    
    append_columns()
    append_rows()

def save_game():
    global Elements
    file = open("save_3x3.dat", "w")
    for i in range(len(Elements)):
        file.write(str(Elements[i]))
        file.write("\n")
    file.close()

def load_game():
    global Elements
    try:
        file = open("save_3x3.dat", "r")
        ElementsLine = file.readlines()

        for i in range(len(Elements)):
            Elements[i] = int(ElementsLine[i])
        file.close()
    except FileNotFoundError:
        print("File does not exist!")
        quit()


class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def main():
    while True:
        load = input("New game ('n') or load an existing game ('l'): ")
        if load == "l":
            load_game()
            break
        if load == "n":
            break
        else:
            continue
    
    new_element()
    new_element()
    os.system('cls')  # for Windows
    os.system('clear')  # for Linux/OS X
    print_playground()
    Command = None
    while True:
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k == '\x1b[D':
            move_left()
            win()
            left_loose()
            new_element()
            os.system('cls')  # for Windows
            os.system('clear')  # for Linux/OS X
            print_playground()
            continue
        if k == '\x1b[C':
            move_right()
            win()
            right_loose()
            new_element()
            os.system('cls')  # for Windows
            os.system('clear')  # for Linux/OS X
            print_playground()
            continue
        if k == '\x1b[A':
            move_up()
            win()
            up_loose()
            new_element()
            os.system('cls')  # for Windows
            os.system('clear')  # for Linux/OS X
            print_playground()
            continue
        if k == '\x1b[B':
            move_down()
            win()
            down_loose()
            new_element()
            os.system('cls')  # for Windows
            os.system('clear')  # for Linux/OS X
            print_playground()
            continue
        if k == "esc":
            while True:
                Exit = input("Do you want to save the game? (y/n): ")
                if Exit == "y":
                    save_game()
                    os.system('cls')  # for Windows
                    os.system('clear')  # for Linux/OS X
                    print("Game saved!")
                    print("-----------")
                    break
                if Exit == "n":
                    os.system('cls')  # for Windows
                    os.system('clear')  # for Linux/OS X
                    break
                else:
                    print("Invalid command!")
                    continue
            break
        else:
            print("Invalid command!")
            continue

# ========== Global variables ==========

# Elements = [0,0,0,0,0,0,0,0,0]
Elements = [0 for null in range(9)]

Column1 = []
Column2 = []
Column3 = []
Row1 = []
Row2 = []
Row3 = []

# ========== Main ========== 

# main()