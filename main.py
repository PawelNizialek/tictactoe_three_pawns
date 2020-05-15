import time
import boardclass as bc
import notification as no
import tkinter.messagebox
from tkinter import *
update = 0
place_delete = 0
while True:
    while True:
        try:
            level = int(input("0 - easy, 1 - hard: "))
        except ValueError:
            print("It is not a number! Try again!!!")
            continue
        if level in range(0, 2):
            break

    game_run = 0
    pawns_limit = 0
    GameBoard = bc.Board()
    GameBoardCopy = bc.Board()
    shape_tab = []
    time_checker = 0
    player_shape = input("X or O ??:")
    while True:
        if player_shape == "X":
            computer_shape = "O"
            game_run = 1
            player_name = input("Your name?: ")
            break
        elif player_shape == "O":
            computer_shape = "X"
            game_run = 1
            player_name = input("Your name?: ")
            break
        player_shape = input("Try to type X or O: ")
    if game_run == 1:
        break

root = Tk()
root.resizable(False, False)
Main = Frame(root, width =400, height=300,relief=RIDGE)
Main.grid(row=1, column=0)
Board = Frame(Main, width=400, heigh =300, relief=RIDGE)
Board.pack(side=TOP)

buttons = []

def click(buttons, number):
    global click
    global update
    global place_delete
    player(number)
    if update:
        update = 0
        buttons["text"] = player_shape
        place_delete=0
        computer()
    if win() == -1:
        scorekeeper(player_shape)
    if win() == 1:
        scorekeeper(computer_shape)

def win():
    global game_run
    for i in range(9):
        GameBoardCopy.board[i] = GameBoard.board[i]

    win_check = GameBoard.win_checker(player_shape, computer_shape)

    if win_check == -1:
        print("=============")
        GameBoard.draw_board()
        print(player_name, " win")
        game_run = 0

    elif win_check == 0:
        print("=============")
        GameBoard.draw_board()
        print("remis")
        game_run = 0

    elif win_check == 1:
        print("=============")
        GameBoard.draw_board()
        print("computer win")
        game_run = 0
    return win_check


def shape_tab_edit(it, shape):
    for j in range(len(shape_tab)):
        del shape_tab[0]
    for k in range(9):
        if GameBoardCopy.board[k] == shape:
            shape_tab.append(k)
    return shape_tab[it]

def player(number):
    global update
    global pawns_limit
    global place_delete
    if pawns_limit == 0:
        move = int(number)
        move = move - 1
        if move in range(0, 9):
            if GameBoard.board[move] == computer_shape or GameBoard.board[move] == player_shape:
                print("already exists; try again")
                return 0
            GameBoard.board[move] = player_shape
            update=1
        else:
            print("Try to type a number(1;9)")
            return 0
    else:
        if place_delete == 0:
            move = int(number)
            move = move - 1
            if move in range(0, 9):
                if GameBoard.board[move] == computer_shape:
                    print("computer's pawn; try again")
                    return 0
                if GameBoard.board[move] == ' ':
                    print("blank place")
                    return 0
                if GameBoard.board[move] == player_shape and place_delete == 0:
                    GameBoard.board[move] = ' '
                    button_number(move,' ')
                    print("You deleted place number: ", move + 1)
                    place_delete = 1
                    return 0
            else:
                print("Try to type a number(1;9)")
                return 0

        move = number
        move = move - 1
        if move in range(0, 9):
            if GameBoard.board[move] == computer_shape or GameBoard.board[move] == player_shape:
                print("already exists; try again")
                return 0
            GameBoard.board[move] = player_shape
            update = 1

def button_number(number_to_change,shape):
    if number_to_change==0:
        button1['text'] = shape
    elif number_to_change==1:
        button2['text'] = shape
    elif number_to_change==2:
        button3['text'] = shape
    elif number_to_change==3:
        button4['text'] = shape
    elif number_to_change==4:
        button5['text'] = shape
    elif number_to_change==5:
        button6['text'] = shape
    elif number_to_change==6:
        button7['text'] = shape
    elif number_to_change==7:
        button8['text'] = shape
    elif number_to_change==8:
        button9['text'] = shape
    pass



