from exercises import BinaryTreeList, BinaryTree, insert_right, insert_left

def test_BinaryTreeList():
    t = BinaryTreeList('A')
    assert t[0] == "A"
    assert t[1] == []
    assert t[2] == []
    assert insert_left(t, ['C', [], []]) == ['A', [['C', [], []], [], []], []]
    assert insert_right(t, ['D', [], []]) == ['A', [['C', [], []], [], []], [['D', [], []], [], []]]

def test_BinaryTree():
    t = BinaryTree('A')
    t.insert_left('B')
    assert t.left_child.root == 'B' 
    t.insert_right('C')
    assert t.right_child.root == 'C'
    t.insert_left('D')
    assert t.left_child.root == 'D'
    assert t.left_child.left_child.root == 'B' 
    t.insert_right('E')
    assert t.right_child.root == 'E'
    assert t.right_child.right_child.root == 'C'
    assert t.get_right_child()['root'] == 'E'
    assert t.get_left_child()['root'] == 'D'
    assert t.get_root_val() == 'A'
    t.set_root_val('Z') 
    assert t.get_root_val() == 'Z'
    
    
