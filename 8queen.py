def is_safe(board,row,col):
    for i in range(row):
        if board[i]==col:
            return False
        if board[i]==col-(row-i):
            return False
        if board[i]==col+(row-i):
            return False
    return True
def solve_queen(board,row,sol_count):
    if row>=8:
        sol_count[0]+=1
    if sol_count[0]==1:
        print_board(board)
    for col in range(8):
        if is_safe(board,row,col):
            board[row]=col
            solve_queen(board,row+1,sol_count)
def print_board(board):
    for i in range(8):
        for j in range(8):
            if board[i]==j:
                print("Q",end=" ")
            else:
                print(".",end=" ")
        print()
    print()
def main():
    board=[-1]*8
    sol_count=[0]
    solve_queen(board,0,sol_count)
    print("Total solution is:",sol_count[0])
if __name__=="__main__":
    main()