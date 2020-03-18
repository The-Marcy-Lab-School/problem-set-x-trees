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
    def __init__(self, val):
        self.val = val
        self.right_child = None
        self.left_child = None

    def insert_right(self, val):
        if self.right_child == None:
            self.right_child = BinaryTree(val)
        else:
            old_right = self.right_child
            new_right = BinaryTree(val)
            new_right.right_child = old_right
            self.right_child = new_right
        
    def insert_left(self, val):
        if self.left_child == None:
            self.left_child = BinaryTree(val)
        else:
            old_left = self.left_child
            new_left = BinaryTree(val)
            new_left.left_child = old_left
            self.left_child = new_left
            
    def get_right_child(self):
        return self.right_child.val
        
    def get_left_child(self):
        return self.left_child.val
        
    def set_root_val(self, val):
        self.val = val
        return self.val
        
    def get_root_val(self):
        return self.val
        
        
def preorder(node):
    if node == None:
        return None
    print(node.val)
    preorder(node.left_child)
    preorder(node.right_child)

def postorder(node):
    if node == None:
        return None
    postorder(node.left_child)
    postorder(node.right_child)
    print(node.val)

def inorder(node):
    if node == None:
        return None
    inorder(node.left_child)
    print(node.val)
    inorder(node.right_child)

def is_unival_tree(node):
    values = set()
	        
    def traverse(node):
        if node == None:
            return None
        else:
    	    values.add(node.val)
    	    traverse(node.left_child)
    	    traverse(node.right_child)
    return len(values) == 1

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

def second_minimum_node(node):
    values = set()
    
    def traverse(node):
        if node == None:
            return None
        else:
            values.add(node.val)
            traverse(node.left_child)
            traverse(node.right_child)
    
    return sorted(values)[1]