def minmax(depth=0, max_min=1):
    result = GameBoardCopy.win_checker(player_shape, computer_shape)
    if result is not None:
        return result
    if max_min:
        best_score = -10
        for i in range(9):
            if GameBoardCopy.board[i] == " ":
                GameBoardCopy.board[i] = computer_shape
                score = minmax(depth + 1, 0)
                GameBoardCopy.board[i] = " "
                if best_score < score:
                    best_score = score
        return best_score
    else:
        best_score = 10
        for i in range(9):
            if GameBoardCopy.board[i] == ' ':
                GameBoardCopy.board[i] = player_shape
                score = minmax(depth + 1, 1)
                GameBoardCopy.board[i] = ' '
                if best_score > score:
                    best_score = score
        return best_score
def minmax_for_three_pawns(seconds, min_max_time, depth=0, max=1, it=0):
    seconds_to_check = seconds
    first_time = min_max_time
    pawn_to_remove = it
    result = GameBoardCopy.win_checker(player_shape, computer_shape)
    if result is not None:
        return result
    if level == 0:
        if depth == 2:
            return 0
    else:
        if depth == 6:
            return 0

    if time.time() - first_time > seconds_to_check / 9:
        return 0

    if max:
        best_score = -10
        for i in range(9):
            if GameBoardCopy.board[i] == " ":
                for h in range(3):
                    u = shape_tab_edit(h, computer_shape)
                    GameBoardCopy.board[u] = " "
                    GameBoardCopy.board[i] = computer_shape

                    score = minmax_for_three_pawns(seconds_to_check, first_time, depth + 1, 0, pawn_to_remove)

                    GameBoardCopy.board[u] = computer_shape
                    GameBoardCopy.board[i] = " "

                    if best_score < score:
                        best_score = score

        return best_score

    else:

        best_score = 10
        for i in range(9):
            if GameBoardCopy.board[i] == ' ':
                for g in range(3):
                    u = shape_tab_edit(g, player_shape)
                    GameBoardCopy.board[u] = " "
                    GameBoardCopy.board[i] = player_shape

                    score = minmax_for_three_pawns(seconds_to_check, first_time, depth + 1, 1, pawn_to_remove)

                    GameBoardCopy.board[u] = player_shape
                    GameBoardCopy.board[i] = " "

                    if best_score > score:
                        best_score = score

        return best_score
def computer():
    for i in range(9):
        GameBoardCopy.board[i] = GameBoard.board[i]
    global pawns_limit
    global time_checker
    if level == 0:
        seconds_to_check = 1
    elif level == 1:
        seconds_to_check = 4
    points = -1
    time_checker = 0
    start_time = time.time()
    best_place_to_remove = 0
    move = 0
    best_score = -100

    for i in range(9):
        if GameBoardCopy.board[i] == computer_shape:
            shape_tab.append(i)

    if len(shape_tab) > 1:
        pawns_limit = 1

    if len(shape_tab) > 2:
        if seconds_to_check > 2:
            print("Response time: max ", seconds_to_check + 1, " seconds. Please wait. Finding the best move...")
        for i in range(9):
            if GameBoardCopy.board[i] == " ":
                easy_flag = 0
                for computer_shape_number in range(3):
                    if level == 0 and easy_flag == 0:
                        computer_shape_number = 1
                        easy_flag = 1
                    remove = shape_tab_edit(computer_shape_number, computer_shape)
                    GameBoardCopy.board[remove] = ' '
                    GameBoardCopy.board[i] = computer_shape

                    min_max_time = time.time()
                    points = minmax_for_three_pawns(seconds_to_check, min_max_time, 0, 0, computer_shape_number)
                    time_checker = no.notification(start_time, time_checker)

                    GameBoardCopy.board[remove] = computer_shape
                    GameBoardCopy.board[i] = ' '

                    if best_score <= points:
                        best_score = points
                        best_place_to_remove = remove
                        move = i

                if points == 1:
                    break

        GameBoard.board[best_place_to_remove] = ' '
        button_number(best_place_to_remove, ' ')
        GameBoard.board[move] = computer_shape
        button_number(move, computer_shape)

    else:
        for i in range(9):
            if GameBoardCopy.board[i] == " ":
                GameBoardCopy.board[i] = computer_shape

                points = minmax(0, 0)
                GameBoardCopy.board[i] = ' '

                if best_score <= points:
                    best_score = points
                    move = i
        print(move)
        GameBoard.board[move] = computer_shape
        button_number(move,computer_shape)

    for j in range(len(shape_tab)):
        del shape_tab[0]
