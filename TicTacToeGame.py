from itertools import cycle
from colorama import init, Fore, Style
init()


def game_board(game_map, player=0, row=0, col=0, just_display=False):
    try:
        if(game_map[row][col] != 0):
            print("This position is occupied ! Please choose another ...")
            return game_map, False

        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][col] = player

        for count, row in enumerate(game_map):
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.MAGENTA + ' O ' + Style.RESET_ALL
            print(count, colored_row)

        return game_map, True
    except IndexError as e:
        print("Error! make sure you input row/columns as 0 1 or 2? ", e)
        return game_map, False

    except Exception as e:
        print("Error! something went wrong! ", e)
        return game_map, False


def win(current_game):

    def all_same(l):
        if(l.count(l[0]) == len(l) and l[0]) != 0:
            return True
        else:
            return False

    # Determine horizontal winner
    for row in current_game:
        # print(row)
        if(all_same(row)):
            print(f"Player {row[0]} is the winner horizontally (-)")
            return True

    # Determine vertical winner
    for col in range(len(current_game)):
        check = []
        for row in current_game:
            check.append(row[col])

        # print(check)

        if(all_same(check)):
            print(f"Player {check[0]} is the winner vertically (|)")
            return True

    # Determine diagonal winner
    # Direction "\"
    diags = []
    for idx in range(len(current_game)):
        diags.append(current_game[idx][idx])

    # print(diags)

    if(all_same(diags)):
        print(f"Player {diags[0]} is the winner diagonally (\\)")
        return True

    # Direction "/"
    diags = []
    # cols = list(reversed(range(len(current_game))))
    # rows = list(range(len(current_game)))
    # print(cols)
    # print(rows)

    '''for col, row in zip(cols, rows):
        diags.append(current_game[col][row])
    '''
    for col, row in enumerate(reversed(range(len(current_game)))):
        # print(col, row)
        diags.append(current_game[row][col])

    # print(diags)

    if(all_same(diags)):
        print(f"Player {diags[0]} is the winner diagonally (/)")
        return True

    return False


play = True
while play:

    game_size = int(input("What size of tic tac toe game you want to play? : "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]

    game_won = False
    player_choice = cycle([1, 2])
    game, _ = game_board(game, just_display=True)
    while not game_won:
        current_player = next(player_choice)
        print(f"Current player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("What column do you want to play? (0, 1, 2): "))
            row_choice = int(input("What row do you want to play? (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("Would you like to play again? (y/n): ")
            if again.lower() == "y":
                print("Restarting!")
            elif again.lower() == "n":
                print("Byeeeee")
                play = False
            else:
                print("Not a valid choice! See you later... aligator ;) ")
                play = False