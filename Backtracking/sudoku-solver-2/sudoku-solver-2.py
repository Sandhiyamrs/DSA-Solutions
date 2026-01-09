def solveSudoku(board):
    def is_valid(r, c, ch):
        for i in range(9):
            if board[r][i] == ch or board[i][c] == ch:
                return False
            if board[3*(r//3)+i//3][3*(c//3)+i%3] == ch:
                return False
        return True

    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for ch in "123456789":
                        if is_valid(i, j, ch):
                            board[i][j] = ch
                            if backtrack():
                                return True
                            board[i][j] = "."
                    return False
        return True

    backtrack()
