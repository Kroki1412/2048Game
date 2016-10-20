import random
# ========== Global variables ==========

ZeroStage = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
Stage=[[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]

# ========== Functions ==========

def ZeroStagef(ZeroStage):
    global Stage
    for i in range(4):
        for j in range(4):
            if Stage[i][j] == 0:
                ZeroStage[i][j] = 1
            if Stage[i][j] != 0:
                ZeroStage[i][j] = 0
    return ZeroStage

def Startposition(stage):
    start_row1 = random.randint(0,3)
    start_column1 = random.randint(0,3)
    start_row2 = random.randint(0,3)
    start_column2 = random.randint(0,3)
    stage[start_row1][start_column1]=2
    stage[start_row2][start_column2]=2
    while start_row1==start_row2 and start_column1==start_column2:
        start_row1 = random.randint(0,3)
        start_column1 = random.randint(0,3)
        
def PlayGround(Stage):
    print (Stage[0][0], "\t", Stage[0][1], "\t", Stage[0][2], "\t", Stage[0][3])
    print (Stage[1][0], "\t", Stage[1][1], "\t", Stage[1][2], "\t", Stage[1][3])
    print (Stage[2][0], "\t", Stage[2][1], "\t", Stage[2][2], "\t", Stage[2][3])
    print (Stage[3][0], "\t", Stage[3][1], "\t", Stage[3][2], "\t", Stage[3][3])

def Newelement(zerostage):
    global Stage
    start_row3 = random.randint(0,3)
    start_column3 = random.randint(0,3)
    while zerostage[start_row3][start_column3] == 0:
        start_row3 = random.randint(0,3)
        start_column3 = random.randint(0,3)
    Stage[start_row3][start_column3] = 2

def fusion_left(Stage):
    for i in range(4):
        j = 0
        while j < 3:
            if Stage[i][j] == Stage[i][j+1]:
                Stage[i][j] *= 2
                Stage[i][j+1] = 0
                j += 1
                break
            else:
                j += 1
                continue

def fusion_right(Stage):
    for i in range(4):
        j = -1
        while j > -4:
            if Stage[i][j] == Stage[i][j-1]:
                Stage[i][j] *= 2
                Stage[i][j-1] = 0
                j -= 1
                break
            else:
                j -= 1
                continue

def move_up():
    global Stage
    for i in range(4):
        for j in range(4):
            if Stage[i][j] != 0:
                if i==0:
                    Stage[i][j]=Stage[i][j]
                if i==1:
                    Stage[i-1][j]=Stage[i][j]  
                    Stage[i][j]=0
                if i==2:
                    Stage[i-2][j]=Stage[i][j] 
                    Stage[i][j]=0
                if i==3:
                    Stage[i-3][j]=Stage[i][j] 
                    Stage[i][j]=0

def move_down():
    global Stage
    for i in range(4):
        for j in range(4):
            if Stage[i][j] != 0:
                if i==0:
                    Stage[i+3][j]=Stage[i][j] 
                    Stage[i][j]=0
                if i==1:
                    Stage[i+2][j]=Stage[i][j]  
                    Stage[i][j]=0
                if i==2:
                    Stage[i+1][j]=Stage[i][j] 
                    Stage[i][j]=0
                if i==3:
                    Stage[i][j]=Stage[i][j]

def move_left():
    global Stage
    for i in range(4):
        j = 0
        Member = 1
        while j < 3:
            if Stage[i][j] == Stage[i][j+1] and Stage[i][j] != 0:
                fusion_left(Stage)
                j = 1
                continue
            if Stage[i][j] == 0:                        
                if Stage[i][j+1] != 0:
                    Stage[i][j] = Stage[i][j+1]
                    Stage[i][j+1] = 0
                    j -= 1
                    if j < 1:
                        Member += 1
                    if Member < 3:
                        j = +1
                    else:
                        break
                    continue
                else:
                    j += 1
            else:
                j += 1

def move_right():
    global Stage
    for i in range(4):
        j = -1
        Member = 1
        while j > -4:
            if Stage[i][j] == Stage[i][j-1] and Stage[i][j-1] != 0:
                fusion_right(Stage)
                j = -1
                continue
            if Stage[i][j] == 0:                        
                if Stage[i][j-1] != 0:
                    Stage[i][j] = Stage[i][j-1]
                    Stage[i][j-1] = 0
                    j += 1
                    if j > -1:
                        Member += 1
                    if Member < 3:
                        j = -1
                    else:
                        break
                    continue
                else:
                    j -= 1
            else:
                j -= 1

def key_press():
    while True:
        direction=input("Direction: ")
        if direction == "w":
            move_up()
            Newelement(ZeroStagef(ZeroStage))
            PlayGround(Stage)
        elif direction == "s":
            move_down()
            Newelement(ZeroStagef(ZeroStage))
            PlayGround(Stage)
        elif direction == "d":
            move_right()
            Newelement(ZeroStagef(ZeroStage))
            PlayGround(Stage)
        elif direction == "a":
            move_left()
            Newelement(ZeroStagef(ZeroStage))
            PlayGround(Stage)
        elif direction == "q":
            quit()
        else:
            print("Invalid command!")

# ========== Main ==========

Startposition(Stage)
PlayGround(Stage)
key_press()
