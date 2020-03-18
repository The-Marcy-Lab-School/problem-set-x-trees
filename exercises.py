def binary_tree_list(root: any) -> list:
    return [root, [], []]

def insert_left(root: list, value: any) -> list:
        t = root.pop(1)
        if t == []:
            root.insert(1, BinaryTreeList(value))
        else:
            root.insert(1, [value, t, []])
        return root

def insert_right(root: list, value: any) -> list:
    t = root.pop(2)

    if t == []:
        root.insert(2, BinaryTreeList(value))
    else:
        root.insert(2, [value, [], t])
    return root

class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.leftChild = None
        self.rightChild = None

    def insert_left(self, node):
        if self.leftChild == None:
            self.leftChild = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insert_right(self, node):
        if self.rightChild == None:
            self.rightChild = BinaryTree(node)
        else:
            t = BinaryTree(node)
            t.rightChild = self.rightChild
            self.rightChild = t

    def get_right_child(self):
        return self.rightChild

    def get_left_child(self):
        return self.leftChild

    def set_root_val(self, node):
        self.root = node

    def get_root_val(self):
        return self.root

def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

def postorder(tree):
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())

def inorder(tree):
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())

def is_unival_tree(tree):
    values = set()

    def duplicates(root):
            if root:
                values.add(root.root)
                duplicates(root.get_left_child().get_root_val())
                duplicates(root.get_right_child().get_root_val())
    duplicates(tree)

    return len(set(values)) == 1

def invert(tree):
    if tree and tree.leftChild and tree.rightChild:
         left = tree.leftChild
         tree.leftChild = tree.rightChild
         tree.rightChild = left
         invert(tree.leftChild)
         invert(tree.rightChild)
        return tree
    else:
        return None

def second_minimum_node(tree):
    values = []

    def find_min_node(root):
        if root.leftChild or root.rightChild:
            root.root = min(root.rightChild.root, root.leftChild.root)
        values.append(root.root)
        return find_min_node(root.root)
    find_min_node(tree)
    print(values)


'''
tree = BinaryTree(4)
tree.leftChild = BinaryTree(2)
tree.rightChild = BinaryTree(4)
tree.leftChild.leftChild = BinaryTree(3)
tree.leftChild.rightChild = BinaryTree(1)

second_minimum_node(tree)
'''