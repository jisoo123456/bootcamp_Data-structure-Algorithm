#너비우선탐색(큐사용)
from collections import deque
class Graph:
	def __init__ (self, size) :
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]


g = None
queue = deque([])
visited_array = []


g = Graph(4)
g.graph[0][2] = 1; g.graph[0][3] = 1
g.graph[1][2] = 1
g.graph[2][0] = 1; g.graph[2][1] = 1; g.graph[2][3] = 1
g.graph[3][0] = 1; g.graph[3][2] = 1

print('## G1 무방향 그래프 ##')
for row in range(4) :
	for col in range(4) :
		print(g.graph[row][col], end =' ')
	print()

current = 0
queue.append(current)
visited_array.append(current)

while len(queue) != 0:
	next = None
	for vertex in range(4) :
		if g.graph[current][vertex] == 1 :
			if vertex in visited_array :
				pass
			else :
				next = vertex
				break

	if next is not None:
		current = next
		queue.append(current)
		visited_array.append(current)
	else :
		current = queue.popleft()


for i in visited_array :
	print(i, end = ' --> ')
print("END")
