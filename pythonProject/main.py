import random

class tree_node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

data_array = ['바나나맛우유', '레쓰비캔커피', '츄파츕스', '도시락', '삼다수', '코카콜라', '삼각김밥']
sale_array = [random.choice(data_array) for _ in range(20)]


node = tree_node()
node.data = sale_array[0]
root = node

for sale in sale_array[1:]:
    node = tree_node()
    node.data = sale

    current = root
    while True:
        if sale < current.data:
            if current.left == None:
                current.left = node
                break
            else:
                current = current.left
        elif sale > current.data:
            if current.right == None:
                current.right = node
                break
            else:
                current = current.right
        else:
            del(node)
            break

def preorder(node):
    if node == None:
        return
    print(node.data, end = ' ')
    preorder(node.left)
    preorder(node.right)

print(sale_array)
preorder(root)