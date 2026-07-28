marks=[88,72,95,61,79]
for mark in marks:
    print(mark)
for mark in reversed(marks):
    print(mark)
for mark in marks[::-1]:
    print(mark)

#Nested loop

classroom=[[85,90,78], 
           [72,88,91], 
           [95,60,83]
           ]
for row in classroom:
    for mark in row:
        print(mark, end=' ')
    print(end='\n')