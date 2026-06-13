def LCSLength(X, Y):
    m, n = len(X), len(Y)
    c = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        print(f"\ni = {i}")

        for j in range(1, n + 1):
            print(f"j = {j}, ", end = "")

            if X[i - 1] == Y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1

                print(f"{X[i - 1]} == {Y[j - 1]} ==> c[{i}][{j}] = {c[i - 1][j - 1]} + 1 = {c[i - 1][j - 1] + 1}")

            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])

                print(f"{X[i - 1]} != {Y[j - 1]} ==> c[{i}][{j}] = max{c[i - 1][j], c[i][j - 1]} = {max(c[i - 1][j], c[i][j - 1])}")

    print()

    return c

def printLCS(c, X, Y, i, j):
    if i == 0 or j == 0:
        return

    if X[i - 1] == Y[j - 1]:
        printLCS(c, X, Y, i - 1, j - 1)
        print(f"{X[i - 1]:2}", end = "")
    elif c[i - 1][j] >= c[i][j - 1]:
        printLCS(c, X, Y, i - 1, j)
    else:
        printLCS(c, X, Y, i, j - 1)

if __name__ == "__main__":
    X = list(input("Enter String1: ").upper())
    Y = list(input("Enter String2: ").upper())
    m = len(X)
    n = len(Y)

    c = LCSLength(X, Y)

    for j in range(-2, n):
        if j < 0:
            print(" " * 2, end = "")
        else:
            print(f"{Y[j]:2}", end = "")
    print()
    for i in range(m + 1):
        if i == 0:
            print(" ", end = "")
        else:
            print(X[i - 1], end = "")

        for j in range(n + 1):
            print(f"{c[i][j]:2}", end = "")
        print()
    print()

    for j in range(-2, n):
        if j < 0:
            print(" " * 2, end = "")
        else:
            print(f"{Y[j]:2}", end = "")
    print()
    for i in range(m + 1):
        if i == 0:
            print(" ", end = "")
        else:
            print(X[i - 1], end = "")

        for j in range(n + 1):
            if i == 0:
                print(f"{j:2}", end = "")
            elif j == 0:
                print(f"{i:2}", end = "")
            else:
                if X[i - 1] == Y[j - 1]:
                    char = "↖"
                elif c[i - 1][j] >= c[i][j - 1]:
                    char = "↑"
                else:
                    char = "←"
                
                print(f"{char:>2}", end = "")
        print()
    print()

    print(f"Length: {c[m][n]}")
    print("Common String:", end = " ")
    printLCS(c, X, Y, m, n)