# from practice import BinaryTree,get_root_val, insert_right, insert_left, set_root_val
# from typing import List

# def binary_tree(root: any) -> List[str, List]:
#     return [root, [], []]
#             # root, left, right
    
    
# def BinaryTreeList():
#     pass

# **_A List of List:_** Implement a binary tree as a list of lists. Name your function `BinaryTreeList`. Be sure to implement `insert_right` and `insert_left`.

# BinaryTreeList()

class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.right_child = None 
        self.left_child = None
        
    def insert_left(self, node):
        if self.left_child == None:
            self.left_child = BinaryTree(node)
        if not self.left_child == None:
            new_left_child = BinaryTree(node)
            new_left_child.left_child = self.left_child
            self.left_child = new_left_child
            
    def insert_right(self, node):
        if self.right_child == None:
            self.right_child = BinaryTree(node)
        if not self.right_child == None:
            new_right_child = BinaryTree(node)
            new_right_child.right_child = self.right_child
            self.right_child = new_right_child

    def get_right_child(self):
        return self.right_child.root
        
    def get_left_child(self):
        return self.left_child.root
        
    def get_root_val(self):
        return self.root
        
    def set_root_val(self, new_root_val):
        self.root = new_root_val
        return self.root



def preorder(node):
    pass

def postorder():
    pass

def inorder():
    pass

def is_unival_tree():
    pass

def invert():
    pass

def second_minimum_node():
    pass



new = BinaryTree(5)
new.insert_left(15)
print(new.root)
print(new.get_left_child())