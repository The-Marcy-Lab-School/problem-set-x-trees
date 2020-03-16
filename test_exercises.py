from practice import List
from typing import List

def test_binary_tree():
    t: List = binary_tree('A')
    assert t[0] == 'A'
    assert t[1] ==[]
    assert t[2] == []
    left_child: List = ['B', [], []]
    t2 = binary_tree(left_child)
    
    

def test_insert_left():
    pass