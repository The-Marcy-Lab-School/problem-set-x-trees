from exercises import BinaryTreeList, insert_right, insert_left

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
    
