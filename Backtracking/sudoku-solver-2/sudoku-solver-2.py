def solve_sudoku(board):
    def is_valid(r,c,k):
        for i in range(9):
            if board[r][i]==k or board[i][c]==k:
                return False
        br, bc = 3*(r//3), 3*(c//3)
        for i in range(br,br+3):
            for j in range(bc,bc+3):
                if board[i][j]==k:
                    return False
        return True

    def dfs():
        for i in range(9):
            for j in range(9):
                if board[i][j]==0:
                    for k in range(1,10):
                        if is_valid(i,j,k):
                            board[i][j]=k
                            if dfs():
                                return True
                            board[i][j]=0
                    return False
        return True

    dfs()
    return board

# Example usage
board = [
 [5,3,0,0,7,0,0,0,0],
 [6,0,0,1,9,5,0,0,0,0],
 [0,9,8,0,0,0,0,6,0],
 [8,0,0,0,6,0,0,0,3],
 [4,0,0,8,0,3,0,0,1],
 [7,0,0,0,2,0,0,0,6],
 [0,6,0,0,0,0,2,8,0],
 [0,0,0,4,1,9,0,0,5],
 [0,0,0,0,8,0,0,7,9]
]
print("Output:", solve_sudoku(board))
