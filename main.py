import time
import boardclass as bc
from tkinter import *

NUMBER_OF_BUTTONS = 9
TIME_TO_THINK = 7.2
TIME_TO_THINK_EASY_MED = 0.1
BEST_MOVE_MAX_SCORE = 10
BEST_MOVE_MIN_SCORE = -10
NUMBER_OF_BUTTONS_TO_WIN = 3
EASY = 1
MEDIUM = 2
HARD = 3

GameBoard = bc.Board()
GameBoardCopy = bc.Board()
root = Tk()
root.resizable(False, False)
root.title("3pawns tictactoe")
Main = Frame(root, width=400, height=300)
Main.grid(row=1, column=0)
Top = Frame(root, width=100, height=1)
Top.grid(row=0, column=0)
Board = Frame(Main, width=4000, heigh=3000)
Board.pack(side=LEFT)


def click(buttons, number):
    if bc.Board.game_run:
        player(number)
        if bc.Board.update:
            bc.Board.update = 0
            bc.Board.place_delete = 0
            buttons["text"] = bc.Board.player_shape
            if win() == -1:
                win_signal(bc.Board.player_shape)
                return 0
            elif win() == 1:
                win_signal(bc.Board.computer_shape)
                return 0
            else:
                computer()
        if win() == -1:
            win_signal(bc.Board.player_shape)
        elif win() == 1:
            win_signal(bc.Board.computer_shape)


def win():
    for i in range(NUMBER_OF_BUTTONS):
        GameBoardCopy.board[i] = GameBoard.board[i]
    return GameBoard.win_checker(bc.Board.player_shape, bc.Board.computer_shape)


def shape_tab_edit(it, shape):
    for j in range(len(bc.Board.shape_tab)):
        del bc.Board.shape_tab[0]
    for k in range(NUMBER_OF_BUTTONS):
        if GameBoardCopy.board[k] == shape:
            bc.Board.shape_tab.append(k)
    return bc.Board.shape_tab[it]


def player(number):
    if bc.Board.pawns_limit == 0:
        move = int(number)
        move = move - 1
        if move in range(0, NUMBER_OF_BUTTONS):
            if GameBoard.board[move] == bc.Board.computer_shape or GameBoard.board[move] == bc.Board.player_shape:
                return 0
            GameBoard.board[move] = bc.Board.player_shape
            bc.Board.update = 1
        else:
            return 0
    else:
        if bc.Board.place_delete == 0:
            move = int(number)
            move = move - 1
            if move in range(0, NUMBER_OF_BUTTONS):
                if GameBoard.board[move] == bc.Board.computer_shape:
                    return 0
                if GameBoard.board[move] == ' ':
                    return 0
                if GameBoard.board[move] == bc.Board.player_shape and bc.Board.place_delete == 0:
                    GameBoard.board[move] = ' '
                    button_number_changer(move, ' ')
                    bc.Board.place_delete = 1
                    return 0
            else:
                return 0

        move = number
        move = move - 1
        if move in range(0, NUMBER_OF_BUTTONS):
            if GameBoard.board[move] == bc.Board.computer_shape or GameBoard.board[move] == bc.Board.player_shape:
                return 0
            GameBoard.board[move] = bc.Board.player_shape
            bc.Board.update = 1


def button_number_changer(number_to_change, shape):
    bc.Board.button_list[number_to_change]['text'] = shape
    pass


def minmax(depth=0, max_min=1):
    result = GameBoardCopy.win_checker(bc.Board.player_shape, bc.Board.computer_shape)
    if result is not None:
        return result
    if max_min:
        best_score = BEST_MOVE_MIN_SCORE
        for i in range(NUMBER_OF_BUTTONS):
            if GameBoardCopy.board[i] == " ":
                GameBoardCopy.board[i] = bc.Board.computer_shape
                score = minmax(depth + 1, 0)
                GameBoardCopy.board[i] = " "
                if best_score < score:
                    best_score = score
        return best_score
    else:
        best_score = BEST_MOVE_MAX_SCORE
        for i in range(NUMBER_OF_BUTTONS):
            if GameBoardCopy.board[i] == ' ':
                GameBoardCopy.board[i] = bc.Board.player_shape
                score = minmax(depth + 1, 1)
                GameBoardCopy.board[i] = ' '
                if best_score > score:
                    best_score = score
        return best_score


