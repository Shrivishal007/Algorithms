"""
Problem: Solve the N-Queens puzzle by finding all valid placements of N mutually non-attacking queens on an NxN board.
Approach: Backtracking (Depth-First Search with pruning).
Assumptions: N is a positive integer (N > 0).
Input: An integer N representing the size of the board and the number of queens.
Output: A list of all valid board configurations printed to the console as binary matrices.
Time Complexity: O(N!) worst-case. The search space is heavily pruned, but the upper bound is bounded by permutations.
Space Complexity: O(N) for the recursive call stack and the 1D state array, plus O(S * N) to store the valid solutions (where S is the number of solutions).
Key Idea: 

"""

def nQueens(board, n, S, row=0):
    # Base case: successfully placed a queen in every row
    if row == n:
        S.append(board.copy())

        return

    # Attempt to place a queen in each column of the current row
    for col in range(n):

        def isSafe(board, row, col):
            # Check all previously placed queens (rows 0 to row-1)
            for i in range(row):
                # Check column collision
                if board[i] == col:
                    return False
                # Check diagonal collisions: slope is 1 or -1 if absolute differences match
                if abs(row - i) == abs(col - board[i]):
                    return False

            return True

        if isSafe(board, row, col):
            board[row] = col # Place queen

            nQueens(board, n, S, row + 1)

            board[row] = -1 # Backtrack step

if __name__ == "__main__":
    N = int(input("Enter the order of the chessboard: "))
    # board[i] will store the column index of the queen in row i
    board = [-1] * N
    S = []

    nQueens(board, N, S)

    print("Solutions:")
    print(*S, sep="\n")
    print(f"\nNumber of Solutions: {len(S)}")