import time
import tkinter as tk
import boardclass as bc

NUMBER_OF_BUTTONS = 9
TIME_TO_THINK = 7.2
TIME_TO_THINK_EASY_MED = 0.1
BEST_MOVE_MAX_SCORE = 10
BEST_MOVE_MIN_SCORE = -10
NUMBER_OF_BUTTONS_TO_WIN = 3
EASY = 1
MEDIUM = 2
HARD = 3
CHECKED_FIELDS = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                  (0, 3, 6), (1, 4, 7), (2, 5, 8),
                  (0, 4, 8), (2, 4, 6), ]
POSSIBILITIES_OF_WINNING = 8

GameBoard = bc.Board()
GameBoardCopy = bc.Board()


def click(number, button_list, shape_tab):
    """
    Reakcja na naciśnięty przycisk.
    """
    if GameBoard.game_run:
        player(number, button_list)
        if GameBoard.move:
            GameBoard.move = 0
            GameBoard.field_delete = 0
            button_number_changer(number - 1, GameBoard.player_shape, "royal blue", button_list)
            if win() == -1:
                win_signal(GameBoard.player_shape, button_list)
            elif win() == 1:
                win_signal(GameBoard.computer_shape, button_list)
            else:
                computer(button_list, shape_tab)
        if win() == -1:
            win_signal(GameBoard.player_shape, button_list)
        elif win() == 1:
            win_signal(GameBoard.computer_shape, button_list)


def win():
    """
        Sprawdzenie wygranej.
    """
    for i in range(NUMBER_OF_BUTTONS):
        GameBoardCopy.board[i] = GameBoard.board[i]
    return GameBoard.win_checker(GameBoard.player_shape, GameBoard.computer_shape)


def shape_tab_edit(button_number, shape, shape_tab):
    """
        Zwraca indeks listy przechowującej pionki gracza lub komputera.
    """
    for _ in range(len(shape_tab)):
        del shape_tab[0]
    for k in range(NUMBER_OF_BUTTONS):
        if GameBoardCopy.board[k] == shape:
            shape_tab.append(k)
    return shape_tab[button_number]


def player(number, button_list):
    """
        Odpowiada za możliwość poprawnego ruchu gracza.
    """
    if GameBoard.pawns_limit_on_board == 0:
        move = int(number)
        move = move - 1
        if move in range(0, NUMBER_OF_BUTTONS):
            if GameBoard.board[move] == GameBoard.computer_shape \
                    or GameBoard.board[move] == GameBoard.player_shape:
                return 0
            GameBoard.board[move] = GameBoard.player_shape
            GameBoard.move = 1
        else:
            return 0
    else:
        if GameBoard.field_delete == 0:
            move = int(number)
            move = move - 1
            if move in range(0, NUMBER_OF_BUTTONS):
                if GameBoard.board[move] == GameBoard.player_shape and GameBoard.field_delete == 0:
                    GameBoard.board[move] = ' '
                    button_number_changer(move, ' ', 'midnight blue', button_list)
                    GameBoard.field_delete = 1
            return 0

        move = number
        move = move - 1
        if move in range(0, NUMBER_OF_BUTTONS):
            if GameBoard.board[move] == GameBoard.computer_shape \
                    or GameBoard.board[move] == GameBoard.player_shape:
                return 0
            GameBoard.board[move] = GameBoard.player_shape
            GameBoard.move = 1
        return 0


def button_number_changer(number_to_change, shape, color, button_list):
    """
        Zmiana wyswietlanego tekstu na przycisku.
    """
    button_list[number_to_change].configure(fg=color)
    button_list[number_to_change]['text'] = shape


def minmax(depth=0, max_min=1):
    """
        Zwraca indeks najlepszego posunięcia dla komputera.
    """
    result = GameBoardCopy.win_checker(GameBoard.player_shape, GameBoard.computer_shape)
    if result is not None:
        return result
    if max_min:
        best_score = BEST_MOVE_MIN_SCORE
        for i in range(NUMBER_OF_BUTTONS):
            if GameBoardCopy.board[i] == " ":
                GameBoardCopy.board[i] = GameBoard.computer_shape
                score = minmax(depth + 1, 0)
                GameBoardCopy.board[i] = " "
                if best_score < score:
                    best_score = score
        return best_score
    else:
        best_score = BEST_MOVE_MAX_SCORE
        for i in range(NUMBER_OF_BUTTONS):
            if GameBoardCopy.board[i] == ' ':
                GameBoardCopy.board[i] = GameBoard.player_shape
                score = minmax(depth + 1, 1)
                GameBoardCopy.board[i] = ' '
                if best_score > score:
                    best_score = score
        return best_score