def minmax_for_three_pawns(min_max_time, depth=0, max=1, it=0):
    time_start_algorithm = min_max_time
    pawn_to_remove = it
    result = GameBoardCopy.win_checker(bc.Board.player_shape, bc.Board.computer_shape)
    if result is not None:
        return result
    if bc.Board.level == EASY:
        seconds_to_check = TIME_TO_THINK_EASY_MED
        if depth == 0:
            return 0
    if bc.Board.level == MEDIUM:
        seconds_to_check = TIME_TO_THINK_EASY_MED
        if depth == 1:
            return 0
    else:
        seconds_to_check = TIME_TO_THINK
        if depth == 4:
            return 0

    if time.time() - time_start_algorithm > seconds_to_check / NUMBER_OF_BUTTONS:
        return 0

    if max:
        best_score = BEST_MOVE_MIN_SCORE
        for i in range(NUMBER_OF_BUTTONS):
            if GameBoardCopy.board[i] == " ":
                for h in range(NUMBER_OF_BUTTONS_TO_WIN):
                    u = shape_tab_edit(h, bc.Board.computer_shape)
                    GameBoardCopy.board[u] = " "
                    GameBoardCopy.board[i] = bc.Board.computer_shape

                    score = minmax_for_three_pawns(time_start_algorithm, depth + 1, 0, pawn_to_remove)

                    GameBoardCopy.board[u] = bc.Board.computer_shape
                    GameBoardCopy.board[i] = " "

                    if best_score < score:
                        best_score = score

        return best_score

    else:

        best_score = BEST_MOVE_MAX_SCORE
        for i in range(NUMBER_OF_BUTTONS):
            if GameBoardCopy.board[i] == ' ':
                for g in range(NUMBER_OF_BUTTONS_TO_WIN):
                    u = shape_tab_edit(g, bc.Board.player_shape)
                    GameBoardCopy.board[u] = " "
                    GameBoardCopy.board[i] = bc.Board.player_shape

                    score = minmax_for_three_pawns(time_start_algorithm, depth + 1, 1, pawn_to_remove)

                    GameBoardCopy.board[u] = bc.Board.player_shape
                    GameBoardCopy.board[i] = " "

                    if best_score > score:
                        best_score = score

        return best_score


def computer():
    for i in range(NUMBER_OF_BUTTONS):
        GameBoardCopy.board[i] = GameBoard.board[i]
    #bc.Board.time_checker = 0
    best_place_to_remove = 0
    best_score = BEST_MOVE_MIN_SCORE
    points = -1
    move = 0
    for i in range(NUMBER_OF_BUTTONS):
        if GameBoardCopy.board[i] == bc.Board.computer_shape:
            bc.Board.shape_tab.append(i)

    if len(bc.Board.shape_tab) > 1:
        bc.Board.pawns_limit = 1

    if len(bc.Board.shape_tab) > 2:
        for i in range(NUMBER_OF_BUTTONS):
            if GameBoardCopy.board[i] == " ":
                for computer_shape_number in range(NUMBER_OF_BUTTONS_TO_WIN):
                    remove = shape_tab_edit(computer_shape_number, bc.Board.computer_shape)
                    GameBoardCopy.board[remove] = ' '
                    GameBoardCopy.board[i] = bc.Board.computer_shape

                    min_max_time = time.time()
                    points = minmax_for_three_pawns(min_max_time, 0, 0, computer_shape_number)

                    GameBoardCopy.board[remove] = bc.Board.computer_shape
                    GameBoardCopy.board[i] = ' '

                    if best_score <= points:
                        best_score = points
                        best_place_to_remove = remove
                        move = i

                if points == 1:
                    break

        GameBoard.board[best_place_to_remove] = ' '
        button_number_changer(best_place_to_remove, ' ')
        GameBoard.board[move] = bc.Board.computer_shape
        button_number_changer(move, bc.Board.computer_shape)

    else:
        for i in range(NUMBER_OF_BUTTONS):
            if GameBoardCopy.board[i] == " ":
                GameBoardCopy.board[i] = bc.Board.computer_shape

                points = minmax(0, 0)
                GameBoardCopy.board[i] = ' '

                if best_score <= points:
                    best_score = points
                    move = i
        GameBoard.board[move] = bc.Board.computer_shape
        button_number_changer(move, bc.Board.computer_shape)

    for j in bc.Board.shape_tab:
        del bc.Board.shape_tab[0]


def win_signal(shape):
    win_list = (0, 0, 0)
    if GameBoard.board[0] == shape and GameBoard.board[1] == shape and GameBoard.board[2] == shape:
        win_list = (0, 1, 2)

    elif GameBoard.board[3] == shape and GameBoard.board[4] == shape and GameBoard.board[5] == shape:
        win_list = (3, 4, 5)

    elif GameBoard.board[6] == shape and GameBoard.board[7] == shape and GameBoard.board[8] == shape:
        win_list = (6, 7, 8)

    elif GameBoard.board[0] == shape and GameBoard.board[3] == shape and GameBoard.board[6] == shape:
        win_list = (0, 3, 6)

    elif GameBoard.board[1] == shape and GameBoard.board[4] == shape and GameBoard.board[7] == shape:
        win_list = (1, 4, 7)

    elif GameBoard.board[2] == shape and GameBoard.board[5] == shape and GameBoard.board[8] == shape:
        win_list = (2, 5, 8)

    elif GameBoard.board[0] == shape and GameBoard.board[4] == shape and GameBoard.board[8] == shape:
        win_list = (0, 4, 8)

    elif GameBoard.board[2] == shape and GameBoard.board[4] == shape and GameBoard.board[6] == shape:
        win_list = (2, 4, 6)
    for i in range(NUMBER_OF_BUTTONS_TO_WIN):
        bc.Board.button_list[win_list[i]].configure(fg='red')

    bc.Board.game_run = 0


