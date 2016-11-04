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
        for i in range(0,3):
            if Elements[i] != Elements[i+1]:
                Loose = 2
                continue
            elif Elements[i] == Elements[i+1]:
                Loose = 0
                break
        if Loose == 0:
            break
        else:
            for i in range(4,7):
                if Elements[i] != Elements[i+1]:
                    Loose = 2
                    continue
                elif Elements[i] == Elements[i+1]:
                    Loose = 0
                    break
            if Loose == 0:
                break
            else:    
                for i in range(8,11):
                    if Elements[i] != Elements[i+1]:
                        Loose = 2
                        continue
                    elif Elements[i] != Elements[i+1]:
                        Loose = 0
                        break
                if Loose == 0:
                    break
                else:
                    for i in range(12,15):
                        if Elements[i] != Elements[i+1]:
                            Loose = 2
                            continue
                        elif Elements[i] == Elements[i+1]:
                            Loose = 0
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
        for i in range(0,3):
            if Elements[i] != Elements[i+1]:
                Loose = 2
                continue
            elif Elements[i] == Elements[i+1]:
                Loose = 0
                break
        if Loose == 0:
            break
        else:
            for i in range(4,7):
                if Elements[i] != Elements[i+1]:
                    Loose = 2
                    continue
                elif Elements[i] == Elements[i+1]:
                    Loose = 0
                    break
            if Loose == 0:
                break
            else:    
                for i in range(8,11):
                    if Elements[i] != Elements[i+1]:
                        Loose = 2
                        continue
                    elif Elements[i] != Elements[i+1]:
                        Loose = 0
                        break
                if Loose == 0:
                    break
                else:
                    for i in range(12,15):
                        if Elements[i] != Elements[i+1]:
                            Loose = 2
                            continue
                        elif Elements[i] == Elements[i+1]:
                            Loose = 0
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
        for i in range(0,3):
            if Column1[i] == Column1[i+1]:
                Loose = 0
                break
            elif Column2[i] == Column2[i+1]:
                Loose = 0
                break
            elif Column3[i] == Column3[i+1]:
                Loose = 0
                break
            elif Column4[i] == Column4[i+1]:
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
        for i in range(0,3):
            if Column1[i] == Column1[i+1]:
                Loose = 0
                break
            elif Column2[i] == Column2[i+1]:
                Loose = 0
                break
            elif Column3[i] == Column3[i+1]:
                Loose = 0
                break
            elif Column4[i] == Column4[i+1]:
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
    NewIndex = random.randint(0, 15)
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
            NewIndex = random.randint(0, 15)
            continue

def print_playground():
    global Elements
    print(Elements[0], "\t", Elements[1], "\t",Elements[2], "\t",Elements[3], "\n")
    print(Elements[4], "\t", Elements[5], "\t",Elements[6], "\t",Elements[7], "\n")
    print(Elements[8], "\t", Elements[9], "\t",Elements[10], "\t",Elements[11], "\n")
    print(Elements[12], "\t", Elements[13], "\t",Elements[14], "\t",Elements[15], "\n")

def create_column(index):
    global Elements
    Column = []
    for i in range(len(Elements)):
        if i % 4 == index - 1:
            Column.append(Elements[i])
    return Column

def append_columns():
    global Column1
    global Column2
    global Column3
    global Column4
    global Columns

    Columns = []
    for i in range(len(Column1)):
        Columns.append(Column1[i])
    for i in range(len(Column2)):
        Columns.append(Column2[i])
    for i in range(len(Column3)):
        Columns.append(Column3[i])
    for i in range(len(Column4)):
        Columns.append(Column4[i])
    return Columns

def create_row(index):
    global Columns
    Row = []
    for i in range(len(Elements)):
        if i % 4 == index - 1:
            Row.append(Columns[i])
    return Row

def append_rows():
    global Elements
    global Row1
    global Row2
    global Row3
    global Row4
    Row1 = create_row(1)
    Row2 = create_row(2)
    Row3 = create_row(3)
    Row4 = create_row(4)
    Elements = []
    for i in range(len(Row1)):
        Elements.append(Row1[i])
    for i in range(len(Row2)):
        Elements.append(Row2[i])
    for i in range(len(Row3)):
        Elements.append(Row3[i])
    for i in range(len(Row4)):
        Elements.append(Row4[i])

def combine_right():
    global Elements

    for i in range(3, 0, -1):
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

    for i in range(7, 4, -1):
        if Elements[i] == 0:
            continue
        if Elements[i] != 0:
            for j in range(i - 1, 3, -1):
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

    for i in range(11, 8, -1):
        if Elements[i] == 0:
            continue
        if Elements[i] != 0:
            for j in range(i - 1, 7, -1):
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

    for i in range(15, 12, -1):
        if Elements[i] == 0:
            continue
        if Elements[i] != 0:
            for j in range(i - 1, 11, -1):
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
    
    for i in range(0, 3):
        if Elements[i] == 0:
            continue
        if Elements[i] != 0:
            for j in range(i + 1, 4):
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

    for i in range(4, 7):
        if Elements[i] == 0:
            continue
        if Elements[i] != 0:
            for j in range(i + 1, 8):
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

    for i in range(8, 11):
        if Elements[i] == 0:
            continue
        if Elements[i] != 0:
            for j in range(i + 1, 12):
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

    for i in range(12, 15):
        if Elements[i] == 0:
            continue
        if Elements[i] != 0:
            for j in range(i + 1, 16):
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
    global Column4
    global Row1
    global Row2
    global Row3
    global Row4
    Column1 = create_column(1)
    Column2 = create_column(2)
    Column3 = create_column(3)
    Column4 = create_column(4)
    
    for i in range(0, 3):
        if Column1[i] == 0:
            continue
        if Column1[i] != 0:
            for j in range(i + 1, 4):
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

    for i in range(0, 3):
        if Column2[i] == 0:
            continue
        if Column2[i] != 0:
            for j in range(i + 1, 4):
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

    for i in range(0, 3):
        if Column3[i] == 0:
            continue
        if Column3[i] != 0:
            for j in range(i + 1, 4):
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

    for i in range(0, 3):
        if Column4[i] == 0:
            continue
        if Column4[i] != 0:
            for j in range(i + 1, 4):
                if Column4[j] == 0:
                    continue
                if Column4[j] != 0:
                    if Column4[j] != Column4[i]:
                        break
                    if Column4[j] == Column4[i]:
                        Column4[i] *= 2
                        Column4[j] = 0
                        break
        continue

    append_columns()
    Row1 = create_row(1)
    Row2 = create_row(2)
    Row3 = create_row(3)
    Row4 = create_row(4)
    append_rows

