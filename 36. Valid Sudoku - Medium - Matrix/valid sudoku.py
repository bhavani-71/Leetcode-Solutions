from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Initialize sets to track digits seen in each row, column, and 3x3 box
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Iterate over each cell in the 9x9 Sudoku board
        for row in range(9):
            for col in range(9):
                current_val = board[row][col]

                # Skip empty cells denoted by '.'
                if current_val == ".":
                    continue

                # Check if current value already seen in this row
                if current_val in rows[row]:
                    return False
                rows[row].add(current_val)

                # Check if current value already seen in this column
                if current_val in columns[col]:
                    return False
                columns[col].add(current_val)

                # Compute the index of the 3x3 box
                box_index = (row // 3) * 3 + (col // 3)

                # Check if current value already seen in this 3x3 box
                if current_val in boxes[box_index]:
                    return False
                boxes[box_index].add(current_val)

        # If no duplicates found in rows, columns, or boxes, Sudoku is valid
        return True
