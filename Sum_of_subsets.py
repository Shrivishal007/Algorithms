"""
Problem: Find all subsets of a given set whose elements sum up to a specific target value.
Approach: Backtracking with Branch and Bound (Pruning).
Assumptions: The input set 's' contains non-negative integers. Negative numbers break the pruning logic.
Input: A set of integers 's' and a 'target' sum.
Output: A list of binary state arrays (or the subsets themselves) representing the elements that form the target sum.
Time Complexity: O(2^N) in the worst case, but significantly reduced in practice due to bounding conditions.
Space Complexity: O(N) for the recursion stack and the state tracking array 'l'.
Key Idea: 
If (curr_sum > target) or (curr_sum + rem_sum < target):
    prune
# Otherwise, explore both choices
Include s[i]:
    recurse(i + 1, curr_sum + s[i])
Exclude s[i]:
    recurse(i + 1, curr_sum)
"""

def sumOfSubsets(s, l, target, A, rem_sum, index=0, curr_sum=0):
    # Base Case: If we successfully hit our target sum
    if curr_sum == target:
        A.append(l.copy())
        return
    
    # Base case: Exhausted all elements in the set
    if index == len(s):
        return

    # Check branch-and-bound constraints before exploring
    def promising(curr_sum, rem_sum, target):
        # Prune branch: The accumulated sum already exceeds the target
        if curr_sum > target:
            return False
        # Prune branch: Even if we take all remaining elements, we can't reach the target
        if curr_sum + rem_sum < target:
            return False
        return True

    if promising(curr_sum, rem_sum, target):
        
        # Left Branch: Include the current element
        l[index] = 1
        sumOfSubsets(s, l, target, A, rem_sum - s[index], index + 1, curr_sum + s[index])

        # Right Branch: Exclude the current element
        l[index] = 0
        sumOfSubsets(s, l, target, A, rem_sum - s[index], index + 1, curr_sum)

if __name__ == "__main__":
    s = list(map(int, input("Enter the elements in the set: ").split()))
    target = int(input("Enter the target sum: "))
    A = []

    # Sorting is critical for the logic of subsets and bounding to be predictable
    s.sort()

    # State array to track included (1) and excluded (0) elements
    l = [0] * len(s)
    total = sum(s)

    print(s)
    sumOfSubsets(s, l, target, A, total)

    print("\nSubsets:")
    for sol in A:
        # Translate the binary state array back into actual set elements
        subset = [s[i] for i in range(len(s)) if sol[i] == 1]
        print(subset)