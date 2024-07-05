def evaluate(board):
    """
    Evaluate the board to count the number of queens that are attacked.
    """
    queen_positions = convert_to_board(board)
    attacked_queens = [False] * len(queen_positions)

    for col in range(len(queen_positions)):
        for col2 in range(col + 1, len(queen_positions)):
            if are_queens_attacking_each_other(col, queen_positions[col], col2, queen_positions[col2]):
                attacked_queens[col] = True
                attacked_queens[col2] = True
    
    return sum(attacked_queens)

def convert_to_board(board):
    """
    Convert the binary representation of the board to a list of queen positions.
    """
    queens_pos = []
    three_bits = 7  # Mask to extract the last three bits

    for _ in range(8):
        row = board & three_bits
        queens_pos.append(row)
        board >>= 3

    return queens_pos

def are_queens_attacking_each_other(q1_col, q1_row, q2_col, q2_row):
    """
    Check if two queens are attacking each other.
    """
    return q1_row == q2_row or q1_col == q2_col or abs(q1_row - q2_row) == abs(q1_col - q2_col)

if __name__ == "__main__":
    board = 0b000010010100000101011110
    print(convert_to_board(board))
    print(evaluate(board))