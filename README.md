# Problem Set 11.5 - Introduction to Trees

## Directions
Respond to short response questions in clear, concise sentences directly within this file. Use markdown to ensure that your answers are formatted correctly.

### Short Response Questions
**1. What are the properties of a tree?**
 
  A tree has a multitude of properties or features that comes with it. To start, each node is unique is in it's own right. A path like Root 
  --> leaf2 --> leaf3 --> desiredLeaf would traverse through the tree until desiredLeaf is found. If a path was specified to that node then it's
  time complexity should just be O(n), referencing the height or length of the tree up until that leaf node. Furthermore, a tree contains a root node, its 
  branches, and leaves. If you wanted to traverse through the entire tree. You could take a number of paths that lead from the root node all
  the way down to any of it's leaves, easily moving through the structure. We can not only move through the tree but move around the leaves, themselves.
  In other words, if I had a path and wanted to move around node or subtree to different place within the tree without affecting the 
  lower levers of the tree, I could. A good way to think of this is like trying to move a folder from your documents folder to you desktop. 
  Your documents folder has other folders or subdirecties inside of it, but moving that documents folder to the desktop will change the 
  path to that root node (the documents folder).

**2. What is the definition of a tree data structure? Define it in two ways: (1) a description of edges, nodes, and paths, and (2) as a recursive data structure??**

  Similar to linkedLists, a binary tree will have properties that point to other nodes down it's path, In this case, it will be a right or left property rather
  than a next property. Think of the binary. Each node can only point to at most two other nodes, unlike a normal tree where any node can have any of edges that 
  point to other nodes.
  

**3. What is a binary tree and how does it differ from a regular tree?**

  Generally, a tree is a structure that contains a set of nodes and pointers called edges to connect to the child nodes. There's a number of differences between 
  the two that woud warrant them being different data structures. First, is the amount of child node that each leaf has an edge pointing to. A tree is a tree 
  that the nodes can have any amount of children.	In contrast to in binary trees, which each node can have at most two nodes. Next, is that in a binary tree
  there are only two subtree's, the left and right subtree. While, a normal tree can hold any number of children or none at all.

### Coding Exercises
Answer the following questions in `exercises.py`. Run unit test with the `pytest` command. Ensure all tests are passing before submitting this problem set.
1. **_A List of List:_** Implement a binary tree as a list of lists. Name your function `BinaryTreeList`. Be sure to implement `insert_right` and `insert_left`.

2. **Implement a Binary True:** Implement a binary tree class using nodes and references. Instances of `BinaryTree` should have the following methods available to them:
   - `insert_left`
   - `insert_right`
   - `get_right_child`
   - `get_left_child`
   - `set_root_val`
   - `get_root_val`

3. **Traversals:** Implement `preorder`, `postorder`, and `inorder` traversal. These functions should take a tree as an parameter and print each node's value.
   
4. **Univalued Binary Tree:** A binary tree is univalued if every node in the tree has the same value. Write a function `is_unival_tree`, that takes a Tree as a parameter and returns true if and only if the given tree is univalued.

5. **Invert a Binary Tree:** Invert a binary tree.

    Input:
      ```
          4
        /   \
        2     7
      / \   / \
      1   3 6   9
      ```

      Output:
      ```

          4
        /   \
        7     2
      / \   / \
      9   6 3   1
      ```

      **Trivia:**
      This problem was inspired by this original tweet by Max Howell:

      > Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

6. **Second Minimum Node:** Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property `root.val = min(root.left.val, root.right.val)` always holds.

      Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

      If no such second minimum value exists, output `-1` instead.

        Example 1:
        ```
        Input: 
            2
          / \
          2   5
            / \
            5   7
        ```

        Output: 5
        Explanation: The smallest value is 2, the second smallest value is 5.
        

        Example 2:
        ```
        Input: 
            2
          / \
          2   2
        ```
        Output: -1
        Explanation: The smallest value is 2, but there isn't any second smallest value.
        