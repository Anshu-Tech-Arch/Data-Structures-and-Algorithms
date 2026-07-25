marks=[91, 80, 75, 99, 65, 44]
first_m=marks[0] # This is O[1]
print(first_m)

def find_name(names, target):
    left=0
    right=len(names)-1

    while left<= right:
        middle = (left+right)//2

        if names[middle]==target:
            return middle
        elif names[middle]<target:
            left=middle+1
        else:
            right=middle-1
    return -1

names=['Ayush', 'Chirag', 'Gaurav',  'Mohit' ,'Sneha', 'Uday', 'Zara']
target_name='Sneha'
result=find_name(names, target_name)
if result != -1:
    print(f"Found at index", result)
else:
    print('Sorry not found!')