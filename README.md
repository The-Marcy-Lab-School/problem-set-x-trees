# Problem Set 11.5 - Introduction to Trees

## Directions
Respond to short response questions in clear, concise sentences directly within this file. Use markdown to ensure that your answers are formatted correctly.

### Short Response Questions
**1. What are the properties of a tree?**
- It consists of a root, branches, and leaves. A root is at the top and has outgoing edges that connect to other nodes, and branches have both ingoing and outgoing edges. Branches can have children, and also be parents of children. Leaves only have incoming edges, and they have no children. Each root can also contain sub-trees, which is a tree in a tree.

**2. What is the definition of a tree data structure? Define it in two ways: (1) a description of edges, nodes, and paths, and (2) as a recursive data structure??**
- The tree data structure is a special type of graph data structure that is used to represent a hierarchy. Similarly to a linked list, trees have nodes, or values in a tree, that can connect to - or point to - other nodes, which we refer to as edges. To traverse throgh a tree, you need to follow a path, which will often result to going to children nodes. Usually one parent node has two children nodes, so specifying which child node you want to go to will help follow a path to whatever node you need to reach.
Recursively, traversing follows the same rule of passing through the tree from child nodes. Simply passing in a root child will go to that child, and if that child also has a child node, you'll be able to go to that child as well. It's useful to remember that children nodes can also be parent nodes if they also have children.

**3. What is a binary tree and how does it differ from a regular tree?**
- A binary tree is when a node contains up to two children nodes, which are often referred to as the left and right children. These two children can have children nodes of their own, as a binary tree allows for two sub-trees. Any more than that though, and it would be a regular tree data structure. Regular tree data structures can have as many children nodes as you would want.

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
