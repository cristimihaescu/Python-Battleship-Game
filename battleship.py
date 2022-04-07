# from random import randint
import copy
# initializing board
# import msvcrt


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


def ship_placement(board, alphabet_letters, boardp1, boardp2, player, size):
    while True:
        placement = input("Please select a position for your ship ! Row first and column second !")
        if (len(placement) == 1) or (len(placement) == 0):
            print("The coordinate is made out of 2 coordinates !")
            continue
        coordinate_number = placement[1]
        coordinate_letter = placement[0]
        if coordinate_number == '0':
            print("The number coordinate is out of range !")
            continue
        number_found = 0
        for letter in alphabet_letters:
            if coordinate_letter.lower() == letter.lower():
                number_found += 1
        if number_found == 0:
            print("The letter coordinate is out of range !")
            continue
        try:
            coordinate_number = int(coordinate_number)
        except ValueError:
            print("The second coordinate has to be a number !")
            continue

        if len(placement) == 3:
            third_coordinate = placement[2]
            try:
                third_coordinate = int(placement[2])
            except TypeError:
                print("The third coordinate has to be a number !")
                continue
            except ValueError:
                print("The third coordinate has to be a number !")
                continue

            coordinate_number = str(coordinate_number) + str(third_coordinate)
            if int(coordinate_number) > 10:
                print("The number coordinate is out of range !")
                continue

        if len(placement) > 3:
            print("Your input can be of maximum 3 characters !")
            continue

        counter_letter = -1
        for letter in alphabet_letters:
            counter_letter += 1
            if placement[0].casefold() == letter.casefold():
                for index, number in enumerate(board[counter_letter]):
                    if int(coordinate_number)-1 == index:

                        an_occupied_space = False
                        try:
                            if player == 1:
                                if boardp1[counter_letter][index+1] == "O":
                                    pass
                                else:
                                    an_occupied_space = True
                            if player == 2:
                                if boardp2[counter_letter][index+1] == "O":
                                    pass
                                else:
                                    an_occupied_space = True
                        except IndexError:
                            pass

                        try:
                            if player == 1:
                                if boardp1[counter_letter][index-1] == "O":
                                    pass
                                else:
                                    an_occupied_space = True
                            if player == 2:
                                if boardp2[counter_letter][index-1] == "O":
                                    pass
                                else:
                                    an_occupied_space = True
                        except IndexError:
                            pass

                        try:
                            if player == 1:
                                if boardp1[counter_letter+1][index] == "O":
                                    pass
                                else:
                                    an_occupied_space = True
                            if player == 2:
                                if boardp2[counter_letter+1][index] == "O":
                                    pass
                                else:
                                    an_occupied_space = True
                        except IndexError:
                            pass

                        try:
                            if player == 1:
                                if boardp1[counter_letter-1][index] == "O":
                                    pass
                                else:
                                    an_occupied_space = True
                            if player == 2:
                                if boardp2[counter_letter-1][index] == "O":
                                    pass
                                else:
                                    an_occupied_space = True

                        except IndexError:
                            pass

                        if player == 1:
                            if boardp1[counter_letter][index] == "X":
                                an_occupied_space = True

                        if player == 2:
                            if boardp2[counter_letter][index] == "X":
                                an_occupied_space = True

                        if an_occupied_space is False:
                            if player == 1:
                                if size == 1:
                                    boardp1[counter_letter][index] = "X"
                                    return boardp1
                                if size == 2:
                                    while True:
                                        orientation = input("Choose whether to put the ships vertically or horizontally ! ")
                                        second_x = False
                                        if orientation.lower() == "vertical" or orientation.lower() == "v":
                                            boardp1[counter_letter][index] = "X"
                                            if boardp1[counter_letter+2][index] == "X":
                                                second_x = True
                                            if boardp1[counter_letter+1][index+1] == "X":
                                                second_x = True
                                            if boardp1[counter_letter+1][index-1] == "X":
                                                second_x = True

                                            if second_x:
                                                print("\nThe orientation is blocked by another ship !\n")
                                                continue
                                            try:
                                                boardp1[counter_letter+1][index] = "X"
                                            except IndexError:
                                                print("The position you have chosen to put the ships is invalid !")
                                                continue
                                            return boardp1
                                        if orientation.lower() == "horizontal" or orientation.lower() == 'h':
                                            boardp1[counter_letter][index] = "X"
                                            if boardp1[counter_letter][index+2] == "X":
                                                second_x = True
                                            if boardp1[counter_letter+1][index+1] == "X":
                                                second_x = True
                                            if boardp1[counter_letter-1][index+1] == "X":
                                                second_x = True

                                            if second_x:
                                                print("\nThe orientation is blocked by another ship !\n")
                                                continue
                                            try:
                                                boardp1[counter_letter][index+1] = "X"
                                            except IndexError:
                                                print("The position you have chosen to put the ships is invalid !")
                                                continue
                                            return boardp1

                            if player == 2:
                                if size == 1:
                                    boardp2[counter_letter][index] = "X"
                                    return boardp2
                                if size == 2:
                                    while True:
                                        orientation = input("Choose whether to put the ships vertically or horizontally ! ")
                                        second_x = False
                                        if orientation.lower() == "vertical" or orientation.lower() == "v":
                                            boardp2[counter_letter][index] = "X"

                                            if boardp2[counter_letter+2][index] == "X":
                                                second_x = True
                                            if boardp2[counter_letter+1][index+1] == "X":
                                                second_x = True
                                            if boardp2[counter_letter+1][index-1] == "X":
                                                second_x = True

                                            if second_x:
                                                print("\nThe orientation is blocked by another ship !\n")
                                                continue
                                            try:
                                                boardp2[counter_letter+1][index] = "X"
                                            except IndexError:
                                                print("The position you have chosen to put the ships is invalid !")
                                                continue
                                            return boardp2
                                        if orientation.lower() == "horizontal" or orientation.lower() == 'h':
                                            boardp2[counter_letter][index] = "X"

                                            if boardp2[counter_letter+2][index] == "X":
                                                second_x = True
                                            if boardp2[counter_letter+1][index+1] == "X":
                                                second_x = True
                                            if boardp2[counter_letter+1][index-1] == "X":
                                                second_x = True

                                            if second_x:
                                                print("\nThe orientation is blocked by another ship !\n")
                                                continue
                                            try:
                                                boardp2[counter_letter][index+1] = "X"
                                            except IndexError:
                                                print("The position you have chosen to put the ships is invalid !")
                                                continue
                                            return boardp2

                            return
                        else:
                            print("Ships are too close or position is already taken !")


