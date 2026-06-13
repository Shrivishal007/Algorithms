def isSafe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
        if abs(row - i) == abs(col - board[i]):
            return False

    return True

def n_Queens(board, n, S, row = 0):
    if row == n:
        S.append(board.copy())

        return

    for col in range(n):

        if isSafe(board, row, col):
            board[row] = col

            n_Queens(board, n, S, row + 1)
            board[row] = -1

if __name__ == "__main__":
    N = int(input("Enter the order of the chessboard: "))
    board = [-1] * N
    S = []

    n_Queens(board, N, S)

    print("\nSolutions:")
    for ans in S:
        for i in range(N):
            for j in range(N):
                print(1 if j == ans[i] else 0, end = " ")
            print()
        print()

    print(f"Number of Solutions: {len(S)}")