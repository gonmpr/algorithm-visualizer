
def insertion_sort(nums):
    for i in range(1, len(nums)):
        j = i
        yield nums, (j-1,j), i, True

        while j>0 and nums[j-1] > nums[j]:
            yield nums, (j-1,j), i, True
            nums[j], nums[j-1] = nums[j-1], nums[j]
            yield nums, (j-1,j), i, True
            j -= 1

    yield nums, -1, -1, False
