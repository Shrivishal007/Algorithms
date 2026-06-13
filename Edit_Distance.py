def editDistance(X, Y):
    m, n = len(X), len(Y)
    D = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        D[i][0] = i
    for j in range(n + 1):
        D[0][j] = j

    for i in range(1, m + 1):
        print(f"\ni = {i}")

        for j in range(1, n + 1):
            print(f"\tj = {j}, ", end = "")

            if X[i - 1] == Y[j - 1]:
                D[i][j] = D[i - 1][j - 1]

                print(f"{X[i - 1]} == {Y[j - 1]} ==> D[{i}][{j}] = D[{i - 1}][{j - 1}] = {D[i][j]}")

            else:
                insert_cost = D[i][j - 1]
                delete_cost = D[i - 1][j]
                replace_cost = D[i - 1][j - 1]
                D[i][j] = 1 + min(insert_cost, delete_cost, replace_cost)

                print(f"{X[i - 1]} != {Y[j - 1]} ==> D[{i}][{j}] = min{insert_cost, delete_cost, replace_cost} + 1 = {D[i][j]}")

    print()

    return D

def printOperations(D, X, Y, i, j):
    if i == 0 or j == 0:
        return

    if D[i][j] == D[i][j - 1] + 1:
        printOperations(D, X, Y, i, j - 1)
        print(f"Insert {Y[j - 1]}")
    elif D[i][j] == D[i - 1][j] + 1:
        printOperations(D, X, Y, i - 1, j)
        print(f"Delete {X[i - 1]}")
    else:
        printOperations(D, X, Y, i - 1, j - 1)
        if X[i - 1] != Y[j - 1]:
            print(f"Replace {X[i - 1]} with {Y[j - 1]}")

if __name__ == "__main__":
    X = list(input("Enter Source string: ").upper())
    Y = list(input("Enter Target string: ").upper())
    m = len(X)
    n = len(Y)

    D = editDistance(X, Y)

    for j in range(-2, n):
        if j < 0:
            print(" " * 3, end = "")
        else:
            print(f"{Y[j]:3}", end = "")
    print()
    for i in range(m + 1):
        if i == 0:
            print(" ", end = "")
        else:
            print(X[i - 1], end = "")

        for j in range(n + 1):
            print(f"{D[i][j]:3}", end = "")
        print()
    print()

    for j in range(-2, n):
        if j < 0:
            print(" " * 3, end = "")
        else:
            print(f"{Y[j]:3}", end = "")
    print()
    for i in range(m + 1):
        if i == 0:
            print(" ", end = "")
        else:
            print(X[i - 1], end = "")

        for j in range(n + 1):
            if i == 0:
                print(f"{j:3}", end = "")
            elif j == 0:
                print(f"{i:3}", end = "")
            else:
                if D[i][j] == D[i][j - 1] + 1:
                    char = "←"
                elif D[i][j] == D[i - 1][j] + 1:
                    char = "↑"
                else:
                    char = "↖"

                print(f"{char:>3}", end = "")
        print()
    print()

    print(f"Length: {D[m][n]}")
    print("Operations:")
    printOperations(D, X, Y, m, n)