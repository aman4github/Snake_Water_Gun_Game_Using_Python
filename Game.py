import random

user_win, com_win, draw = 0, 0, 0

while True:
    com_ch = random.randint(1, 3)
    print("Menu : \nPress 1 to choose Snake.\nPress 2 to choose Water.\nPress 3 to choose Gun.\nPress 4 to view the Scoreboard.\nPress 0 to Exit.")
    user_ch = int(input("Enter your choise : "))
    if user_ch == com_ch:
        draw += 1
        print("\n\tDraw\n")

    elif user_ch == 1:
        if com_ch == 2:
            user_win += 1
            print("\nComputer = Water\nUser = Snake\n\tUser Wins\n")
        elif com_ch == 3:
            com_win += 1
            print("\nComputer = Gun\nUser = Snake\n\tComputer Wins\n")

    elif user_ch == 2:
        if com_ch == 1:
            com_win += 1
            print("\nComputer = Snake\nUser = Water\n\tComputer Wins\n")
        elif com_ch == 3:
            user_win += 1
            print("\nComputer = Gun\nUser = Water\n\tUser Wins\n")

    elif user_ch == 3:
        if com_ch == 1:
            user_win += 1
            print("\nComputer = Snake\nUser = Gun\n\tUser Wins\n")
        elif com_ch == 2:
            com_win += 1
            print("\nComputer = Water\nUser = Gun\n\tComputer Wins\n")

    elif user_ch == 4:
        print(f"\n\tComputer = {com_win}\tUser = {user_win}\tDraw = {draw}\n")

    elif user_ch == 0:
        break

    else :
        print("\n\tEnter a Valid Choise\n")
