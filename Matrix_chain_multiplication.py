def matrixChainOrder(p):
    n = len(p) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            m[i][j] = float('inf')

            print(f"\nm[{i}][{j}]:")
            q_vals = []

            for k in range(i, j):

                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]

                print(f"\tk = {k}, q = m[{i}][{k}] + m[{k + 1}][{j}] + (p[{i - 1}] * p[{k}] * p[{j}])")
                print(f"\t\t = {m[i][k]} + {m[k + 1][j]} + ({p[i - 1]} * {p[k]} * {p[j]}) = {q}")

                q_vals.append(q)

                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

            print(f"min{tuple(q_vals)} = {min(q_vals)}")
    print()

    return m, s

def printOptimalParens(s, i, j):
    if i == j:
        print(f"A{i}", end = "")
    else:
        print("(", end = "")
        printOptimalParens(s, i, s[i][j])
        print(" * ", end = "")
        printOptimalParens(s, s[i][j] + 1, j)
        print(")", end = "")

if __name__ == "__main__":
    p = list(map(int, input("Enter the order values: ").split()))
    n = len(p) - 1

    m, s = matrixChainOrder(p)

    for j in range(n + 1):
        if j < 1:
            print(" ", end = "")
        else:
            print(f"{j:8}", end = "")
    print()
    for i in range(1, n + 1):
        print(i, end = "")

        for j in range(1, n + 1):
            if i <= j:
                print(f"{m[i][j]:8}", end = "")
            else:
                print(f"{'-':>8}", end = "")
        print()
    print()

    for j in range(n + 1):
        if j < 1:
            print(" ", end = "")
        else:
            print(f"{j:8}", end = "")
    print()
    for i in range(1, n + 1):
        print(i, end = "")

        for j in range(1, n + 1):
            if i < j:
                print(f"{s[i][j]:8}", end = "")
            else:
                print(f"{'-':>8}", end = "")
        print()
    print()

    print("Expression:", end = " ")
    printOptimalParens(s, 1, n)