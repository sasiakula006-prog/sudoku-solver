def valid(board, row, col, box, r, c, num):
    """Check if num can be placed at (r, c)."""
    val = 0
    val |= (row[r] & (1 << num))
    val |= (col[c] & (1 << num))
    val |= (box[3 * (r // 3) + (c // 3)] & (1 << num))

    return val == 0


def setbit(row, col, box, r, c, num):
    """Mark num as present."""
    row[r] |= (1 << num)
    col[c] |= (1 << num)
    box[3 * (r // 3) + (c // 3)] |= (1 << num)


def unsetbit(row, col, box, r, c, num):
    """Remove num from the bitmask."""
    row[r] &= ~(1 << num)
    col[c] &= ~(1 << num)
    box[3 * (r // 3) + (c // 3)] &= ~(1 << num)


def print_sudoku(board):
    """Print the Sudoku board."""
    for row in board:
        print(*row)


def solver(board, row, col, box, x):
    """Backtracking Sudoku solver."""
    if x >= 81:
        return True

    r = x // 9
    c = x % 9

    if board[r][c] == '.':
        for num in range(1, 10):
            if valid(board, row, col, box, r, c, num):
                setbit(row, col, box, r, c, num)
                board[r][c] = str(num)

                if solver(board, row, col, box, x + 1):
                    return True

                unsetbit(row, col, box, r, c, num)
                board[r][c] = '.'

        return False

    return solver(board, row, col, box, x + 1)


# Main
n = 9
board = []

print("Please enter the sudoku board (use '.' for blanks):")

for _ in range(n):
    board.append(input().split())

row = [0] * 9
col = [0] * 9
box = [0] * 9

for i in range(n):
    for j in range(n):
        if board[i][j] != '.':
            num = int(board[i][j])
            setbit(row, col, box, i, j, num)

solver(board, row, col, box, 0)

print("\nSolved Sudoku:")
print_sudoku(board)