from exercises import binary_tree_list, get_root_val, insert_right, insert_left, BinaryTree, invert, is_unival_tree'
from typing import List


def test_binary_tree():
    t: List = binary_tree_list('A')
    assert t[0] == 'A'
    assert t[1] == []
    assert t[2] == []


def test_get_root_val():
    t: List = binary_tree_list('A')
    assert get_root_val(t) == 'A'

def test_insert_left():
    t: List = binary_tree_list('A')
    insert_left(t, 'B')
    assert t[1][0] == 'B'
    insert_left(t, 'C')
    assert t[1][0] == 'C'
    assert t[1][1][0] == 'B'


def test_BinaryTree():
    sample_tree = BinaryTree(4)
    sample_tree.insert_left(5)
    sample_tree.insert_right(6)
    assert sample_tree.get_root_val() == 4
    assert sample_tree.left_child.root == 5
    assert sample_tree.right_child.root == 6
    sample_tree.left_child.insert_left(7)
    sample_tree.right_child.insert_right(6)
    assert sample_tree.left_child.left_child.root == 7
    assert sample_tree.right_child.right_child.root == 6
    assert sample_tree.get_left_child().get_root_val() == 5
    assert sample_tree.get_right_child().get_root_val() == 6

def test_is_unival_tree():
    sample_tree = BinaryTree(4)
    sample_tree.insert_left(5)
    sample_tree.insert_right(6)

def test_invert():
    sample_tree = BinaryTree(4)
    sample_tree.insert_left(5)
    sample_tree.insert_right(6)
    invert(sample_tree)
    assert sample_tree.left_child.root == 5
    assert sample_tree.right_child.root == 6