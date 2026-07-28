def find_two_numbers(nums, target):
    left=0
    right=len(nums)-1
    while left<right:
        total=nums[right]+nums[left]
        if total==target:
            return (left, right)
        elif total>target:
            right=right-1
        else:
            left=left-1
    return []
nums=[1,3,5,6,8,11]
print(find_two_numbers(nums, 14))
