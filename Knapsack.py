def knapsack(W, w, v):
    N = len(v)
    DP = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        print(f"\ni = {i}, w[{i - 1}] = {w[i - 1]}, v[{i - 1}] = {v[i - 1]}")

        for j in range(1, W + 1):
            print(f"\tj = {j}, ", end = "")

            if w[i - 1] <= j:
                DP[i][j] = max(DP[i - 1][j], v[i - 1] + DP[i - 1][j - w[i - 1]])

                print(f"{w[i - 1]} ≤ {j} ==> DP[{i}][{j}] = max{DP[i - 1][j], v[i - 1] + DP[i - 1][j - w[i - 1]]} = {DP[i][j]}")

            else:
                DP[i][j] = DP[i - 1][j]

                print(f"{w[i - 1]} > {j} ==> DP[{i}][{j}] = DP[{i - 1}][{j}] = {DP[i][j]}")
    print()

    return DP

def print_items(DP, w, S, i, j):
    if i == 0 or j == 0:
        return

    if DP[i][j] != DP[i - 1][j]:
        S[i - 1] = 1
        print_items(DP, w, S, i - 1, j - w[i - 1])

    else:
        print_items(DP, w, S, i - 1, j)

if __name__ == "__main__":
    w = list(map(int, input("Enter the weight values: ").split()))
    v = list(map(int, input("Enter the profit values: ").split()))
    if len(w) != len(v):
        raise ValueError('Number of weights and profits must be equal')
    W = int(input("Enter total capacity: "))
    N = len(w)
    S = [0] * N

    DP = knapsack(W, w, v)

    for j in range(-1, W + 1):
        if j < 0:
            print(" ", end = "")
        else:
            print(f"{j:4}", end = "")
    print()
    for i in range(N + 1):
        print(i, end = "")

        for j in range(W + 1):
            print(f"{DP[i][j]:4}", end = "")
        print()
    print()

    print(f"Total Profit: {DP[N][W]}")
    print_items(DP, w, S, N, W)
    for i in range(N):
        if S[i] == 1:
                print(f"Item {i + 1} is selected")