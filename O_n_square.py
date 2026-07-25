def find_duplicate(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i]==numbers[j]:
                return True
    return False

numbers=[10,22,35,22,48]
result=find_duplicate(numbers)
if result:
    print('Found')
else:
    print('Not Found')