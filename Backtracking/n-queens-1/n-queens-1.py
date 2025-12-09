def solve_n_queens(n):
    res = []
    board = [-1]*n

    def is_valid(row, col):
        for r in range(row):
            if board[r] == col or abs(board[r]-col)==row-r:
                return False
        return True

    def dfs(row):
        if row == n:
            res.append(['.'*c + 'Q' + '.'*(n-c-1) for c in board])
            return
        for col in range(n):
            if is_valid(row, col):
                board[row] = col
                dfs(row+1)

    dfs(0)
    return res

# Example usage
n = 4
print("Output:", solve_n_queens(n))