def scorekeeper(shape):
    GameBoard.draw_board()
    if GameBoard.board[0]==shape and GameBoard.board[1]==shape and GameBoard.board[2]==shape:
        button_number(0,"W")
        button_number(1,"I")
        button_number(2,"N")
    elif GameBoard.board[3] == shape and GameBoard.board[4] == shape and GameBoard.board[5] == shape:
        button_number(3, "W")
        button_number(4, "I")
        button_number(5, "N")
    elif GameBoard.board[6] == shape and GameBoard.board[7] == shape and GameBoard.board[8] == shape:
        button_number(6, "W")
        button_number(7, "I")
        button_number(8, "N")
    elif GameBoard.board[0] == shape and GameBoard.board[3] == shape and GameBoard.board[6] == shape:
        button_number(0, "W")
        button_number(3, "I")
        button_number(6, "N")
    elif GameBoard.board[1] == shape and GameBoard.board[4] == shape and GameBoard.board[7] == shape:
        button_number(1, "W")
        button_number(4, "I")
        button_number(7, "N")
    elif GameBoard.board[2] == shape and GameBoard.board[5] == shape and GameBoard.board[8] == shape:
        button_number(2, "W")
        button_number(5, "I")
        button_number(8, "N")
    elif GameBoard.board[0] == shape and GameBoard.board[4] == shape and GameBoard.board[8] == shape:
        button_number(0, "W")
        button_number(4, "I")
        button_number(8, "N")
    elif GameBoard.board[2] == shape and GameBoard.board[4] == shape and GameBoard.board[6] == shape:
        button_number(2, "W")
        button_number(4, "I")
        button_number(6, "N")


button1 = Button(Board, text=" ", height = 2, width = 4, font=('CourierNew 30 bold'), bg="light gray",
                 command = lambda:click(button1,1))
button1.grid(row=1, column=0)

button2 = Button(Board, text=" ", height = 2, width = 4, font=('CourierNew 30 bold'), bg="light gray",
                 command = lambda:click(button2,2))
button2.grid(row=1, column=1)

button3 = Button(Board, text=" ", height = 2, width = 4, font=('CourierNew 30 bold'), bg="light gray",
                 command = lambda:click(button3,3))
button3.grid(row=1, column=2)

button4 = Button(Board, text=" ", height = 2, width = 4, font=('CourierNew 30 bold'), bg="light gray",
                 command = lambda:click(button4,4))
button4.grid(row=2, column=0)

button5 = Button(Board, text=" ", height = 2, width = 4, font=('CourierNew 30 bold'), bg="light gray",
                 command = lambda:click(button5,5))
button5.grid(row=2, column=1)

button6 = Button(Board, text=" ", height = 2, width = 4, font=('CourierNew 30 bold'), bg="light gray",
                 command = lambda:click(button6,6))
button6.grid(row=2, column=2)

button7 = Button(Board, text=" ", height = 2, width = 4, font=('CourierNew 30 bold'), bg="light gray",
                 command = lambda:click(button7,7))
button7.grid(row=3, column=0)

button8 = Button(Board, text=" ", height = 2, width = 4, font=('CourierNew 30 bold'), bg="light gray",
                 command = lambda:click(button8,8))
button8.grid(row=3, column=1)

button9 = Button(Board, text=" ", height = 2, width = 4, font=('CourierNew 30 bold'), bg="light gray",
                 command = lambda:click(button9,9))
button9.grid(row=3, column=2)



root.mainloop()