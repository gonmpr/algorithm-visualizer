def quick_sort(nums, low=0, high=None):
    if high is None:
        high = len(nums) - 1

    yield from _quick_sort(nums, low, high)
    yield nums, -1, -1, False

def _quick_sort(nums, low, high):
    if low < high:
        pivot_index = yield from partition(nums, low, high)
        yield from _quick_sort(nums, low, pivot_index - 1)
        yield from _quick_sort(nums, pivot_index + 1, high)



def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        yield nums, (i + 1, j), high, True

        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

            yield nums, (i, j), high, True

    nums[i + 1], nums[high] = nums[high], nums[i + 1]

    yield nums, (i + 1,), high, True

    return i + 1