def combine_down():
    global Column1
    global Column2
    global Column3
    global Column4
    global Row1
    global Row2
    global Row3
    global Row4
    Column1 = create_column(1)
    Column2 = create_column(2)
    Column3 = create_column(3)
    Column4 = create_column(4)

    for i in range(3, 0, -1):
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

    for i in range(3, 0, -1):
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

    for i in range(3, 0, -1):
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

    for i in range(3, 0, -1):
        if Column4[i] == 0:
            continue
        if Column4[i] != 0:
            for j in range(i - 1, -1, -1):
                if Column4[j] == 0:
                    continue
                if Column4[j] != 0:
                    if Column4[j] != Column4[i]:
                        break
                    if Column4[j] == Column4[i]:
                        Column4[i] *= 2
                        Column4[j] = 0
                        break
        continue
    
    append_columns()
    Row1 = create_row(1)
    Row2 = create_row(2)
    Row3 = create_row(3)
    Row4 = create_row(4)
    append_rows

def move_left():
    global Elements
    combine_left()
    for i in range(0,3):
        while i < 3:
            if Elements[i] == 0 and Elements[i+1] != 0:
                Elements[i] = Elements[i+1]
                Elements[i+1] = 0
                i = 0
                continue
            else:
                i += 1
                continue

    for i in range(4,7):
        while i < 7:
            if Elements[i] == 0 and Elements[i+1] != 0:
                Elements[i] = Elements[i+1]
                Elements[i+1] = 0
                i = 4
                continue
            else:
                i += 1
                continue

    for i in range(8,11):
        while i < 11:
            if Elements[i] == 0 and Elements[i+1] != 0:
                Elements[i] = Elements[i+1]
                Elements[i+1] = 0
                i = 8
                continue
            else:
                i += 1
                continue

    for i in range(12,15):
        while i < 15:
            if Elements[i] == 0 and Elements[i+1] != 0:
                Elements[i] = Elements[i+1]
                Elements[i+1] = 0
                i = 12
                continue
            else:
                i += 1
                continue

    # manage_zeros()

def move_right():
    global Elements
    combine_right()
    for i in range(3,0,-1):
        while i > 0:
            if Elements[i] == 0 and Elements[i-1] != 0:
                Elements[i] = Elements[i-1]
                Elements[i-1] = 0
                i = 3
                continue
            else:
                i -= 1
                continue

    for i in range(7,4,-1):
        while i > 4:
            if Elements[i] == 0 and Elements[i-1] != 0:
                Elements[i] = Elements[i-1]
                Elements[i-1] = 0
                i = 7
                continue
            else:
                i -= 1
                continue

    for i in range(11,8,-1):
        while i > 8:
            if Elements[i] == 0 and Elements[i-1] != 0:
                Elements[i] = Elements[i-1]
                Elements[i-1] = 0
                i = 11
                continue
            else:
                i -= 1
                continue

    for i in range(15,12,-1):
        while i > 12:
            if Elements[i] == 0 and Elements[i-1] != 0:
                Elements[i] = Elements[i-1]
                Elements[i-1] = 0
                i = 15
                continue
            else:
                i -= 1
                continue

    # manage_zeros()

def move_up():
    global Elements
    global Column1
    global Column2
    global Column3
    global Column4
    global Columns
    combine_up()
    i = 0
    while i < 3:
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
        if Column4[i] == 0 and Column4[i+1] != 0:
            Column4[i] = Column4[i+1]
            Column4[i+1] = 0
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
    global Column4
    global Columns
    combine_down()
    i = 3
    while i > 0:
        if Column1[i] == 0 and Column1[i-1] != 0:
            Column1[i] = Column1[i-1]
            Column1[i-1] = 0
            i = 3
            continue
        if Column2[i] == 0 and Column2[i-1] != 0:
            Column2[i] = Column2[i-1]
            Column2[i-1] = 0
            i = 3
            continue
        if Column3[i] == 0 and Column3[i-1] != 0:
            Column3[i] = Column3[i-1]
            Column3[i-1] = 0
            i = 3
            continue
        if Column4[i] == 0 and Column4[i-1] != 0:
            Column4[i] = Column4[i-1]
            Column4[i-1] = 0
            i = 3
            continue          
        else:
            i -= 1
            continue
    
    append_columns()
    append_rows()

def save_game():
    global Elements
    file = open("save_4x4.dat", "w")
    for i in range(len(Elements)):
        file.write(str(Elements[i]))
        file.write("\n")
    file.close()

def load_game():
    global Elements
    try:
        file = open("save_4x4.dat", "r")
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

# Elements = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
Elements = [0 for null in range(16)]

Column1 = []
Column2 = []
Column3 = []
Column4 = []
Row1 = []
Row2 = []
Row3 = []
Row4 = []

# ========== Main ========== 

# main()