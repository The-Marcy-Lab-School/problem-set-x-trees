from exercises import BinaryTreeList, insert_right, insert_left, BinaryTree, preorder

def test_BinaryTreeList():
    t = BinaryTreeList('A')
    assert t[0] == 'A'
    assert t[1] == []
    assert t[2] == []
   
def test_insert_right():
    t = BinaryTreeList('A')
    insert_right(t, 'B')
    assert t[2][0] == 'B'
    insert_right(t, 'Z')
    assert t[2][0] == 'Z'
    assert t[2][2][0] == 'B'
 
def test_insert_left():
    t = BinaryTreeList('A')
    insert_left(t, 'B')
    assert t[1][0] == 'B'
    insert_left(t, 'Z')
    assert t[1][0] == 'Z'
    assert t[1][1][0] == 'B'
    
def test_BinaryTree():
    t = BinaryTree('A')
    assert t.right_child == None
    assert t.left_child == None
    
    t.insert_left('B')
    assert t.left_child.val == 'B'
    
    t.insert_right('C')
    assert t.right_child.val == 'C'
    
    t.insert_left('D')
    assert t.left_child.val == 'D'
    assert t.left_child.left_child.val == 'B'
    t.left_child.insert_right('E')
    assert t.left_child.right_child.val == 'E'
    
    t.insert_right('F')
    assert t.right_child.val == 'F'
    assert t.right_child.right_child.val == 'C'
    t.right_child.insert_left('G')
    assert t.right_child.left_child.val == 'G'
    
    assert t.get_left_child() == 'D'
    assert t.get_right_child() == 'F'
    
    assert t.get_root_val() == 'A'
    t.set_root_val('H')
    assert t.get_root_val() == 'H'
    
