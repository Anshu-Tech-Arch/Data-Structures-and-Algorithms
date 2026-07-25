def has_duplicates_fast(numbers):
    seen=set()
    for number in numbers:
        if number in seen:
            return True
        seen.add(number)
    return False

nums=[10,20,30,40,50,10]
result=has_duplicates_fast(nums)
if result:
    print(F'Found')
else:
    print('False')