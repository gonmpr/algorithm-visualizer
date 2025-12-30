           

def merge_sort(arr):
    # wrapper
    yield from _merge_sort(arr, 0, len(arr) - 1)
    yield arr, -1, -1, False
    
def _merge_sort(arr, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    yield from _merge_sort(arr, left, mid)
    yield from _merge_sort(arr, mid + 1, right)
    yield from _merge(arr, left, mid, right)

def _merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        li = left + i
        ri = mid + 1 + j

        yield arr, li, ri, True

        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1

        yield arr, k, -1, True
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        yield arr, left + i, -1, True
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        yield arr, mid + 1 + j, -1, True
        j += 1
        k += 1
