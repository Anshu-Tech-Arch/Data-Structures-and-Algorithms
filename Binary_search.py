def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            print("Found")
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    print("Not found!")
    return -1
            


nums=[5,10,20,30,40,50]
binary_search(nums, 5)