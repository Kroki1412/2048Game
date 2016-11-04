import os
import mode_3x3
import mode_4x4
import mode_5x5


os.system('cls')  # for Windows
os.system('clear')  # for Linux/OS X

while True:    
    print("Welcome in 2048 game!")
    print("=====================")
    print("Game ontrol: arrow keys")
    print("3x3 game:   '3'")
    print("4x4 game:   '4'")
    print("5x5 game:   '5'")
    print("Exit:       'esc'\n")

    mode = input("Please select a game mode: ")

    if mode == "3":
        mode_3x3.main()
        continue
    if mode == "4":
        mode_4x4.main()
        continue
    if mode == "5":
        mode_5x5.main()
        continue
    if mode == "esc":
        break
    else:
        continue