def ship_size(player, board, alphabet_letters, board_size, boardp1, boardp2):

    ships_size = [1, 2, 1, 2]
    ships_size_counter = 0
    for size in ships_size:
        ships_size_counter += 1
        if player == 1:
            print_board(boardp1, board_size)
            print("\nIt's Player's 1 turn!")
        if player == 2:
            print_board(boardp2, board_size)
            print("\nIt's Player's 2 turn!")
        if ships_size_counter == 1:
            print(f"\nChoose your {ships_size_counter}st ship !\n")
        if ships_size_counter == 2:
            print(f"\nChoose your {ships_size_counter}nd ship !\n")
        if ships_size_counter == 3:
            print(f"\nChoose your {ships_size_counter}rd ship !\n")
        if ships_size_counter == 4:
            print(f"\nChoose your {ships_size_counter}th ship !\n")
        if player == 1:
            ship_placement(board, alphabet_letters, boardp1, boardp2, player, size)
        if player == 2:
            ship_placement(board, alphabet_letters, boardp1, boardp2, player, size)
        if ships_size_counter == 4:
            if player == 1:
                print_board(boardp1, board_size)
            if player == 2:
                print_board(boardp2, board_size)

        else:
            print("The max ship size can only be 1 !")

    input("\n! Press ENTER to start the game\n")
    if player == 1:
        return boardp1
    if player == 2:
        return boardp2
    # msvcrt.getch()


def alphabet_letters_get(board):
    alphabet_letters = []
    row_counter = 0
    for row in board:
        alphabet_letters.append(chr(row_counter + 65))
        row_counter += 1
    return alphabet_letters


