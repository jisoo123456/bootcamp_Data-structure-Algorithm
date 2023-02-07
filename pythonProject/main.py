class tree_node:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

node1 = tree_node()
node1.data = 'hasa'

node2 = tree_node()
node2.data = 'sola'
node1.left = node2

node3 = tree_node()
node3.data = 'monbyeal'
node1.right = node3

node4 = tree_node()
node4.data = 'hyheen'
node2.left = node4

node5 = tree_node()
node5.data = 'zyee'
node2.right = node5

node6 = tree_node()
node6.data = 'sunmi'
node3.left = node6

def preorder(node):
    if node == None:
        return
    print(node.data, end = '->')  #화사
    preorder(node.left) #preorder(sola) -> sola -> preorder(hyheen) -> hyheen -> out preorder(hyheen) -> preorder(zyeel)
                        #zyee -> out preorder(zyee) -> out preorder(sola) -> preorder(monbyeal) -> monbyeal
                        # preorder(sunmi) -> sunmi -> out preorder(sunmi) -> preorder(monbyeal.right) -> return
    preorder(node.right)


def inorder(node):
    if node == None:
        return
    inorder(node.left)
    print(node.data, end='->')
    inorder(node.right)

def postorder(node):
    if node == None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data, end='->')

print("preorder: ", end = ' ')
preorder(node1)
print()
print("inorder: ", end = ' ')
inorder(node1)
print()
print("postorder: ", end = ' ')
postorder(node1)