bc.Board.button_list.append(Button(Board, text=" ", height=1, width=3, font='CourierNew 30 bold', bg="light gray",
                                   command=lambda: click(bc.Board.button_list[0], 1)))
bc.Board.button_list[0].grid(row=2, column=0)

bc.Board.button_list.append(Button(Board, text=" ", height=1, width=3, font='CourierNew 30 bold', bg="light gray",
                                   command=lambda: click(bc.Board.button_list[1], 2)))
bc.Board.button_list[1].grid(row=2, column=1)
bc.Board.button_list.append(Button(Board, text=" ", height=1, width=3, font='CourierNew 30 bold', bg="light gray",
                                   command=lambda: click(bc.Board.button_list[2], 3)))
bc.Board.button_list[2].grid(row=2, column=2)
bc.Board.button_list.append(Button(Board, text=" ", height=1, width=3, font='CourierNew 30 bold', bg="light gray",
                                   command=lambda: click(bc.Board.button_list[3], 4)))
bc.Board.button_list[3].grid(row=3, column=0)

bc.Board.button_list.append(Button(Board, text=" ", height=1, width=3, font='CourierNew 30 bold', bg="light gray",
                                   command=lambda: click(bc.Board.button_list[4], 5)))
bc.Board.button_list[4].grid(row=3, column=1)
bc.Board.button_list.append(Button(Board, text=" ", height=1, width=3, font='CourierNew 30 bold', bg="light gray",
                                   command=lambda: click(bc.Board.button_list[5], 6)))
bc.Board.button_list[5].grid(row=3, column=2)
bc.Board.button_list.append(Button(Board, text=" ", height=1, width=3, font='CourierNew 30 bold', bg="light gray",
                                   command=lambda: click(bc.Board.button_list[6], 7)))
bc.Board.button_list[6].grid(row=4, column=0)

bc.Board.button_list.append(Button(Board, text=" ", height=1, width=3, font='CourierNew 30 bold', bg="light gray",
                                   command=lambda: click(bc.Board.button_list[7], 8)))
bc.Board.button_list[7].grid(row=4, column=1)
bc.Board.button_list.append(Button(Board, text=" ", height=1, width=3, font='CourierNew 30 bold', bg="light gray",
                                   command=lambda: click(bc.Board.button_list[8], 9)))
bc.Board.button_list[8].grid(row=4, column=2)


def reset():
    bc.Board.game_run = 1
    bc.Board.pawns_limit = 0
    bc.Board.place_delete = 0

    for i in range(NUMBER_OF_BUTTONS):
        button_number_changer(i, " ")
        bc.Board.button_list[i].configure(fg='black')
        GameBoard.board[i] = " "


def main(shape_number, level_number):
    reset()
    if level_number.get() == EASY:
        bc.Board.level = EASY
    elif level_number.get() == MEDIUM:
        bc.Board.level = MEDIUM
    elif level_number.get() == HARD:
        bc.Board.level = HARD
    if shape_number.get() == 1:
        bc.Board.player_shape = "X"
        bc.Board.computer_shape = "O"
    if shape_number.get() == 2:
        bc.Board.player_shape = "O"
        bc.Board.computer_shape = "X"


level_number = IntVar()
shape_number = IntVar()
level_number.set(HARD)
shape_number.set(1)

menubar = Menu(Top)
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit())
menubar.add_cascade(label="File", menu=file_menu)

game_menu = Menu(menubar, tearoff=0)
game_menu.add_command(label="StartGame", command=lambda: main(shape_number, level_number))
game_menu2 = Menu(game_menu, tearoff=0)
game_menu3 = Menu(game_menu, tearoff=0)
game_menu2.add_radiobutton(label="Easy", variable=level_number, value=EASY)
game_menu2.add_radiobutton(label="Medium", variable=level_number, value=MEDIUM)
game_menu2.add_radiobutton(label="Hard", variable=level_number, value=HARD)
game_menu3.add_radiobutton(label="X", variable=shape_number, value=1)
game_menu3.add_radiobutton(label="O", variable=shape_number, value=2)
game_menu.add_cascade(label="Level", menu=game_menu2)
game_menu.add_cascade(label="Shape", menu=game_menu3)
menubar.add_cascade(label="Game", menu=game_menu)

root.config(menu=menubar)

root.mainloop()
