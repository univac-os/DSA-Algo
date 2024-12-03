class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solve the Sudoku puzzle using backtracking with further optimizations.
        """
        # Memoization sets to track used numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Initialize the memoization sets and find all empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    box_index = (r // 3) * 3 + (c // 3)
                    boxes[box_index].add(num)

        def is_valid(num, r, c):
            # Compute the box index
            box_index = (r // 3) * 3 + (c // 3)
            # Check if the number is already in the row, column, or box
            return num not in rows[r] and num not in cols[c] and num not in boxes[box_index]

        def backtrack(index):
            if index == len(empty_cells):
                return True  # All empty cells are filled correctly
            
            r, c = empty_cells[index]
            box_index = (r // 3) * 3 + (c // 3)

            for num in map(str, range(1, 10)):
                if is_valid(num, r, c):
                    # Place the number and update memoization sets
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_index].add(num)

                    if backtrack(index + 1):  # Recursive call for the next cell
                        return True

                    # Undo the move and update memoization sets
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_index].remove(num)

            return False  # Trigger backtracking if no valid number works

        backtrack(0)
