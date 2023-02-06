import random
import math

class Node():
    def __init__(self):
        self.data = None
        self.link = None

def store_list(store):  #ex. [A, 10 ,20] [B, 1, 2] [C, 20, 30]
    global memory, head, current, pre

    node = Node()
    node.data = store
    memory.append(node)

    if head == None:
        head = node
        node.link = head
        return

    node_x, node_y = node.data[1:]
    node_distance = math.sqrt(node_x * node_x + node_y * node_y)
    head_x, head_y = head.data[1:]
    head_distance = math.sqrt(head_x * head_x + head_y * head_y)

    if head_distance > node_distance:  #node가 head 앞에 오는 경우
        node.link = head  #B.link = A
        last = head  #last = A
        while last.link != head:
            last = last.link
        last.link = node
        head = node
        return

    current = head  #B
    while current.link != head:  #B.link = A/ A.link
        pre = current  #pre =B
        current = current.link  #current = B.link = A
        current_x, current_y = current.data[1:]
        current_distance = math.sqrt(current_x * current_x + current_y * current_y)

        if current_distance > node_distance:
            pre.link = node
            node.link = current
            return

    current.link = node  #A.link = c
    node.link = head  #c.link = head

def print_stores(start):  #ex. [A, 10 ,20] [B, 1, 2] [C, 20, 30]
    current = start

    while current.link != head:
        current = current.link
        x, y = current.data[1:]
        print(f'{current.data[0]} store: distance {math.sqrt(x * x + y * y)}')

memory = []
head, current, pre = None, None, None

if __name__=="__main__":
    store_array = []
    store_name = 'A'
    for _ in range(10):
        store = [store_name, random.randint(1, 100), random.randint(1, 100)]
        store_array.append(store)
        store_name = chr(ord(store_name) + 1)

    for store in store_array:
        store_list(store)  #ex. [A, 10 ,20] [B, 1, 2] [C, 20, 30]

    print_stores(head)