def shooting(shooting_boardp1, shooting_boardp2, player, boardp1, boardp2, alphabet_letters):
    if player == 1:
        opposite_player = 2
    if player == 2:
        opposite_player = 1
    while True:
        placement = input(f"Please choose a position to shoot at in Player's {opposite_player} board!")

        if (len(placement) == 1) or (len(placement) == 0):
            print("The coordinate is made out of 2 coordinates !")
            continue

        coordinate_number = placement[1]
        coordinate_letter = placement[0]
        if coordinate_number == '0':
            print("The number coordinate is out of range !")
            continue
        number_found = 0
        for letter in alphabet_letters:
            if coordinate_letter.lower() == letter.lower():
                number_found += 1
        if number_found == 0:
            print("The letter coordinate is out of range !")
            continue
        try:
            coordinate_number = int(coordinate_number)
        except ValueError:
            print("The second coordinate has to be a number !")
            continue

        if len(placement) == 3:
            third_coordinate = placement[2]
            try:
                third_coordinate = int(placement[2])
            except TypeError:
                print("The third coordinate has to be a number !")
                continue
            except ValueError:
                print("The third coordinate has to be a number !")
                continue

            coordinate_number = str(coordinate_number) + str(third_coordinate)
            if int(coordinate_number) > 10:
                print("The number coordinate is out of range !")
                continue

        if len(placement) > 3:
            print("Your input can be of maximum 3 characters !")
            continue
        counter_letter = -1
        for letter in alphabet_letters:
            counter_letter += 1
            if placement[0].casefold() == letter.casefold():
                for index, number in enumerate(boardp2[counter_letter]):
                    if int(coordinate_number)-1 == index:

                        if player == 1:
                            if boardp2[counter_letter][index] == 'X':
                                if_x_near = False
                                if_h_near = False

                                if boardp2[counter_letter+1][index] == 'X':
                                    if_x_near = True
                                if boardp2[counter_letter-1][index] == 'X':
                                    if_x_near = True
                                if boardp2[counter_letter][index+1] == 'X':
                                    if_x_near = True
                                if boardp2[counter_letter][index-1] == 'X':
                                    if_x_near = True

                                if if_x_near:
                                    if shooting_boardp1[counter_letter+1][index] == 'H':
                                        shooting_boardp1[counter_letter+1][index] = 'S'
                                        if_h_near = True
                                    if shooting_boardp1[counter_letter-1][index] == 'H':
                                        shooting_boardp1[counter_letter-1][index] = 'S'
                                        if_h_near = True
                                    if shooting_boardp1[counter_letter][index+1] == 'H':
                                        shooting_boardp1[counter_letter][index+1] = 'S'
                                        if_h_near = True
                                    if shooting_boardp1[counter_letter][index-1] == 'H':
                                        shooting_boardp1[counter_letter][index-1] = 'S'
                                        if_h_near = True

                                    if if_h_near:
                                        shooting_boardp1[counter_letter][index] = 'S'
                                        print("\nCongrats!\n You have sunk a large ship !\n")
                                        return shooting_boardp1, shooting_boardp2

                                    shooting_boardp1[counter_letter][index] = 'H'
                                    print("\nCongrats!\n You have hit a large ship !\n")
                                    return shooting_boardp1, shooting_boardp2

                                shooting_boardp1[counter_letter][index] = 'S'
                                print("\nCongrats!\n You have sunk a ship !\n")
                                return shooting_boardp1, shooting_boardp2

                            if boardp2[counter_letter][index] == 'O':
                                shooting_boardp1[counter_letter][index] = 'M'
                                print("\nOh no !\n You have missed !\n")
                                return shooting_boardp1, shooting_boardp2

                        if player == 2:
                            if boardp1[counter_letter][index] == 'X':
                                if_x_near = False
                                if_h_near = False

                                if boardp1[counter_letter+1][index] == 'X':
                                    if_x_near = True
                                if boardp1[counter_letter-1][index] == 'X':
                                    if_x_near = True
                                if boardp1[counter_letter][index+1] == 'X':
                                    if_x_near = True
                                if boardp1[counter_letter][index-1] == 'X':
                                    if_x_near = True

                                if if_x_near:
                                    if shooting_boardp2[counter_letter+1][index] == 'H':
                                        shooting_boardp2[counter_letter+1][index] = 'S'
                                        if_h_near = True
                                    if shooting_boardp2[counter_letter-1][index] == 'H':
                                        shooting_boardp2[counter_letter-1][index] = 'S'
                                        if_h_near = True
                                    if shooting_boardp2[counter_letter][index+1] == 'H':
                                        shooting_boardp2[counter_letter][index+1] = 'S'
                                        if_h_near = True
                                    if shooting_boardp2[counter_letter][index-1] == 'H':
                                        shooting_boardp2[counter_letter][index-1] = 'S'
                                        if_h_near = True

                                    if if_h_near:
                                        shooting_boardp2[counter_letter][index] = 'S'
                                        print("\nCongrats!\n You have sunk a large ship !\n")
                                        return shooting_boardp1, shooting_boardp2

                                    shooting_boardp2[counter_letter][index] = 'H'
                                    print("\nCongrats!\n You have hit a large ship !\n")
                                    return shooting_boardp1, shooting_boardp2

                            shooting_boardp2[counter_letter][index] = 'S'
                            print("\nCongrats!\n You have sunk a ship !\n")
                            return shooting_boardp1, shooting_boardp2

                        if boardp1[counter_letter][index] == 'O':
                            print("\nOh no !\n You have missed !\n")
                            shooting_boardp2[counter_letter][index] = 'M'
                            return shooting_boardp1, shooting_boardp2

        # if ship_placement in boardp2 == "X":
        #     empty_board.append(ship_placement)


