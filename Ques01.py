# Question 01]  Write a program to find all pairs of an integer array whose sum is equal to a given number?


def find_pairs_with_sum(arr, target_sum):
    pairs = []
    seen = set()

    for num in arr:
        complement = target_sum - num
        if complement in seen:
            pairs.append((num, complement))
        seen.add(num)

    return pairs

# Example usage
input_array = [2, 4, 3, 5, 6, -2, 8, 9, 11, 1]
target = 9

pairs = find_pairs_with_sum(input_array, target)
print(f"Pairs in the array that sum up to {target}:")
for pair in pairs:
    print(pair)