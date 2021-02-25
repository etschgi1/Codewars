
def is_solved(board):
    zeroflag = False
    cols = [[0]*3, [0]*3, [0]*3]
    diag = [[board[0][0], board[1][1], board[2][2]],
            [board[0][2], board[1][1], board[2][0]]]
    for i in range(3):
        for j in range(3):
            cols[i][j] = board[j][i]

    for field in [board, cols, diag]:
        for element in field:
            if 0 in element:
                zeroflag = True
                continue
            elsum = sum(element)
            if((elsum % 3) == 0):
                return elsum/3
    if zeroflag:
        return -1
    return 0


A = [[0, 0, 1],
     [0, 1, 2],
     [2, 1, 0]]

print(is_solved(A))