def tie():
    while True:
        turn_option = input("\nPlease choose how many turns you want to play 5-50 ! ")
        try:
            turn_option = int(turn_option)
        except TypeError:
            print("The input has to be a whole integer !")
            continue
        except ValueError:
            print("The input has to be a whole integer !")
            continue
        if int(turn_option) < 5 or int(turn_option) > 50:
            print("Input out of range !")
            continue
        return turn_option


def win_condition(boardp1, boardp2, player):

    s_counter = 0
    if player == 2:
        for row in boardp2:
            for element in row:
                if element == "S":
                    s_counter += 1
        if s_counter == 6:
            print("\nPlayer 2 has destroyed all of Player 1's ships and won !\n\nCongrats!")
            return True
        else:
            return False

    if player == 1:
        for row in boardp1:
            for element in row:
                if element == "S":
                    s_counter += 1
        if s_counter == 6:
            print("\nPlayer 1 has destroyed all of Player 2's ships and won !\n\nCongrats!")
            return True
        else:
            return False


def which_player(counter):
    counter += 1
    if counter % 2 == 0:
        return 1, counter
    if counter % 2 != 0:
        return 2, counter


def main():
    lets_play = "Let's play Battleship!"
    print("\n", lets_play, "\n")

    board, board_size, = get_size()
    turn_option = tie()
    pre_game_preparation = True
    game_loop = True
    alphabet_letters = alphabet_letters_get(board)
    pre_game_counter = -1
    shooting_boardp1 = copy.deepcopy(board)
    shooting_boardp2 = copy.deepcopy(board)
    boardp1 = copy.deepcopy(board)
    boardp2 = copy.deepcopy(board)

    while pre_game_preparation:

        player, pre_game_counter = which_player(pre_game_counter)

        if pre_game_counter == 2:
            print("It's time for battle !")
            pre_game_preparation = False
            break

        if player == 1:

            boardp1 = ship_size(player, board, alphabet_letters, board_size, boardp1, boardp2)

        if player == 2:

            boardp2 = ship_size(player, board, alphabet_letters, board_size, boardp1, boardp2)

    counter = -1
    while game_loop:

        player, counter = which_player(counter)

        print("\n  ------------------------\n")
        if player == 1:
            print_board(shooting_boardp1, board_size)
            print(f"\nYour number of turns is {turn_option}")
            print("\nIt's Player's 1 turn!\n")

        if player == 2:
            print_board(shooting_boardp2, board_size)
            print(f"\nYour number of turns is {turn_option}")
            if turn_option == 0:
                quit("\nOh no ! It's a tie !\n")
            turn_option = turn_option - 1
            print("\nIt's Player's 2 turn!\n")

        shooting_boardp1, shooting_boardp2 = shooting(shooting_boardp1, shooting_boardp2, player, boardp1, boardp2, alphabet_letters)
        if win_condition(shooting_boardp1, shooting_boardp2, player):
            game_loop = False

        print("\n  ------------------------\n")
        if player == 1:
            print_board(shooting_boardp1, board_size)

        if player == 2:
            print_board(shooting_boardp2, board_size)

    quit("\nThe game has finished now !\n\nThanks for playing !")


if __name__ == "__main__":
    main()
