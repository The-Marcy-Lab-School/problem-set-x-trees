from exercises import insert_right, binary_tree, get_root_val, insert_left, BinaryTree , invert
from typing import List


def test_binary_tree():
    t: List = binary_tree('A')
    assert t[0] == 'A'
    assert t[1] == []
    assert t[2] == []
    
    
def test_get_root_val():
    t: List = binary_tree('A')
    assert get_root_val(t) == 'A'

def test_insert_left():
    t: List = binary_tree('A')
    insert_left(t, 'B')
    assert t[1][0] == 'B'
    insert_left(t, 'Z')
    assert t[1][0] == 'Z'
    assert t[1][1][0] == 'B'
    
    
def test_BinaryTree():
    sample_tree = BinaryTree(10)
    sample_tree.insert_left(9)
    sample_tree.insert_right(8)
    assert sample_tree.get_root_val() == 10
    assert sample_tree.left_child.root == 9
    assert sample_tree.right_child.root == 8
    sample_tree.left_child.insert_left(7)
    sample_tree.right_child.insert_right(6)
    assert sample_tree.left_child.left_child.root == 7
    assert sample_tree.right_child.right_child.root == 6
    assert sample_tree.get_left_child().get_root_val() == 9
    assert sample_tree.get_right_child().get_root_val() == 8


def test_invert():
    sample_tree = BinaryTree(10)
    sample_tree.insert_left(9)
    sample_tree.insert_right(8)
    invert(sample_tree)
    assert sample_tree.left_child.root == 8
    assert sample_tree.right_child.root == 9