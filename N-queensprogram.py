def board_structure(board):
    for row in board:
        print(" ".join(row))
    print()
def safe(board,n,row,col):
    for i in range(col):
        if board[row][i] == "q":
            return False
    i,j = row,col
    while i>=0 and j>=0:
        if board[i][j] == "q":
            return  False
        i -= 1
        j -= 1
    i,j = row,col
    while i<n and j>=0:
        if board[i][j] == "q":
            return False
        i += 1
        j -= 1
    return True
def n_queen(board,n,col):
    if col>=n:
        print_board(board)
        return True
    sol_found = False
    for row in range(n):
        if safe(board,n,row,col):
            board[row][col] = "q"
            sol_found=n_queen(board,n,col+1) or sol_found
            board[row][col] = "."
    return sol_found
n=int(input("enter no.of queens: "))
board = [["." for _ in range(n)] for _ in range(n)]
if not n_queen(board,n,0):
    print("no solution exist.")