def minmax_for_three_pawns(min_max_time, shape_tab, depth=0, max=1, place_number=0):
    """
        Zwraca indeks najlepszego posunięcia komputera, gdy na planszy są po trzy pionki każdej ze stron.
    """
    time_start_min_max = min_max_time
    pawn_to_remove = place_number
    result = GameBoardCopy.win_checker(GameBoard.player_shape, GameBoard.computer_shape)
    if result is not None:
        return result
    if GameBoard.level == EASY:
        seconds_to_check = TIME_TO_THINK_EASY_MED
        if depth == 0:
            return 0
    if GameBoard.level == MEDIUM:
        seconds_to_check = TIME_TO_THINK_EASY_MED
        if depth == 1:
            return 0
    else:
        seconds_to_check = TIME_TO_THINK
        if depth == 4:
            return 0

    if time.time() - time_start_min_max > seconds_to_check / NUMBER_OF_BUTTONS:
        return 0

    if max:
        best_score = BEST_MOVE_MIN_SCORE
        for i in range(NUMBER_OF_BUTTONS):
            if GameBoardCopy.board[i] == " ":
                for j in range(NUMBER_OF_BUTTONS_TO_WIN):
                    index = shape_tab_edit(j, GameBoard.computer_shape, shape_tab)
                    GameBoardCopy.board[index] = " "
                    GameBoardCopy.board[i] = GameBoard.computer_shape

                    score = minmax_for_three_pawns(time_start_min_max, shape_tab, depth + 1, 0, pawn_to_remove)

                    GameBoardCopy.board[index] = GameBoard.computer_shape
                    GameBoardCopy.board[i] = " "

                    if best_score < score:
                        best_score = score

        return best_score

    else:

        best_score = BEST_MOVE_MAX_SCORE
        for i in range(NUMBER_OF_BUTTONS):
            if GameBoardCopy.board[i] == ' ':
                for j in range(NUMBER_OF_BUTTONS_TO_WIN):
                    index = shape_tab_edit(j, GameBoard.player_shape, shape_tab)
                    GameBoardCopy.board[index] = " "
                    GameBoardCopy.board[i] = GameBoard.player_shape

                    score = minmax_for_three_pawns(time_start_min_max, shape_tab, depth + 1, 1, pawn_to_remove)

                    GameBoardCopy.board[index] = GameBoard.player_shape
                    GameBoardCopy.board[i] = " "

                    if best_score > score:
                        best_score = score

        return best_score


def computer(button_list, shape_tab):
    """
        Odpowiada za właściwy ruch komputera.
    """
    for i in range(NUMBER_OF_BUTTONS):
        GameBoardCopy.board[i] = GameBoard.board[i]
    best_place_to_remove = 0
    best_score = BEST_MOVE_MIN_SCORE
    points = -1
    move = 0
    for i in range(NUMBER_OF_BUTTONS):
        if GameBoardCopy.board[i] == GameBoard.computer_shape:
            shape_tab.append(i)

    if len(shape_tab) > 1:
        GameBoard.pawns_limit_on_board = 1

    if len(shape_tab) > 2:
        for i in range(NUMBER_OF_BUTTONS):
            if GameBoardCopy.board[i] == " ":
                for computer_shape_number in range(NUMBER_OF_BUTTONS_TO_WIN):
                    remove = shape_tab_edit(computer_shape_number, GameBoard.computer_shape, shape_tab)
                    GameBoardCopy.board[remove] = ' '
                    GameBoardCopy.board[i] = GameBoard.computer_shape

                    min_max_time = time.time()
                    points = minmax_for_three_pawns(min_max_time, shape_tab, 0, 0, computer_shape_number)

                    GameBoardCopy.board[remove] = GameBoard.computer_shape
                    GameBoardCopy.board[i] = ' '

                    if best_score <= points:
                        best_score = points
                        best_place_to_remove = remove
                        move = i

                if points == 1:
                    break

        GameBoard.board[best_place_to_remove] = ' '
        button_number_changer(best_place_to_remove, ' ', 'indian red', button_list)
        GameBoard.board[move] = GameBoard.computer_shape
        button_number_changer(move, GameBoard.computer_shape, 'indian red', button_list)

    else:
        for i in range(NUMBER_OF_BUTTONS):
            if GameBoardCopy.board[i] == " ":
                GameBoardCopy.board[i] = GameBoard.computer_shape

                points = minmax(0, 0)
                GameBoardCopy.board[i] = ' '

                if best_score <= points:
                    best_score = points
                    move = i
        GameBoard.board[move] = GameBoard.computer_shape
        button_number_changer(move, GameBoard.computer_shape, 'indian red', button_list)

    for _ in shape_tab:
        del shape_tab[0]


