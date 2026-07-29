from collections import deque
queue=deque()

queue.append('Ravi')
queue.append('Riya')
queue.append('You')
queue.append('Karan')
print(queue)

first=queue.popleft()
print(first)
print(queue)