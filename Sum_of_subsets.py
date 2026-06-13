def promising(curr_sum, rem_sum, target):
    if curr_sum > target:
        return False
    if curr_sum + rem_sum < target:
        return False
    return True

def sumOfSubsets(s, l, target, A, rem_sum, index = 0, curr_sum = 0):
    if index == len(s):
        return

    if promising(curr_sum, rem_sum, target):
        l[index] = 1
        if curr_sum + s[index] == target:
            A.append(l.copy())
        else:
            sumOfSubsets(s, l, target, A, rem_sum - s[index], index + 1, curr_sum + s[index])

        l[index] = 0
        sumOfSubsets(s, l, target, A, rem_sum - s[index], index + 1, curr_sum)

if __name__ == "__main__":
    s = list(map(int, input("Enter the elements in the set: ").split()))
    target = int(input("Enter the target sum: "))
    A = []
    s.sort()
    l = [0] * len(s)
    total = sum(s)

    print(s)
    sumOfSubsets(s, l, target, A, total)

    print("\nSubsets:")
    for sol in A:
        subset = [s[i] for i in range(len(s)) if sol[i] == 1]
        print(subset)