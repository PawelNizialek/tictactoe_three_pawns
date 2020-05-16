import time
import boardclass as bc
import notification as no
from tkinter import *

update = 0
place_delete = 0
game_run = 0
pawns_limit = 0
time_checker = 0
GameBoard = bc.Board()
GameBoardCopy = bc.Board()
shape_tab = []
computer_shape = 'O'
player_shape = 'X'
level = 0

root = Tk()
root.resizable(False, False)
Main = Frame(root, width=400, height=300)
Main.grid(row=1, column=0)
Top = Frame(root, width=100, height=1)
Top.grid(row=0, column=0)
Board = Frame(Main, width=4000, heigh=3000)
Board.pack(side=LEFT)


def click(buttons, number):
    if game_run:
        global update
        global place_delete
        player(number)
        if update:
            update = 0
            place_delete = 0
            buttons["text"] = player_shape
            computer()
        if win() == -1:
            win_signal(player_shape)
        if win() == 1:
            win_signal(computer_shape)


def win():
    for i in range(9):
        GameBoardCopy.board[i] = GameBoard.board[i]
    return GameBoard.win_checker(player_shape, computer_shape)


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
            update = 1
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
                    button_number_changer(move, ' ')
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


def button_number_changer(number_to_change, shape):
    if number_to_change == 0:
        button1['text'] = shape
    elif number_to_change == 1:
        button2['text'] = shape
    elif number_to_change == 2:
        button3['text'] = shape
    elif number_to_change == 3:
        button4['text'] = shape
    elif number_to_change == 4:
        button5['text'] = shape
    elif number_to_change == 5:
        button6['text'] = shape
    elif number_to_change == 6:
        button7['text'] = shape
    elif number_to_change == 7:
        button8['text'] = shape
    elif number_to_change == 8:
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
        seconds_to_check = 0.5
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
        button_number_changer(best_place_to_remove, ' ')
        GameBoard.board[move] = computer_shape
        button_number_changer(move, computer_shape)

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
        button_number_changer(move, computer_shape)

    for j in range(len(shape_tab)):
        del shape_tab[0]


def win_signal(shape):
    global game_run
    if GameBoard.board[0] == shape and GameBoard.board[1] == shape and GameBoard.board[2] == shape:
        button1.configure(fg='red')
        button2.configure(fg='red')
        button3.configure(fg='red')
    elif GameBoard.board[3] == shape and GameBoard.board[4] == shape and GameBoard.board[5] == shape:
        button4.configure(fg='red')
        button5.configure(fg='red')
        button6.configure(fg='red')
    elif GameBoard.board[6] == shape and GameBoard.board[7] == shape and GameBoard.board[8] == shape:
        button7.configure(fg='red')
        button8.configure(fg='red')
        button9.configure(fg='red')
    elif GameBoard.board[0] == shape and GameBoard.board[3] == shape and GameBoard.board[6] == shape:
        button1.configure(fg='red')
        button4.configure(fg='red')
        button7.configure(fg='red')
    elif GameBoard.board[1] == shape and GameBoard.board[4] == shape and GameBoard.board[7] == shape:
        button2.configure(fg='red')
        button5.configure(fg='red')
        button8.configure(fg='red')
    elif GameBoard.board[2] == shape and GameBoard.board[5] == shape and GameBoard.board[8] == shape:
        button3.configure(fg='red')
        button6.configure(fg='red')
        button9.configure(fg='red')
    elif GameBoard.board[0] == shape and GameBoard.board[4] == shape and GameBoard.board[8] == shape:
        button1.configure(fg='red')
        button5.configure(fg='red')
        button9.configure(fg='red')
    elif GameBoard.board[2] == shape and GameBoard.board[4] == shape and GameBoard.board[6] == shape:
        button3.configure(fg='red')
        button5.configure(fg='red')
        button7.configure(fg='red')
    game_run = 0


