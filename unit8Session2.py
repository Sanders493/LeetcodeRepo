class TreeNode():

   def __init__(self, value, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right


#Problem 1: Is Even-valued
def is_even(root):
   if root:
      if root.left:
         if root.left.val % 2 != 0:
            return False
      if root.right:
         if root.right.val % 2 != 0:
            return False
      return is_even(root.left) and is_even(root.right)
   else:
      return True

nod1 = TreeNode(4)
nod1.right = TreeNode(8)
nod1.left = TreeNode(2)
nod1.left.left = TreeNode(4)
nod1.left.right = TreeNode(6)
nod1.right.right = TreeNode(10)

# print(is_even(nod1))