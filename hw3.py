def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = []
    right = []
    middle = []
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            middle.append(i)

    return quick_sort(left) + middle + quick_sort(right)

arr = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
sorted_arr = quick_sort(arr)

print(sorted_arr)