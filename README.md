
# Sudoku Solver

A lightweight Python application designed to solve 9x9 Sudoku puzzles automatically using the backtracking algorithm. 

---

## 🚀 Features

* **Efficient Solving:** Uses an optimized backtracking algorithm to find solutions quickly.
* **Validation Check:** Ensures the initial puzzle setup is valid before attempting to solve.
* **Clean Interface:** Simple console-based input and output for ease of use.

---

## 🛠️ How It Works

The solver employs a **backtracking algorithm**, which is a depth-first search approach:
1. It searches for an empty cell on the grid.
2. It attempts to place digits from 1 to 9 in that cell.
3. It checks if the digit is valid according to Sudoku rules (unique in the row, column, and 3x3 box).
4. If valid, it recursively repeats the process for the next empty cell.
5. If a dead-end is reached, it backtracks, erases the choice, and tries the next number.

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
---

## 📝 Example

**Input Puzzle:** An empty cell is represented by `0`.

```text
5 3 0 | 0 7 0 | 0 0 0
6 0 0 | 1 9 5 | 0 0 0
0 9 8 | 0 0 0 | 0 6 0
------+------+------
8 0 0 | 0 6 0 | 0 0 3
4 0 0 | 8 0 3 | 0 0 1
7 0 0 | 0 2 0 | 0 0 6
------+------+------
0 6 0 | 0 0 0 | 2 8 0
0 0 0 | 4 1 9 | 0 0 5
0 0 0 | 0 8 0 | 0 7 9

**output :
5 3 4 | 6 7 8 | 9 1 2
6 7 2 | 1 9 5 | 3 4 8
1 9 8 | 3 4 2 | 5 6 7
------+------+------
8 5 9 | 4 6 1 | 7 2 3
4 2 6 | 8 5 3 | 7 9 1
7 1 3 | 9 2 5 | 8 4 6
------+------+------
9 6 1 | 5 3 7 | 2 8 4
2 8 7 | 4 1 9 | 6 3 5
3 4 5 | 2 8 6 | 1 7 9
