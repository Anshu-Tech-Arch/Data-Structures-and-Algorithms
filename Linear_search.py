def linear_search(nums, target):
    for num in nums:
        if num == target:
            print(f"Found {target} at index {nums.index(num)}")
            break
        else:
            print(f"Finding....")

nums=[10,20,30,40,50,45,24,99,24]

linear_search(nums, 45)