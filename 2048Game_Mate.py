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
    # return i,j

def Startposition(stage):
    # global Stage
    # start_row=random.choice(start_position)
    # start_column=random.choice(start_position)
    start_row1 = random.randint(0,3)
    start_column1 = random.randint(0,3)
    start_row2 = random.randint(0,3)
    start_column2 = random.randint(0,3)
    stage[start_row1][start_column1]=2
    stage[start_row2][start_column2]=2
    while start_row1==start_row2 and start_column1==start_column2:
        start_row1 = random.randint(0,3)
        start_column1 = random.randint(0,3)
        
#variable=Stage????
def PlayGround(Stage):
    print (Stage[0][0], "\t", Stage[0][1], "\t", Stage[0][2], "\t", Stage[0][3])
    print (Stage[1][0], "\t", Stage[1][1], "\t", Stage[1][2], "\t", Stage[1][3])
    print (Stage[2][0], "\t", Stage[2][1], "\t", Stage[2][2], "\t", Stage[2][3])
    print (Stage[3][0], "\t", Stage[3][1], "\t", Stage[3][2], "\t", Stage[3][3])

def Newelement(zerostage):
    #csak, ahol 0 van, amikor új Stage lesz
    global Stage
    start_row3 = random.randint(0,3)
    start_column3 = random.randint(0,3)
    while zerostage[start_row3][start_column3] == 0:
        start_row3 = random.randint(0,3)
        start_column3 = random.randint(0,3)
    Stage[start_row3][start_column3] = 2

# def Newelement(function):
#     #csak, ahol 0 van, amikor új Stage lesz
#     global Stage
#     start_row3 = random.randint(0,3)
#     start_column3 = random.randint(0,3)
#     for i in range(4):
#         for j in range(4):
#             if ZeroStage[i][j] == 1:
#                 Stage[start_row3][start_column3]=2

def move_up():
    global Stage
    for i in range(4):
        for j in range(4):
            if Stage[i][j] != 0: #and crash() is not True:
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
            if Stage[i][j] != 0: #and crash() is not True:
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

def move_right():
    global Stage
    for i in range(4):
        for j in range(4):
            if Stage[i][j] != 0: #and crash() is not True:
                if j==0:
                    Stage[i][j+3]=Stage[i][j]
                    Stage[i][j]=0
                if j==1:
                    Stage[i][j+2]=Stage[i][j]
                    Stage[i][j]=0
                if j==2:
                    Stage[i][j+1]=Stage[i][j]
                    Stage[i][j]=0
                if j==3:
                    Stage[i][j]=Stage[i][j]

def move_left():
    global Stage
    for i in range(4):
        for j in range(4):
            if Stage[i][j] != 0: #and crash() is not True:
                if j==0:
                    Stage[i][j]=Stage[i][j]
                if j==1:
                    Stage[i][j-1]=Stage[i][j]
                    Stage[i][j]=0
                if j==2:
                    Stage[i][j-2]=Stage[i][j]
                    Stage[i][j]=0
                if j==3:
                    Stage[i][j-3]=Stage[i][j]
                    Stage[i][j]=0
#???????????????
def fusion():
#before step
    global Stage
    for i in range(4):
        for j in range(4):
            for k in range(4):
                if ZeroStage[i][j] != 1 and Stage[i][j]==Stage[k][j] and k!=i:
                    Stage[i][j]=Stage[i][j]*2

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

# list 0 elements, random, tuple
