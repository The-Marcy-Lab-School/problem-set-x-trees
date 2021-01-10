const { expect } = require('@jest/globals');
const { BinaryTree, preorder, postorder, inorder, isUnivalTree, invert, secondMinimumNode } =  require('./exercises.js');

describe('Binary Tree', () => {
    it('can get its value', () => {
      let tree1 = new BinaryTree(4);
      expect(tree1.getRootValue()).toBe(4);
      let tree2 = new BinaryTree(2);
      expect(tree2.getRootValue()).toBe(2);
    })

    it('can set its value', () => {
      let tree = new BinaryTree(4);
      expect(tree.getRootValue()).toBe(4);
      tree.setRootVal(2);
      expect(tree.getRootValue()).toBe(2);
    })

    it('can insert a left child and return the created node', () => {
      let tree = new BinaryTree(4);
      let newNode = tree.insertLeft(2);
      expect(newNode instanceof BinaryTree).toBe(true);
      expect(tree.left.getRootValue()).toBe(2);
    })

    it('can insert a right child and return the created node', () => {
      let tree = new BinaryTree(4);
      let newNode = tree.insertRight(7);
      expect(newNode instanceof BinaryTree).toBe(true);
      expect(tree.right.getRootValue()).toBe(7);
    })

    it('can get the value of its left child', () => {
      let tree = new BinaryTree(4);
      tree.insertLeft(2);
      expect(tree.getLeftChildValue()).toBe(2);
    })

    it('can get the value of its right child', () => {
      let tree = new BinaryTree(4);
      tree.insertRight(7);
      expect(tree.getRightChildValue()).toBe(7);
    })
})

describe('Preorder traversal', () => {
  it("prints the correct output", () => {
    let tree = new BinaryTree(4);
    let left = tree.insertLeft(2);
    left.insertLeft(1);
    left.insertRight(3);
    let right = tree.insertRight(7);
    right.insertRight(9);
    right.insertLeft(6);
    console.log("Preorder function should print in order: 4, 2, 1, 3, 7, 6, 9")
    preorder(tree);
  })
})

describe('Postorder traversal', () => {
  it("prints the correct output", () => {
    let tree = new BinaryTree(4);
    let left = tree.insertLeft(2);
    left.insertLeft(1);
    left.insertRight(3);
    let right = tree.insertRight(7);
    right.insertRight(9);
    right.insertLeft(6);
    console.log("Postorder function should print in order: 1, 3, 2, 6, 9, 7, 4")
    postorder(tree);
  })
})

describe('Inorder traversal', () => {
  it("prints the correct output", () => {
    let tree = new BinaryTree(4);
    let left = tree.insertLeft(2);
    left.insertLeft(1);
    left.insertRight(3);
    let right = tree.insertRight(7);
    right.insertRight(9);
    right.insertLeft(6);
    console.log("Inorder function should print in order: 1, 2, 3, 4, 6, 7, 9")
    inorder(tree);
  })
})

describe('Univalued Binary Tree', () => {
  it("returns true when given a univalued tree", () => {
    let tree = new BinaryTree(4);
    let left = tree.insertLeft(4);
    left.insertLeft(4);
    left.insertRight(4);
    let right = tree.insertRight(4);
    right.insertLeft(4);
    expect(isUnivalTree(tree)).toBe(true);
  })

  it("returns false when given a univalued tree", () => {
    let tree = new BinaryTree(4);
    let left = tree.insertLeft(4);
    left.insertLeft(4);
    left.insertRight(5);
    let right = tree.insertRight(4);
    right.insertLeft(4);
    expect(isUnivalTree(tree)).toBe(false);
  })
})

describe('Invert', () => {
  it("correctly inverts binary tree", () => {
    let tree = new BinaryTree(4);
    let left = tree.insertLeft(2);
    left.insertLeft(1);
    left.insertRight(3);
    let right = tree.insertRight(7);
    right.insertLeft(6);
    right.insertRight(9);
    invert(tree)
    expect(tree.getRootValue()).toBe(4);
    expect(tree.getLeftChildValue()).toBe(7);
    expect(tree.getRightChildValue()).toBe(2);
    expect(tree.left.getLeftChildValue()).toBe(9);
    expect(tree.left.getRightChildValue()).toBe(6);
    expect(tree.right.getLeftChildValue()).toBe(3);
    expect(tree.right.getRightChildValue()).toBe(1);
  })
})

// remove the .skip in order to run this test!
describe.skip('Second Minimum Node', () => {
  it("works for a valid example", () => {
    let tree = new BinaryTree(2);
    tree.insertLeft(2);
    let right = tree.insertRight(5);
    right.insertLeft(5);
    right.insertRight(7);
    expect(secondMinimumNode(tree)).toBe(5);
  })

  it("works for an invalid example", () => {
    let tree = new BinaryTree(2);
    tree.insertLeft(2);
    tree.insertRight(2);
    expect(secondMinimumNode(tree)).toBe(-1);
  })
})