def isValidSudoku(self, board: List[List[str]]) -> bool:
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    squares = [set() for _ in range(9)]
    for row in range(9):
        for col in range(9):
            num = board[row][col]
            if num != '.':
                # Is Row valid
                if num in rows[row]:
                    return False
                else:
                    rows[row].add(num)
                # Is col valid
                if num in cols[col]:
                    return False
                else:
                    cols[col].add(num)
                # Is Square valid
                square = 3 * (col // 3) + row // 3
                if num in squares[square]:
                    return False
                else:
                    squares[square].add(num)
    return True
