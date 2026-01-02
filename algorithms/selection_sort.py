
def selection_sort(nums):
    
    for i in range(0, len(nums)):
        smallest = nums[i]
        for j in range(i+1, len(nums)):
            yield nums, j , i, True
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                smallest = nums[j]
    yield nums, -1, -1, False       
