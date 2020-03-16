from typing import List

def binary_tree(root:any):
	return [root,[],[]]
    
class BinaryTree:

    def __init__(self, data = None):

        self.left = None
        self.right = None
        self.data = data

    def insert_left(self, data):
        self.left = BinaryTree(data)

    def insert_right(self, data):
        self.right = BinaryTree(data)

    def get_right_child(self):
    	return self.right
    def get_left_child(self):
    	return self.left

    def set_root_val(self,new):
    	self.data = new
    	return new

    def get_root_val:
    	return self.data

# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

def preorder(root):
    if root: 
        # First print the data of node 
        print(root.data)
  
        # Then recur on left child 
        preorder(root.left) 
  
        # Finally recur on right child 
        preorder(root.right) 

def postorder(self,root):      
    if root: 
  
        # First recur on left child 
        postorder(root.left) 
  
        # the recur on right child 
        postorder(root.right) 
  
        # now print the data of node 
        print(root.data) 

def inorder(self,root):
    if root: 
  
        # First recur on left child 
        inorder(root.left) 
  
        # then print the data of node 
        print(root.data) 
  
        # now recur on right child 
        inorder(root.right) 

def is_unival_tree(self, root):
	seen = set()
	        
	def preorder(node):
	    if node:
	        seen.add(node.data)
	        preorder(node.left)
	        preorder(node.right)
	preorder(root)
    return len(seen) == 1

def invert(self, root):
    if root is None:
        return None
    root.left, root.right = \
        self.invertTree(root.right), self.invertTree(root.left)
    return root

def second_minimum_node(self,root):
    a = set()
    def preorder(node):
        if node:
            a.add(node.data)
            preorder(node.left)
            preorder(node.right)
    preorder(root)
    if len(a) < 2: return -1
    return sorted(a)[1]

