def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        iterations += 1
        mid = (left + right) // 2

        if arr[mid] == target:

            return (iterations, arr[mid])
        elif arr[mid] < target:

            left = mid + 1
        else:

            right = mid - 1

    if left < len(arr):

        upper_bound = arr[left]
    else:

        upper_bound = "No upper bound found"

    return (iterations, upper_bound)


# Приклад 1:

arr = [0.5, 1.2, 3.3, 4.4, 5.5, 8.8]
target = 4.4
iterations, upper_bound = binary_search(arr, target)
print(f"Iterations: {iterations}, Upper bound: {upper_bound}")


# Приклад 2:

arr = [10.5, 20.5, 30.5, 40.5, 50.5]
target = 25.5
iterations, upper_bound = binary_search(arr, target)
print(f"Iterations: {iterations}, Upper bound: {upper_bound}")


# Приклад 3:

arr = [-5.0, -3.3, -1.1, 0.0, 2.2, 4.4]
target = -4.0
iterations, upper_bound = binary_search(arr, target)
print(f"Iterations: {iterations}, Upper bound: {upper_bound}")
