# Sudoku Solver

A lightweight Python application designed to solve 9x9 Sudoku puzzles automatically using the backtracking algorithm with bitmask optimization.

---

## 🚀 Features

* **Efficient Solving:** Uses an optimized backtracking algorithm combined with bitmasking for fast solutions.
* **Bitmask Optimization:** Tracks available numbers in rows, columns, and 3x3 boxes using bitwise operations.
* **Validation Check:** Ensures the initial puzzle setup is valid before attempting to solve.
* **Clean Interface:** Simple console-based input and output for ease of use.

---

## 🛠️ How It Works

The solver employs a **backtracking algorithm with bitmask optimization**, which is a depth-first search approach:

1. It initializes bitmasks for rows, columns, and 3x3 boxes to track which numbers (1-9) are already placed.
2. It searches for an empty cell on the grid.
3. It attempts to place digits from 1 to 9 in that cell.
4. It checks if the digit is valid according to Sudoku rules using bitmask lookups (O(1) operation).
5. If valid, it updates the bitmasks and recursively repeats the process for the next empty cell.
6. If a dead-end is reached, it backtracks, removes the choice, and tries the next number.

### Algorithm Complexity
- **Best case:** O(1) for already solved boards
- **Worst case:** Depends on puzzle difficulty, but typically solves standard puzzles in milliseconds

---

## 📦 Getting Started

### Prerequisites
Make sure you have Python installed on your system (Python 3.x is recommended).

### Running the Solver

1. Clone this repository or download `sudoku-solver.py`.
2. Open your terminal or command prompt.
3. Run the script using the following command:

```bash
python sudoku-solver.py
```

4. Enter the Sudoku board when prompted:
   - Enter each row as space-separated digits or dots
   - Use `.` or `0` to represent empty cells
   - Press Enter after each row

---

## 📝 Example

**Input Puzzle:** An empty cell is represented by `.` or `0`.

```
5 3 . . 7 . . . .
6 . . 1 9 5 . . .
. 9 8 . . . . 6 .
8 . . . 6 . . . 3
4 . . 8 . 3 . . 1
7 . . . 2 . . . 6
. 6 . . . . 2 8 .
. . . 4 1 9 . . 5
. . . . 8 . . 7 9
```

**Output (Solved):**

```
5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 4 6 1 7 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 5 8 4 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

---

## 🔧 Key Functions

- **`valid(board, row, col, box, r, c, num)`** - Checks if a number can be placed at a given position using bitmask validation.
- **`setbit(row, col, box, r, c, num)`** - Marks a number as present in the bitmasks.
- **`unsetbit(row, col, box, r, c, num)`** - Removes a number from the bitmasks during backtracking.
- **`solver(board, row, col, box, x)`** - Main recursive solver using backtracking.
- **`print_sudoku(board)`** - Displays the solved Sudoku board.

---

## 💡 Why Bitmask?

Using bitmasks (integers where each bit represents the presence of a digit 1-9) provides:
- **O(1) lookup time** for checking if a digit is valid
- **Memory efficiency** - uses 3 integers instead of storing full lists
- **Fast bit operations** - bitwise AND/OR operations are extremely fast at the CPU level

---

## 📄 License

MIT

---

## 🤝 Contributing

Feel free to fork this repository and submit pull requests for any improvements!