button1 = Button(Board, text=" ", height=1, width=3, font=('CourierNew 30 bold'), bg="light gray",
                 command=lambda: click(button1, 1))
button1.grid(row=2, column=0)
button2 = Button(Board, text=" ", height=1, width=3, font=('CourierNew 30 bold'), bg="light gray",
                 command=lambda: click(button2, 2))
button2.grid(row=2, column=1)

button3 = Button(Board, text=" ", height=1, width=3, font=('CourierNew 30 bold'), bg="light gray",
                 command=lambda: click(button3, 3))
button3.grid(row=2, column=2)

button4 = Button(Board, text=" ", height=1, width=3, font=('CourierNew 30 bold'), bg="light gray",
                 command=lambda: click(button4, 4))
button4.grid(row=3, column=0)

button5 = Button(Board, text=" ", height=1, width=3, font=('CourierNew 30 bold'), bg="light gray",
                 command=lambda: click(button5, 5))
button5.grid(row=3, column=1)

button6 = Button(Board, text=" ", height=1, width=3, font=('CourierNew 30 bold'), bg="light gray",
                 command=lambda: click(button6, 6))
button6.grid(row=3, column=2)

button7 = Button(Board, text=" ", height=1, width=3, font=('CourierNew 30 bold'), bg="light gray",
                 command=lambda: click(button7, 7))
button7.grid(row=4, column=0)

button8 = Button(Board, text=" ", height=1, width=3, font=('CourierNew 30 bold'), bg="light gray",
                 command=lambda: click(button8, 8))
button8.grid(row=4, column=1)

button9 = Button(Board, text=" ", height=1, width=3, font=('CourierNew 30 bold'), bg="light gray",
                 command=lambda: click(button9, 9))
button9.grid(row=4, column=2)


def reset():
    global place_delete
    global pawns_limit
    global game_run
    game_run = 1
    pawns_limit = 0
    place_delete = 0
    button_number_changer(0, " ")
    button_number_changer(1, " ")
    button_number_changer(2, " ")
    button_number_changer(3, " ")
    button_number_changer(4, " ")
    button_number_changer(5, " ")
    button_number_changer(6, " ")
    button_number_changer(7, " ")
    button_number_changer(8, " ")
    button1.configure(fg='black')
    button2.configure(fg='black')
    button3.configure(fg='black')
    button4.configure(fg='black')
    button5.configure(fg='black')
    button6.configure(fg='black')
    button7.configure(fg='black')
    button8.configure(fg='black')
    button9.configure(fg='black')
    for i in range(9):
        GameBoard.board[i] = " "


def main(shape_number, level_number):
    global player_shape
    global computer_shape
    global level
    reset()
    if level_number.get() == 1:
        level = 0
    elif level_number.get() == 2:
        level = 1
    if shape_number.get() == 1:
        player_shape = "X"
        computer_shape = "O"
    if shape_number.get() == 2:
        player_shape = "O"
        computer_shape = "X"


level_number = IntVar()
shape_number = IntVar()
level_number.set(2)
shape_number.set(1)

menubar = Menu(Top)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit())
menubar.add_cascade(label="File", menu=file_menu)
game_menu = Menu(menubar, tearoff=0)
game_menu.add_command(label="StartGame", command=lambda: main(shape_number, level_number))
submenu = Menu(file_menu, tearoff=0)
game_menu2 = Menu(game_menu, tearoff=0)
game_menu3 = Menu(game_menu, tearoff=0)
game_menu2.add_radiobutton(label="Easy", variable=level_number, value=1)
game_menu2.add_radiobutton(label="Hard", variable=level_number, value=2)
game_menu3.add_radiobutton(label="X", variable=shape_number, value=1)
game_menu3.add_radiobutton(label="O", variable=shape_number, value=2)
game_menu.add_cascade(label="Level", menu=game_menu2)
game_menu.add_cascade(label="Shape", menu=game_menu3)
menubar.add_cascade(label="Game", menu=game_menu)

root.config(menu=menubar)

root.mainloop()
