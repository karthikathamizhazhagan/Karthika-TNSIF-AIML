def two_sum(arr, target):
    seen = {}

    for i, num in enumerate(arr):
        required = target - num

        if required in seen:
            return [seen[required], i]

        seen[num] = i

    return []

arr = [2, 7, 11, 15]
target = 9

print(two_sum(arr, target))
