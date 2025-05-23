from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solve the Sudoku puzzle by filling the empty cells in-place.
        Uses backtracking with sets to track used numbers in rows, columns, and boxes.
        """

        # Initialize sets to keep track of used digits in each row, column, and 3x3 box
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Pre-fill the sets with existing numbers on the board
        for row in range(9):
            for col in range(9):
                digit = board[row][col]
                if digit != '.':
                    rows[row].add(digit)
                    columns[col].add(digit)
                    box_index = (row // 3) * 3 + (col // 3)
                    boxes[box_index].add(digit)

        def backtrack(row: int, col: int) -> bool:
            # If reached past last row, puzzle solved
            if row == 9:
                return True

            # Move to next row if at end of current row
            if col == 9:
                return backtrack(row + 1, 0)

            # Skip pre-filled cells
            if board[row][col] != '.':
                return backtrack(row, col + 1)

            box_index = (row // 3) * 3 + (col // 3)

            for digit in '123456789':
                if digit not in rows[row] and digit not in columns[col] and digit not in boxes[box_index]:
                    # Place digit tentatively
                    board[row][col] = digit
                    rows[row].add(digit)
                    columns[col].add(digit)
                    boxes[box_index].add(digit)

                    # Move to next cell
                    if backtrack(row, col + 1):
                        return True

                    # Undo placement (backtrack)
                    board[row][col] = '.'
                    rows[row].remove(digit)
                    columns[col].remove(digit)
                    boxes[box_index].remove(digit)

            # If no valid digit found, backtrack
            return False

        backtrack(0, 0)
