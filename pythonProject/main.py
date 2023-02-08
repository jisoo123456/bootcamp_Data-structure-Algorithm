class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


store_array = [['GS25', 30], ['CU', 60], ['Seven11', 100], ['MiniStop', 90], ['Emart24', 40]]

store_graph = Graph(5)
store_graph.graph[0][1] = 1; store_graph.graph[0][2] = 1
store_graph.graph[1][0] = 1; store_graph.graph[1][2] = 1; store_graph.graph[1][3] = 1
store_graph.graph[2][0] = 1; store_graph.graph[2][1] = 1; store_graph.graph[2][3] = 1
store_graph.graph[3][1] = 1; store_graph.graph[3][2] = 1; store_graph.graph[3][4] = 1
store_graph.graph[4][3] = 1

stack = []
visit_array = []

current = 0
max = current
max_number = store_array[current][1]
stack.append(current)
visit_array.append(current)

while len(stack) != 0:
    next = None
    for vertex in range(store_graph.size):
        if store_graph.graph[current][vertex] == 1:
            if vertex in visit_array:
                pass
            else:
               next = vertex
               break
    if next != None:
        current = vertex
        stack.append(current)
        visit_array.append(current)
        if store_array[current][1] > max_number:
            #max_store = store_array[current][0]
            max = current
            max_number = store_array[current][1]
    else:
        current = stack.pop()

print(f'honeybutterchips max store & number = {store_array[max][0]}, {store_array[max][1]}')
#before {store_array[current][0]}