import heapq

hospital=[]
#Lower Number = Higher Priority
heapq.heappush(hospital, (3,'Broken Finger'))
heapq.heappush(hospital, (1,'Heart Attack'))
heapq.heappush(hospital, (2,'High Fever'))

print(heapq.heappop(hospital))
print(heapq.heappop(hospital))
print(heapq.heappop(hospital))

