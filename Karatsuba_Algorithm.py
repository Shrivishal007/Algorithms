def karatsuba(X, Y, threshold = 2, level = 0):
    indent = "│  " * level
    if level == 0:
        print(f"\n{indent}┌ karatsuba({X}, {Y})")
    else:
        print(f"{indent}├ karatsuba({X}, {Y})")

    if (X < 10 ** threshold) and (Y < 10 ** threshold):
        print(f"{indent}└► {X * Y}")

        return X * Y

    size = max(len(str(X)), len(str(Y)))
    m = size // 2

    X_1, X_0 = divmod(X, 10 ** m)
    Y_1, Y_0 = divmod(Y, 10 ** m)

    a = karatsuba(X_1, Y_1, threshold, level + 1)
    b = karatsuba(X_0, Y_0, threshold, level + 1)
    c = karatsuba(X_0 + X_1, Y_0 + Y_1, threshold, level + 1)

    d = c - b - a
    result = a * (10 ** (2 * m)) + d * (10 ** m) + b

    print(f"{indent}└► {result}             // {a}*(10^{2 * m}) + {d}*(10^{m}) + {b}")

    return result

if __name__ == "__main__":
    X = int(input("Enter the first number: "))
    Y = int(input("Enter the second number: "))
    threshold = input("Enter the threshold value (press Enter for default): ")

    if threshold == "":
        ans = karatsuba(X, Y)
    else:
        ans = karatsuba(X, Y, int(threshold))

    print(f"\n{X} * {Y} = {ans}")