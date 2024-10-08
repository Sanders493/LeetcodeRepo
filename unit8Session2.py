# class TreeNode():

#    def __init__(self, value, left=None, right=None):
#       self.val = value
#       self.left = left
#       self.right = right


#Problem 1: Is Even-valued
def is_even(root):
   if root:
      if root.val % 2 != 0:
         return False
      return is_even(root.left) and is_even(root.right)
   else:
      return True


# nod1 = TreeNode(10)
# nod1.right = TreeNode(8)
# nod1.left = TreeNode(2)
# nod1.left.left = TreeNode(4)
# nod1.left.right = TreeNode(6)
# nod1.right.right = TreeNode(1)

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


class TreeNode():

   def __init__(self, key, value, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right


# Problem 3: BST Insert
def insert(root: TreeNode | None, key: int, value: object):
   if not root:
      return None
   current = root
   while current:
      if current.key == key:
         current.val = value
         break
      elif current.key > key:
         if not current.left:
            current.left = TreeNode(key, value)
            break
         current = current.left
      else:
         if not current.right:
            current.right = TreeNode(key, value)
            break
         current = current.right

   return root


# node1 = TreeNode(10, "Neiji")
# node1.left = TreeNode(8, "Sasuke")
# node1.right = TreeNode(15, "Itachi")
# node1.left.left = TreeNode(1, "Kakashi")
# node1.left.right = TreeNode(6, "Ino")

# insert(node1, 0, "Naruto")
# print(node1.left.left.left.val)


# Problem 4: BST Remove I
def find_smallest_child(root: TreeNode) -> TreeNode:
   min_node: TreeNode = TreeNode(float("inf"), "temp")

   def helper(node: TreeNode | None) -> None:
      nonlocal min_node
      if node:
         if node.key < min_node.key:
            min_node = node
         helper(node.right)
         helper(node.left)

   helper(root)

   return min_node


def remove_bst(root: TreeNode | None, key: int) -> TreeNode | None:
   if not root:
      return None

   if root.key > key:
      root.left = remove_bst(root.left, key)
   elif root.key < key:
      root.right = remove_bst(root.right, key)
   else:
      if not root.left:
         return root.right
      if not root.right:
         return root.left

      temp_node: TreeNode = find_smallest_child(root.right)
      root.key = temp_node.key
      root.val = temp_node.val
      root.right = remove_bst(root.right, temp_node.key)

   return root


# node1 = TreeNode(10, "Neiji")
# node1.left = TreeNode(8, "Sasuke")
# node1.right = TreeNode(15, "Itachi")
# node1.left.left = TreeNode(1, "Kakashi")
# node1.left.right = TreeNode(9, "Ino")
# node1.right.left = TreeNode(13, "Madara")
# node1.right.right = TreeNode(17, "Shoji")
# remove_bst(node1, 10)
# print(node1.val)


# Problem 5: BST In-order Successor
def inorder_successor(root: TreeNode | None, current: TreeNode):
   if not root:
      return None
   node: TreeNode | None = root
   i_successor: TreeNode | None = None
   key: int = current.key

   while node:
      if node.key <= key:
         node = node.right
      else:
         i_successor = node
         node = node.left

   return i_successor


'''
       10
      /  \
     /    \
    5      15
   / \    
  1   8
     / \
    6   9
'''

# print(inorder_successor(node1, node1.right).val)

## Version 3


# Problem 1: Is Odd-valued
def count_odds(root: TreeNode | None) -> int:
   if not root:
      return 0
   if root.val % 2 != 0:
      return 1 + count_odds(root.left) + count_odds(root.right)
   else:
      return 0 + count_odds(root.left) + count_odds(root.right)


# node1 = TreeNode(1)
# node1.left = TreeNode(3)
# node1.right = TreeNode(2)
# node1.left.left = TreeNode(8)
# node1.right.right = TreeNode(13)
# print(count_odds(node1))


# Problem 2: Binary Tree Min
def tree_min(root: TreeNode | None) -> TreeNode | None:
   if not root:
      return None
   min_node: TreeNode = TreeNode(float("inf"))

   def helper(node: TreeNode | None) -> None:
      nonlocal min_node
      if node:
         if node.val < min_node.val:
            min_node = node
         helper(node.left)
         helper(node.right)

   helper(root)
   return min_node


# node1 = TreeNode(15)
# node1.left = TreeNode(3)
# node1.right = TreeNode(2)
# node1.left.left = TreeNode(8)
# node1.right.right = TreeNode(13)
# print(tree_min(node1).val)


# Problem 3: BST Insert III
def insert_with_duplicates(root, value) -> TreeNode:
   if not root:
      return TreeNode(value)

   current: TreeNode | None = root

   while current:
      if current.val == value:
         if not current.left:
            current.left = TreeNode(value)
            break
         current.left = insert_with_duplicates(current.left, value)
         break
      elif current.val > value:
         if not current.left:
            current.left = TreeNode(value)
            break
         current = current.left
      else:
         if not current.right:
            current.right = TreeNode(value)
            break
         current = current.right
   return root


# node2 = TreeNode(10)
# node2.left = TreeNode(8)
# node2.right = TreeNode(15)
# node2.left.left = TreeNode(1)
# node2.left.right = TreeNode(6)
# insert_with_duplicates(node2, 10)
# print(node2.left.right.right.val)


# Problem 4: BST Remove III
def find_largest_child(root: TreeNode) -> TreeNode:
   while root.right:
      root = root.right
   return root


def remove_bst_II(root: TreeNode | None, key: int) -> TreeNode | None:
   if not root:
      return None

   if root.key == key:
      if not root.left:
         return root.right
      elif not root.right:
         return root.left

      temp_node: TreeNode = find_largest_child(root.left)
      temp_node.right = root.right
      return root.left
   elif root.key > key:
      if not root.left:
         print("key not found")
      root.left = remove_bst_II(root.left, key)
   else:
      if not root.right:
         print("Key not found")
      root.right = remove_bst_II(root.right, key)

   return root


# node1 = TreeNode(10, "Neiji")
# node1.left = TreeNode(5, "Sasuke")
# node1.right = TreeNode(15, "Itachi")
# node1.left.left = TreeNode(1, "Kakashi")
# node1.left.right = TreeNode(8, "Ino")
# node1.right.left = TreeNode(13, "Madara")
# node1.right.right = TreeNode(17, "Shoji")
# remove_bst_II(node1, 5)
# print(node1.left.right.val)

# class TreeNode():

#    def __init__(self, value, left=None, right=None):
#       self.val = value
#       self.left = left
#       self.right = right


# Problem 5: BST Find Floor
def find_floor(root: TreeNode | None, value: int) -> TreeNode | None:
   if not root:
      return None

   current: TreeNode | None = root
   prev: TreeNode | None = None

   while current:
      if current.val > value:
         current = current.left
      else:
         prev = current
         current = current.right
   return prev


# node1 = TreeNode(10)
# node1.left = TreeNode(5)
# node1.right = TreeNode(16)
# node1.left.right = TreeNode(8)
# node1.right.left = TreeNode(13)
# node1.right.right = TreeNode(20)
# print(find_floor(node1, 15).val)
'''
Happy Case:
f(TreeNode(10, 5(None, 8), 16(13, 20)), 15) -> TreeNode(13)

Edge Cases:
f(None, 5) -> None
f(TreeNode(10, 5(None, 8), 16(13, 20)), 11) -> TreeNode(10)
f(TreeNode(10, 5(None, 8), 16(13, 20)), 2) -> None

Plans:
- Binary search through the BST using a while loop, while keeping a prev value

Detailed Plan:
- check if the root is None
- initialize a current var and set it to the root
- initialize a prev and set it to None
- while current is not None loops through the binary tree:
   if current.val > value:
      check if current.val has a left (
      if prev:
         return prev
      return None if false)
      set current to current.left
   else:
      check if current has a right (return current is false)
         set prev to current
         set current to current.right

- return None

Evalute:
Time: O(log n)
Space: O(1)
'''


# Problem 6: Nested Binary Trees
def are_equal(root, sub_root) -> bool:
   if not root and not sub_root:
      return True
   if not root or not sub_root:
      return False
   if root.val == sub_root.val:
      return are_equal(root.left, sub_root.left) and are_equal(
          root.right, sub_root.right)
   return False


def is_subtree(root: TreeNode | None, sub_root: TreeNode | None) -> bool:
   if not sub_root:
      if not root:
         return True
      return True
   if not root:
      return False

   if root.val == sub_root.val:
      return are_equal(root, sub_root)
   else:
      return is_subtree(root.left, sub_root) or is_subtree(
          root.right, sub_root)


# node1 = TreeNode(2)
# node1.left = TreeNode(3)
# node1.right = TreeNode(5)
# node1.left.left = TreeNode(6)
# node1.left.right = TreeNode(8)
# node1.right.right = TreeNode(12)

# node2 = TreeNode(3)
# node2.left = TreeNode(6)
# node2.right = TreeNode(7)
# print(is_subtree(node1, node2))
"""
      2                3
     / \              / \
    /   \            6   7  
   3     5
  / \     \
 6   7     12
 """
