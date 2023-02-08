#너비우선탐색(큐사용)

class Graph:
	def __init__ (self, size) :
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]


G1 = None
queue = []
visited_array = []


G1 = Graph(4)
G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print('## G1 무방향 그래프 ##')
for row in range(4) :
	for col in range(4) :
		print(G1.graph[row][col], end = ' ')
	print()

current = 0
queue.append(current)
visited_array.append(current)

while len(queue) != 0:
	next = None
	for vertex in range(4) :
		if G1.graph[current][vertex] == 1 :
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
		current = queue.pop(0)  #overhead


for i in visited_array :
	print(i, end = ' --> ')
print("END")
