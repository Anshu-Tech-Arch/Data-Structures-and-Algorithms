arr1=[24,41,33,42,17]
def selection(arr1):
    n=len(arr1)
    for i in range(n):
        mini=i
        for j in range(i+1, n):
            if arr1[mini]>arr1[j]:
                arr1[mini], arr1[j] = arr1[j], arr1[mini]
    return arr1

print(selection(arr1))