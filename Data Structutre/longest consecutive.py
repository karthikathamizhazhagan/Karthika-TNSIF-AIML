def longest_consecutive(arr):
    numbers = set(arr)
    longest = 0

    for num in numbers:

        # Start only if num is the beginning
        # of a consecutive sequence
        if num - 1 not in numbers:

            current = num
            length = 1

            while current + 1 in numbers:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest


arr = [100, 4, 200, 1, 3, 2]

print(longest_consecutive(arr))
