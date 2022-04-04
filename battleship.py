from random import randint

# initializing board
board = []
ships_size = [1,1,1,1]
numbers_list = list(range(1, 27))
print(numbers_list)

def get_size():
    board_size = int(input("Choose board size: "))
    if board_size > 10:
        print("Invalid input !")
        return get_size()
    return board_size


board_size = get_size()
print()
# numbers_list = int(board_size.count(board_size))
print("   ", end='')
for number in numbers_list:
    print(number, end=' ')
    if number >= board_size:
        break

for x in range(board_size):
    board.append(["O"] * board_size)


def print_board(board):
    row_counter = 0
    for row in board:
        print(chr(row_counter+65), end='  ')
        row_counter += 1
        print(" ".join(row))

print("Let's play Battleship!")
print_board(board)



    