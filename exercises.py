def BinaryTreeList(root):
    return [root, [], []]
    
def insert_left(root, new_path):
    left_path = root.pop(1)
    if len(left_path) > 1:
        root.insert(1, [new_path, left_path, []])
    else:
        root.insert(1, [new_path, [], []])
    return root
    
def insert_right(root, new_path):
    right_path = root.pop(2)
    if len(right_path) > 1:
        root.insert(2, [new_path, [], right_path])
    else:
        root.insert(2, [new_path, [], []])
    return root


class BinaryTree:
    def __init__(self,root):
        self.root = root
        self.right_child = None 
        self.left_child = None
        
    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t
            
    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return {
            'root': self.right_child.root,
        }
        
    def get_left_child(self):
         return {
             'root': self.left_child.root,
         }
        
    def get_root_val(self):
        return self.root
        
    def set_root_val(self, new_root):
        self.root = new_root


def preorder(node):
    current = node
    if current == None:
        return None
    print(current.root)
    preorder(current.left_child)
    preorder(current.right_child)
    
    
def postorder(node):
    current = node
    if current == node.root:
        return None
    preorder(current.left_child)
    preorder(current.right_child)
    print(current.root)
    
    
def inorder(node):
    current = node
    if current == None:
        return None
    preorder(current.left_child)
    print(current.root)
    preorder(current.right_child)

globalSet = set()
def node_collector(node):
    current = node
    if current == None:
        return globalSet
        
    node_collector(current.left_child)
    node_collector(current.right_child)
    globalSet.add(current.root)

def is_unival_tree(t):
    node_collector(t)
    if len(globalSet) > 1:
        return False
    return True


def invert(t):
    holdr = None
    current = None
    holdl = None

    current = t
    if current == None:
        return None
    holdr = t.right_child
    holdl = t.left_child
    t.right_child = holdl
    t.left_child = holdr
    invert(current.right_child)
    invert(current.left_child)
    

def second_minimum_node(t):
    node_collector(t)
    list_of_nodes = sorted(globalSet)
    if len(list_of_nodes) > 1:
        return list_of_nodes[1]
    return -1
