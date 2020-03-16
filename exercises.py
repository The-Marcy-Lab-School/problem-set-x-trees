def binary_tree(root:any):
    return [root, [], []]

def get_root_val(root:any):
    return root[0]

def insert_left(root:list ,value: any):
    t = root.pop(1)
    if t == []:
        root.insert(1, binary_tree(value))
    else:
       root.insert(1, [value, t, []])
    return root
    
def insert_right(root:list, value:any):
    t = root.pop(2)
    if t == []:
        root.insert(2, binary_tree(value))
    else:
        root.insert(2, [value, t ,[]])
    return root
    

class BinaryTree:
    def __init__(self,root=None):
        self.root = root
        self.left_child = None
        self.right_child = None
        
    def insert_left(self, root):
        if self.left_child == None:
            self.left_child = BinaryTree(root)
        else :
            t = BinaryTree(root)
            t.left_child = self.left_child
            self.left_child = t
    
    def insert_right(self, root):
        if self.right_child == None:
            self.right_child = BinaryTree(root)
        else:
            t = BinaryTree(root)
            t.right_child = self.right_child
            self.right_child = t 
    
    def get_right_child(self):
        return self.right_child
    
    def get_left_child(self):
        return self.left_child
    
    def set_root_val(self,key):
        self.root = key
        return key
        
    def get_root_val(self):
        return self.root
        

def preorder(node):
    if node:
        print(node.get_root_val())
        preorder(node.get_left_child())
        preorder(node.get_right_child())


def postorder(node):
    if node != None:
        postorder(node.get_left_child())
        postorder(node.get_right_child())
        print(node.get_root_val())

def inorder(node):
    if node != None:
        inorder(node.get_left_child())
        print(node.get_root_val())
        inorder(node.get_right_child())
        
#Means: A binary tree is uni-valued if all the nodes are of same value
def is_unival_tree(node):
    if node == None:
        return None
    seen = set ()
    if node:
        seen.add(node)
        preorder(node.left_child)
        preorder(node.right_child)
    preorder(node)
    if len(seen) > 1:
        return False
    return -1

def node_collector(node):
    seen = set()
    current = node
    if current == None:
        return seen

    node_collector(current.left_child)
    node_collector(current.right_child)
    seen.add(current.root)

def is_unival_tree2(t):
    seen = set()
    node_collector(t)
    if len(seen) > 1:
        return False
    return True

def invert(node):
    if node is None:
        return None
        
    node.left_child, node.right_child = node.right_child, node.left_child
    
    invert(node.left_child)
    invert(node.right_child)
    return node


def second_minimum_node(node):
    seen = set()
    node_collector(node)
    list_of_nodes = sorted(seen)
    if len(list_of_nodes) > 1:
        return list_of_nodes[1]
    return -1
    