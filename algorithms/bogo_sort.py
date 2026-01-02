import random

def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            return False
    return True

def bogo_sort(nums):

    while not is_sorted(nums):
        yield nums, (random.randint(0, len(nums) -1),random.randint(0, len(nums) -1)), random.randint(0, len(nums) -1), True
        random.shuffle(nums) 
    yield nums, -1, -1, False
