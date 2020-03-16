from exercises import binary_tree, preorder, postorder, inorder,
is_unival_tree, invert,second_minimum_node
from typing import List

def test_binary_tree():
	t: List = binary_tree('A')
	assert t[0] == 'A'
	assert t[1] == []
	assert t[2] == []

print(binary_tree(['A',[],[]]))

def test_