def win_signal(shape, button_list):
    """
        Sprawdzenie, które pionki są wygrywające.
        Zaznaczenie wygranej.
        Reset ustawień.
    """
    win_list = (0, 0, 0)
    for i in range(POSSIBILITIES_OF_WINNING):
        for j in range(NUMBER_OF_BUTTONS_TO_WIN):
            if GameBoard.board[CHECKED_FIELDS[i][j]] == shape:
                pass
            else:
                break
            if j == 2:
                win_list = CHECKED_FIELDS[i]

    for i in range(NUMBER_OF_BUTTONS_TO_WIN):
        button_list[win_list[i]].configure(fg='dark green')

    GameBoard.game_run = 0


def reset(button_list):
    """
        Reset ustawień.
    """
    GameBoard.game_run = 1
    GameBoard.pawns_limit_on_board = 0
    GameBoard.field_delete = 0

    for i in range(NUMBER_OF_BUTTONS):
        button_number_changer(i, " ", 'midnight blue', button_list)
        button_list[i].configure(fg='midnight blue')
        GameBoard.board[i] = " "


def set_game(shape_number, level_number, button_list):
    """
        Reset ustawień.
        Ustawienie poziomu trudności.
        Ustawienie kształtu.
    """
    reset(button_list)
    if level_number.get() == EASY:
        GameBoard.level = EASY
    elif level_number.get() == MEDIUM:
        GameBoard.level = MEDIUM
    elif level_number.get() == HARD:
        GameBoard.level = HARD
    if shape_number.get() == 1:
        GameBoard.player_shape = "X"
        GameBoard.computer_shape = "O"
    if shape_number.get() == 2:
        GameBoard.player_shape = "O"
        GameBoard.computer_shape = "X"


def show_boardgame(button_list, shape_tab):
    """
            Wyświetlanie okienka z grą.
    """
    root = tk.Tk()
    root.resizable(False, False)
    root.title("3pawns tictactoe")
    Main = tk.Frame(root, width=400, height=300)
    Main.grid(row=1, column=0)
    Top = tk.Frame(root, width=100, height=1)
    Top.grid(row=0, column=0)
    Board = tk.Frame(Main, width=4000, heigh=3000)
    Board.pack(side=tk.LEFT)
    row_number = 2
    column_number = 0
    for i in range(9):
        button_list.append(tk.Button(Board, text=" ", height=1, width=3,
                                     font='CourierNew 30 bold', bg="light grey",
                                     command=lambda i=i: click(i + 1, button_list, shape_tab)))
        button_list[i].grid(row=row_number, column=column_number)
        column_number += 1

        if i == 2:
            column_number = 0
            row_number = 3
        elif i == 5:
            column_number = 0
            row_number = 4

    level_number = tk.IntVar()
    shape_number = tk.IntVar()
    level_number.set(HARD)
    shape_number.set(1)

    menubar = tk.Menu(Top)
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=file_menu)
    game_menu = tk.Menu(menubar, tearoff=0)
    game_menu.add_command(label="StartGame", command=lambda: set_game(shape_number, level_number, button_list))
    game_menu2 = tk.Menu(game_menu, tearoff=0)
    game_menu3 = tk.Menu(game_menu, tearoff=0)
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


def main():
    button_list = []
    shape_tab = []
    show_boardgame(button_list, shape_tab)


if __name__ == '__main__':
    main()
