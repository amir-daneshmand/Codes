class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def height(root):
    if root is None:
        return -1
    else:
        return 1+max(height(root.left), height(root.right))


def levelOrder(root):
    lev = 1
    queue = []
    elements = []
    dic = {j: [] for j in range(1, height(root)+2)}
    print(dic)
    print("height is ", height(root))
    root.level = 1
    queue.append(root)
    elements.append(root.info)
    dic[lev].append(root.info)
    while queue:
        current = queue.pop(0)
        if current.left or current.right:
            lev = current.level + 1
        if current.left:
            current.left.level = lev
            print("lev is ", lev)
            queue.append(current.left)
            elements.append(current.left.info)
            print("lev is ", lev)
            dic[lev].append(current.left.info)
        if current.right:
            current.right.level = lev
            queue.append(current.right)
            elements.append(current.right.info)
            dic[lev].append(current.right.info)
    print(" ".join(map(str, elements)))
    print(dic)
# def levelOrder(root):
#     #Write code Here
#     queue = []
#     elements = []
#     pos = 0
#     queue.append(root)
#     current = queue[pos]
#     elements.append(current.info)
#     while pos < len(queue):
#         current = queue[pos]
#         if current.left:
#             queue.append(current.left)
#             elements.append(current.left.info)
#         if current.right:
#             queue.append(current.right)
#             elements.append(current.right.info)
#         pos += 1
#         # print("queue length= ", len(queue))
#         # print("pos = ", pos)
#     # print(elements)
#     print(' '.join(map(str, elements)))


tree = BinarySearchTree()
arr = [3 , 5, 6, 9, 1 ,2, 7]
t = len(arr)
for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)