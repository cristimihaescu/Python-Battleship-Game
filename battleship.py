# from random import randint

# initializing board
import msvcrt


def get_size():
    board = []

    board_size = input("Choose board size: ")
    try:
        board_size = int(board_size)
    except ValueError or TypeError:
        print("The input has to consist of an integer between 5 and 10 !")
        return get_size()
    # finally:
    #     board_size = int(board_size)
    print()

    for x in range(board_size):
        board.append(["O"] * board_size)

    if board_size > 10:
        print("Invalid input !")
        return get_size()

    return board, board_size


def print_board(board, board_size):
    numbers_list = list(range(1, 27))
    print("    ", end='')

    for number in numbers_list:
        print(number, end=' ')
        if number >= board_size:
            break

    print('\n')
    row_counter = 0
    for row in board:
        print(chr(row_counter+65), end='   ')
        row_counter += 1
        print(" ".join(row))


def ship_placement(board, alphabet_letters):
    placement = input("Please select a position for your ship ! Row first and column second !")
    coordinate_number = placement[1]
    if len(placement) == 3:
        coordinate_number = coordinate_number + placement[2]
    counter_letter = -1
    for letter in alphabet_letters:
        counter_letter += 1
        if placement[0].casefold() == letter.casefold():
            for index, number in enumerate(board[counter_letter]):
                if int(coordinate_number)-1 == index:

                    an_occupied_space = False
                    try:
                        if board[counter_letter][index+1] == 'O':
                            pass
                        else:
                            an_occupied_space = True
                    except IndexError:
                        pass

                    try:
                        if board[counter_letter][index-1] == 'O':
                            pass
                        else:
                            an_occupied_space = True
                    except IndexError:
                        pass

                    try:
                        if board[counter_letter+1][index] == 'O':
                            pass
                        else:
                            an_occupied_space = True
                    except IndexError:
                        pass

                    try:
                        if board[counter_letter-1][index] == 'O':
                            pass
                        else:
                            an_occupied_space = True
                    except IndexError:
                        pass

                    if an_occupied_space is False:
                        board[counter_letter][index] = "X"
                        return
                    else:
                        print("Ships are too close !")
                        ship_placement(board, alphabet_letters)


def ship_size(player, board, alphabet_letters, board_size):
    ships_size = [1, 1, 1, 1]
    ships_size_counter = 0
    for size in ships_size:
        ships_size_counter += 1
        if size == 1:
            print_board(board, board_size)
            if player == 1:
                print("\nIt's Player's 1 turn!")
            if player == 2:
                print("\nIt's Player's 2 turn!")
            if ships_size_counter == 1:
                print(f"\nChoose your {ships_size_counter}st ship !\n")
            if ships_size_counter == 2:
                print(f"\nChoose your {ships_size_counter}nd ship !\n")
            if ships_size_counter == 3:
                print(f"\nChoose your {ships_size_counter}rd ship !\n")
            if ships_size_counter == 4:
                print(f"\nChoose your {ships_size_counter}th ship !\n")
            ship_placement(board, alphabet_letters)
        else:
            print("The max ship size can only be 1 !")
    print("\nNext player's placement phase ! Press any key to continue\n")
    msvcrt.getch()


def alphabet_letters_get(board):
    alphabet_letters = []
    row_counter = 0
    for row in board:
        alphabet_letters.append(chr(row_counter + 65))
        row_counter += 1
    return alphabet_letters


def which_player(counter):
    counter += 1
    if counter % 2 == 0:
        return 1, counter
    if counter % 2 != 0:
        return 2, counter

def main():
    lets_play = "Let's play Battleship!"
    print("\n", lets_play, "\n")

    board, board_size = get_size()
    pre_game_preparation = True
    alphabet_letters = alphabet_letters_get(board)
    pre_game_counter = -1

    while pre_game_preparation:

        player, pre_game_counter = which_player(pre_game_counter)

        if pre_game_counter == 2:
            print("It's time for battle !")
            pre_game_preparation = False
            break

        ship_size(player, board, alphabet_letters, board_size)
        if player == 0:
            board_player1 = board
        if player == 1:
            board_player2 = board
        # print_board(board, board_size)
    print(alphabet_letters)


if __name__ == "__main__":
    main()
