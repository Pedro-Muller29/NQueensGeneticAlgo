# Evaluates a board
def evaluate(board):
    queen_pos = convertToBoard(board)
    who_is_attacked = [False for _ in range(len(queen_pos))]

    for col in range(len(queen_pos)):
        for col2 in range(col+1, len(queen_pos)):
            if checkIfAttacks(col, queen_pos[col], col2, queen_pos[col2]):
                who_is_attacked[col] = True
                who_is_attacked[col2] = True
    
    return sum(1 for is_attacked in who_is_attacked if is_attacked)

def convertToBoard(board):
    queens_pos = []

    three_bits = 7

    for _ in range(8):
        line = board & three_bits
        queens_pos.append(line)
        board >>= 3

    return queens_pos

def checkIfAttacks(qCol, qRow, oCol, oRow):
    if (qRow == oRow) or (qCol == oCol):
        return True
    
    return abs(qRow-oRow) == abs(qCol-oCol)

if __name__ == "__main__":
    board = 0b000010010100000101011110
    print(convertToBoard(board=board))
    print(evaluate(board=board))
