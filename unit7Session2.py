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


# print(binary_search([1, 1, 1, 3, 4], 1))
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

# Problem 4: Count Rotations
def count_rotations(nums):
  if len(nums) < 2:
    return 0

  left, right = 0, len(nums) - 1
  first_element = nums[0]

  if nums[left] < nums[right]:
    return 0

  while left < right:
    mid = (left + right) // 2
    if nums[mid] >= first_element:
      left = mid + 1
    else:
      right = mid

  return left


# print(count_rotations([10, 2, 5, 6, 8, 9]))
'''
Happy Case:
count_rotatioins([10,12,3,4,7]) => 2

Edge Case:
count_rotations([]) => 0
count_rotations([1,2,3,4]) => 0
count_rotations([9,12,13,2]) => 3
count_rotations([1]) => 0
Plan:
1. Go through the entire list a find the index of the smallest element.
2. Use a variant of binary search, comparing the first element with the mid element

Detailed Plan:
-check if the list is empty, if it is return 0
-initialize left and right pointers,
-loops 
'''


# Problem 5: Merge Sort I
def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  while i < len(left):
    result.append(left[i])
    i += 1

  while j < len(right):
    result.append(right[j])
    j += 1

  return result


def merge_sort(lst):
  if not lst:
    return []
  if len(lst) == 1:
    return lst

  mid = (len(lst) - 1) // 2

  return merge(merge_sort(lst[:mid + 1]), merge_sort(lst[mid + 1:]))


# print(merge_sort([5, 3, 4, 2, 1]))
"""
Happy Case:
merge_sort([2,4,1,3]) => [1,2,3,4]

Edge Case: 
merge_sort([]) => []
merge_sort([1,1,1,1]) => [1,1,1,1]
merge_sort([1,2,3,4]) => [1,2,3,4]
"""


# Problem 6: Circle Search
def search_circular_list(nums, target):
  if not nums:
    return -1

  left, right = 0, len(nums) - 1

  while left <= right:
    mid = (left + right) // 2
    if target == nums[mid]:
      return mid
    elif nums[left] <= nums[mid]:
      if (nums[left] <= target) and (target < nums[mid]):
        right = mid - 1
      else:
        left = mid + 1
    elif nums[mid + 1] <= nums[right]:
      if (nums[mid] < target) and (target <= nums[right]):
        left = mid + 1
      else:
        right = mid - 1

  return -1


# print(search_circular_list([9,12,2,4,7], 4))
'''
Happy Case:
f([9,12,2,4,7], 4) => 3

Edge Cases:
f([], 3) => -1
f([12,17,3,5,9], 4) => -1
f([6, 6, 8, 9, 13, 2, 5], 6) => 6

Plan:
- Brute force and traverse the entire list till the target is 
found, while keeping a count to return as index. 
(would defeat the time limitation of O(log(n)))
- Implementing a modified binary search

Detailed Plan (BS):
- check is the list is empty
- initialize two pointers left, right, set to 0, and len(lst) - 1
- initialize a first_element and last_element vars
- while left and right haven't met traverse the list
    calculate the mid with left + right // 2
    if the target is at mid return mid
    if the target is less than the value at mid:
      if first element <= value at mid:
        update first_element with mid + 1
        and left with mid + 1
      else
        right = mid - 1
        last_element = right
    if the target is more than the value at mid:
      if last_element >= value at mid:
        update last_element with mid - 1
        and right with mid - 1
      else
        left = mid + 1
        first_element = mid + 1
- if the loop ends return -1 
      
'''

## Version 2