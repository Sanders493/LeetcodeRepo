# Problem 1: Neatly Nested

def is_nested(paren_s: str) -> bool:
  if paren_s == "":
    return True
  if paren_s[0] != "(" or paren_s[len(paren_s) - 1] != ")":
    return False

  return is_nested(paren_s[1:len(paren_s) - 1])

# print(is_nested(""))
'''
Happy case:
is_nested("(())") => True

Edge case:
is_nested("") => True
is_nested("()()()") => False
is_nested("((())") => False
'''

# Problem 2: How Many 1s

def count_ones(lst: list[int]) -> int:
  count = 0

  left, right = 0, len(lst) - 1

  while left <= right:
    mid = (left + right) // 2
    if lst[mid] == 0:
      left = mid + 1
    else:
      right = mid - 1

  if left < len(lst) and lst[left] == 1:
    count = len(lst) - left

  return count

# print(count_ones([0,0,0,0,1,1,1]))
'''
Happy Case:
count_ones([0,0,0,0,1,1,1]) => 3

Edge Case:
count_ones([1,1,1,2,3,4,5]) => 3
count_ones([]) => 0
count_ones([0,0,2,5,13,16,21]) => 0
count_ones([1,1,1,1]) => 4
'''

# Problem 3: Binary Search IV
def binary_search_helper(nums, target, left, right):
  if left > right:
    return -1
  mid = (left + right) // 2
  if target == nums[mid]:
    return mid
  elif target < nums[mid]:
    return binary_search_helper(nums, target, left, mid - 1)
  else:
    return binary_search_helper(nums, target, mid + 1, right)

def binary_search(nums, target):
  if not nums:
    return -1
  left, right = 0, len(nums) - 1
  return binary_search_helper(nums, target, left, right)

print(binary_search([1,1,1,3,4], 1))

'''
Happy Case:
binary_search([1,2,3,4], 2) => 1

Edge Case:
binary_search([1,2,3,4], 5) => -1
binary_search([], 3) => -1
binary_search([1,1,1,3,4], 1) => 2

Plans:
-Recalls the function with slicings of the list
-Make an helper method that also takes in the left and right parameters

Detailed Plan:
- check if the list is not empty
-in the driver function initialize the left and right parameters with 0, and len(lst) - 1
-pass them to the helper method with the list and the target 
- the main base case would be if the left and right pointers haven't met yet
- if they haven't i would recall the function with left or right updated 
'''
