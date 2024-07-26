class TreeNode():

   def __init__(self, value, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right


#Problem 1: Is Even-valued
def is_even(root):
   if root:
      if root.val % 2 != 0:
         return False
      return is_even(root.left) and is_even(root.right)
   else:
      return True

nod1 = TreeNode(10)
nod1.right = TreeNode(8)
nod1.left = TreeNode(2)
nod1.left.left = TreeNode(4)
nod1.left.right = TreeNode(6)
nod1.right.right = TreeNode(1)

# print(is_even(nod1))

# Problem 2.1: Binary Tree Height
def height(root: TreeNode | None) -> int:
   if not root:
      return 0
   print(root.val)
   return max(height(root.left), height(root.right)) + 1
   
# print(height(nod1))

# Problem 2.2: Binary Tree Max
def tree_max(root: TreeNode | None) -> TreeNode | None:
   if not root:
      return None
   elements: list[TreeNode] = []
   def helper(node: TreeNode | None, lst: list[TreeNode]):
      if node:
         helper(node.left, lst)
         lst.append(node)
         helper(node.right, lst)
         
   helper(root, elements)
   
   max_val: float = float("-inf")
   max_node: TreeNode | None = None
   
   for node in elements:
      if node.val > max_val:
         max_val = node.val
         max_node = node
         
   return max_node

# print(tree_max(nod1).val)
      

