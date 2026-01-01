           

def merge_sort(nums):
    # wrapper
    yield from _merge_sort(nums, 0, len(nums) - 1)
    yield nums, -1, -1, False
    
def _merge_sort(nums, left, right):
    if left >= right:
        return

    mid = (left + right) // 2

    yield from _merge_sort(nums, left, mid)
    yield from _merge_sort(nums, mid + 1, right)
    yield from _merge(nums, left, mid, right)




def _merge(nums, left, mid, right):
    left_part = nums[left:mid + 1]
    right_part = nums[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        li = left + i
        ri = mid + 1 + j

        yield nums, (li, ri), k, True

        if left_part[i] <= right_part[j]:
            nums[k] = left_part[i]
            i += 1
        else:
            nums[k] = right_part[j]
            j += 1

        yield nums, (), k, True
        k += 1

    while i < len(left_part):
        li = left + i

        yield nums, (li,), k, True
        nums[k] = left_part[i]
        yield nums, (), k, True

        i += 1
        k += 1

    while j < len(right_part):
        ri = mid + 1 + j

        yield nums, (ri,), k, True
        nums[k] = right_part[j]
        yield nums, (), k, True

        j += 1
        k += 1
