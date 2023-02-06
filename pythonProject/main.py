class Node():
    def __int__(self):
        self.data = None
        self.node = None

def print_nodes(start):
    current = start
    print(current.data, end = ' ')
    while current.link != start:
        pre = current  #
        current = pre.link  #
        print(current.data, end = ' ')
    print()


memory = []
head, current, pre = None, None, None
data_array = ['다현', '정연', '쯔위', '사나', '지효']

def insert_node(find_data, insert_data):
    global memory, head, current, pre

    if find_data == head.data:
        node = Node()
        node.data = insert_data
        node.link = head
        last = head
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == find_data:
            node = Node()
            node.data = insert_data
            node.link = current
            pre.link = node
            return

    node = Node()
    node.data = insert_data
    current.link = node
    node.link = head

def delete_node(delete_node):
    global memory, head, current, pre

    if head.data == delete_node:
        current = head
        head = head.link
        last = head
        while last.link != current:
            last = last.link
        last.link = head
        del(current)
        return

    current = head
    while current.link != head:
        pre = current
        current = current.link
        if current.data == delete_node:
            pre.link = current.link
            del(current)
            return

def find_node(find_data):
    global memory, head, current, pre

    current = head
    if current.data == find_data:
        return current
    while current.link != head:
        current = current.link
        if current.data == find_data:
            return current
    return Node()  #여기서 node의미랑 none출력하고 싶으면?

if __name__=="__main__":
    node = Node()
    node.data = data_array[0]
    head = node
    node.link = node
    memory.append(node)

    for data in data_array[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)

    print_nodes(head)

    fNode = find_node("다현")
    print(fNode.data)

    fNode = find_node("쯔위")
    print(fNode.data)

    print(find_node("쯔위").data)

    fNode = find_node("재남")
    print(fNode.data)
    print(find_node("재남").data)

