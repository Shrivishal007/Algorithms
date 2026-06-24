"""
Problem: Multiply two large integers efficiently.
Approach: Karatsuba Algorithm (Divide and Conquer).
Assumptions: Inputs X and Y are non-negative integers.
Input: Two integers X, Y and an optional threshold for the base case.
Output: The integer product of X and Y, with console logging of the recursion tree.
Time Complexity: O(n^(log_2(3))) ≈ O(n^1.58), where n is the maximum number of digits.
Space Complexity: O(log n) auxiliary stack space for the recursion depth.
Key Idea: 
X*Y = a*(10^2m) + (c - a - b)*(10^m) + b, 
where a = X_1*Y_1, b = X_0*Y_0, c = (X_1+X_0)*(Y_1+Y_0)
"""

def karatsuba(X, Y, threshold=2, level=0):
    indent = "│  " * level
    if level == 0:
        print(f"\n{indent}┌ karatsuba({X}, {Y})")
    else:
        print(f"{indent}├ karatsuba({X}, {Y})")

    # Base case: if BOTH numbers are smaller than the threshold, multiply directly
    if X == 0 or Y == 0:
        print(f"{indent}└► 0")

        return 0
    if (X < 10 ** threshold) or (Y < 10 ** threshold):
        print(f"{indent}└► {X * Y}")

        return X * Y

    # Calculate the size of the numbers to determine the split point
    size = max(len(str(X)), len(str(Y)))
    m = size // 2

    # Split numbers into higher and lower halves
    X_1, X_0 = divmod(X, 10 ** m)
    Y_1, Y_0 = divmod(Y, 10 ** m)

    # Recursive steps: 3 multiplications
    a = karatsuba(X_1, Y_1, threshold, level + 1)
    b = karatsuba(X_0, Y_0, threshold, level + 1)
    c = karatsuba(X_0 + X_1, Y_0 + Y_1, threshold, level + 1)

    # Combine results according to Karatsuba formula
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