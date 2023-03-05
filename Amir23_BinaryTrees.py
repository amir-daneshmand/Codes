# Binary trees
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return False
        else:
            if data > self.data:
                if self.right:
                    self.right.add_child(data)
                else:
                    self.right = BinaryTreeNode(data)
            else:
                if self.left:
                    self.left.add_child(data)
                else:
                    self.left = BinaryTreeNode(data)
            return True

    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        return elements

    def binary_search(self, val):
        if val == self.data:
            return True
        elif val < self.data:
            if self.left:
                return self.left.binary_search(val)
            else:
                return False
        else:
            if self.right:
                return self.right.binary_search(val)
            else:
                return False


def height(root):
    if root is None:
        return -1
    else:
        return 1 + max(height(root.left), height(root.right))


# below is a bad code, use height(root)
def get_height(node, lev=1):
    # if a node self is at level lev, this return height of that node (max distance of node to leaves)
    if node is None:
        return 0
    l_height = lev
    r_height = lev
    if node.left or node.right:
        if node.left:
            l_height = get_height(node.left, lev+1)
        if node.right:
            r_height = get_height(node.right, lev+1)
        return max(l_height, r_height)
    else:
        return lev


def get_level(node, data, lev):
    # if a node at a level lev given, this return level of a node with data = data in subtree with root node
    if node.data == data:
        return lev
    elif not node.left and not node.right:
        return False

    if node.left:
        left_res = get_level(node.left, data, lev+1)
        if left_res:
            return left_res

    if node.right:
        right_res = get_level(node.right, data, lev+1)
        if right_res:
            return right_res


def get_level_list(node, lev=1):
    height = get_height(node, 1)
    lev_max = height + 1
    level_elements = {i+lev: [] for i in range(lev_max)}
    if node.left:
        level_elements = combine(level_elements, get_level_list(node.left, lev+1))
    level_elements[lev].append(node.data)
    if node.right:
        level_elements = combine(level_elements, get_level_list(node.right, lev+1))
    return level_elements


def combine(dic1, dic2):
    for i in dic2:
        if i not in dic1:
            dic1[i] = dic2[i]
        else:
            dic1[i] += dic2[i]
    return dic1


def build_binary_tree(elements):
    root = BinaryTreeNode(elements[0])
    for i in range(1, len(elements)):
        root.add_child(elements[i])
    return root


numbers = [1, 7, 22, 5, 74, 3, 6, 22]
tree_root = build_binary_tree(numbers)
print(tree_root.in_order_traversal())

print(tree_root.binary_search(2))
print("height is = ", height(tree_root))
print("level is = ", get_level(tree_root, 5, 1))
print(get_level_list(tree_root, 1))