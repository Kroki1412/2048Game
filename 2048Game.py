# ========== Functions ==========

# Drawing the 4x4 playground
def PlayGround():
    Range = 21
    Square = Range - 5
    Line1 = "--" * (Range - 3) + "-"
    Line2 = []

    for column in range(Range):
            if column % 5 == 0:
                Line2.append("|")
            elif column == Range:
                print("\n")
            else:
                Line2.append(" "*2)

    for raw in range(Range):
        if raw % 5 == 0:
            print(Line1)
        else:
            print("".join(Line2))

#def: StartPosition():

#def: Controller():

#def: NumInteraction():


#def Initialization(playground, startpos):
    #PlayGround()
    #StartPosition()




# ========== Main ==========

PlayGround()