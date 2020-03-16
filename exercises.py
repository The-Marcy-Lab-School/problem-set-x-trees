def BinaryTreeList(root):
    return [root, [], []]
    
def insert_right(root, val):
    t = root.pop(2)
    if t == []:
        root.insert(2, BinaryTreeList(val))
    else:
        root.insert(2, [val, [], t])
    return root

def insert_left(root, val):
    t = root.pop(1)
    if t == []:
        root.insert(1, BinaryTreeList(val))
    else:
        root.insert(1, [val, t, []])
    return root

class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.right_child = None
        self.left_child = None

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            new_right = BinaryTree(new_node)
            new_right.right_child = self.right_child
            self.right_child = new_right
        
    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            new_left = BinaryTree(new_node)
            new_left.left_child = self.left_child
            self.left_child = new_left
        
def preorder(node):
    if node == None:
        return None
    print(node.root)
    preorder(node.left_child)
    preorder(node.right_child)

def postorder(node):
    if node == None:
        return None
    postorder(node.left_child)
    postorder(node.right_child)
    print(node.root)

def inorder(node):
    if node == None:
        return None
    inorder(node.left_child)
    print(node.root)
    inorder(node.right_child)

def is_unival_tree(node):
    pass

def invert(node):
    if node == None:
        return None
        
    old_right = node.right_child
    old_left = node.left_child
    node.left_child = old_right
    node.right_child = old_left
    
    invert(node.left_child)
    invert(node.right_child)
    
    return node

def second_minimum_node():
    pass