# Problem Set: Trees

## Directions
Respond to short response questions in clear, concise sentences directly within this file. Use markdown to ensure that your answers are formatted correctly.

Complete code challenges in `exercises.js` or `exercises.py`. 

Use Test Driven Development to guide you. For JavaScript, run `npm install` to download dependencies. Run `npm test` to run tests locally. For Python, run `pytest`. Ensure all tests are passing before submitting this problem set.

### Short Response Questions

**1. What are the properties of a tree?**

**2. What is the definition of a tree data structure? Define it in two ways: (1) a description of edges, nodes, and paths, and (2) as a recursive data structure??**

**3. What is a binary tree and how does it differ from a regular tree?**

### Coding Exercises

1. **Implement a Binary Tree:** Implement a binary tree class using nodes and references. Instances should have the following methods available to them:
   - `get_root_val`
   - `set_root_val`
   - `insert_left`
   - `insert_right`
   - `get_left_child_val`
   - `get_right_child_val`

2. **Traversals:** Implement `preorder`, `postorder`, and `inorder` traversal. These functions should take a tree as an parameter and print each node's value.

3. **Univalued Binary Tree:** A binary tree is univalued if every node in the tree has the same value. Write a function `is_unival_tree`, that takes a Tree as a parameter and returns true if and only if the given tree is univalued.

4. **Invert a Binary Tree:** Invert a binary tree.

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

5. **Challenge Problem: Second Minimum Node:** Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property `root.val = min(root.left.val, root.right.val)` always holds.

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
