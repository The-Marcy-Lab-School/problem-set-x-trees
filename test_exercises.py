from exercises import binary_tree #, get_root_val, insert_right, insert_left, set_root_val
from typing import List

def test_binary_tree():
    t = binary_tree('A')
    assert t[0] == "A"
    assert t[1] == []
    assert t[2] == []
    left_child: List = ['B', [], []]
    t2: List = binary_tree(left_child)
    
# def test_nested_tree():
#     lef