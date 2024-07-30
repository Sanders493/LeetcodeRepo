from typing import no_type_check


class TreeNode():

   def __init__(self, val, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right


# Problem 1: Build A Binary Tree
# node3 = TreeNode(4)
# node2 = TreeNode(3)
# node1 = TreeNode(2)
# root = TreeNode(1)
# root.right = node1
# root.left = node2
# node1.right = node3


# Problem 2-3: 3-Node Product I
def check_tree(root: TreeNode) -> bool:
   if not root or not root.left or not root.right:
      return False
   product = root.left.val * root.right.val
   return product == root.val


# print(check_tree(root))


# Problem 4: Find Rightmost Node I
def right_most(root: TreeNode) -> object | None:
   if not root:
      return None

   current: TreeNode = root
   while current.right:
      current = current.right

   return current.val


# print(right_most(root))


# Problem 5: Find Rightmost Node II
def right_most_II(root: TreeNode) -> object | None:
   if not root:
      return None
   if not root.right:
      return root.val

   return right_most_II(root.right)


# print(right_most_II(root))


# Problem 6: Post-order Traversal
def postorder_traversal(root: TreeNode) -> object | None:
   if not root:
      return [None]

   elements = []

   def helper(root, lst):
      if root:
         helper(root.left, lst)
         helper(root.right, lst)
         lst.append(root.val)

   helper(root, elements)
   return elements


# print(postorder_traversal(root))


# Problem 7: Binary Tree Product
def tree_product(root: TreeNode) -> int:
   if not root:
      return 1

   def helper(root) -> int:
      if not root:
         return 1

      left = helper(root.left)
      right = helper(root.right)
      return root.val * left * right

   return helper(root)


# print(tree_product(root))


# Problem 8: Binary Tree Is Leaf
def is_leaf(root: TreeNode | None, value: object) -> bool:
   if not root:
      return False

   if root.val == value:
      return root.left is None and root.right is None

   return is_leaf(root.left, value) or is_leaf(root.right, value)


# print(is_leaf(root, 3))


# Problem 9: Binary Search Tree Is Leaf
def is_leaf_bst(root: TreeNode | None, target: object) -> bool:
   if not root:
      return False

   if root.val == target:
      return (root.left is None) and (root.right is None)
   elif target < root.val:
      return is_leaf_bst(root.left, target)
   else:
      return is_leaf_bst(root.right, target)


nod1 = TreeNode(4)
nod1.right = TreeNode(5)
nod1.left = TreeNode(2)
nod1.left.left = TreeNode(1)
nod1.left.right = TreeNode(3)

# print(is_leaf_bst(nod1, 3))


# Problem 10: BST Is Full
def is_full_tree(root: TreeNode | None):
   if not root:
      return False
   if (not root.left and root.right) or (root.left and not root.right):
      return False

   def helper(root):
      if (not root.left and root.right) or (root.left and not root.right):
         return False

      if root.left and root.right:
         return helper(root.left) and helper(root.right)
      else:
         return True

   if root.left and root.right:
      return helper(root.left) and helper(root.right)
   else:
      return True


# print(is_full_tree(nod1))

## Version 3

# Problem 1: Build A Binary Tree III
node2 = TreeNode("a")
node2.left = TreeNode("b")
node2.right = TreeNode("c")
node2.right.right = TreeNode("d")

# Problem 2: 3-Node Booleans
def tree_expression(root: TreeNode) -> bool:
   if not root.left or not root.right:
      return False
      
   if root.val.lower == "and":
      return root.left.val and root.right.val
   elif root.val.lower == "or":
      return root.left.val or root.right.val
   else:
      return False



   

# Problem 3: 3-Node Equality
def equality(root: TreeNode) -> bool:
   if not root:
      return False
   if root.left and root.right:
      return root.left.val == root.right.val
   return False
node3 = TreeNode(1)
node3.left = TreeNode(2)
node3.right = TreeNode(2)
print(equality(node3))