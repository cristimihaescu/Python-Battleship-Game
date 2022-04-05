# from random import randint

# initializing board




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
    alphabet_letters = []
    for row in board:
        print(chr(row_counter+65), end='   ')
        alphabet_letters.append(chr(row_counter +65))
        row_counter += 1
        print(" ".join(row))
    return alphabet_letters

def ship_placement(board, alphabet_letters):
    placement = input("Please select a position for your ship ! Row first and column second !")
    counter_letter = -1
    for letter in alphabet_letters:
        counter_letter += 1
        if placement[0].casefold() == letter.casefold():
            for index , number in enumerate(board[counter_letter]) :
                if int(placement[1])-1 == index:
                    board[counter_letter][index] = "X"
                
def ship_size(board, alphabet_letters, board_size):
    ships_size = [1, 1, 1, 1]
    for size in ships_size:
        if size == 1:
            alphabet_letters = print_board(board, board_size)
            ship_placement(board, alphabet_letters)
        else:
            print("The max ship size can only be 1 !")




    

        




def main():
    lets_play = "Let's play Battleship!"
    print("\n", lets_play, "\n")

    board, board_size = get_size()
    pre_game_preparation = True

    while pre_game_preparation:
        alphabet_letters = print_board(board, board_size)
        ship_size(board, alphabet_letters, board_size)
        #pre_game_preparation = False
    print(alphabet_letters)
if __name__ == "__main__":
    main()