import re


class TreeNode():
   def __init__(self, val, left=None, right=None):
       self.val = val
       self.left = left
       self.right = right

# Problem 1: Build A Binary Tree
node3 = TreeNode(5)
node2 = TreeNode(10)
node1 = TreeNode(1)
root = TreeNode(20)
root.right = node1
root.left = node2
node1.right = node3


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

print(postorder_traversal(root))

# Problem 7: Binary Tree Product

