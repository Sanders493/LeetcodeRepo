# Problem 1: Neatly Nested
from typing_extensions import reveal_type


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


# Problem 1: Substring Search
def count_substring(s: str, sub: str) -> int:
  sub_length: int = len(sub)

  if len(s) < sub_length:
    return 0

  if s[:sub_length] == sub:
    return 1 + count_substring(s[sub_length:], sub)
  else:
    return count_substring(s[1:], sub)


# print(count_substring("ab aca ba", "ab"))
'''
Happy Case:
count_substring("abceabcfgba","ab") => 2

Edge Cases:
count_substring("","ab") => 0
count_substring("egbad","ab") => 0
count_substring("a b aca ba","ab") => 0

Detail Plan:
- The main base case will be if there string is empty return 0
- The check if the string given is smaller than the sub string
  if it is return 0
- The check is the first nth (n being the length of the sub string ) characters are equal to the sub string
  if they are return 1 + the function recalled with the slicing of the string s from [n:]
  else recall the function with the sliccing of the string from [1:]
'''


# Problem 2How Many 0s (Iterative)
def count_zeroes(lst: list[int]) -> int:
  if not lst or lst[0] == 1:
    return 0

  left, right = 0, len(lst) - 1

  while left <= right:
    mid = (left + right) // 2
    if lst[mid] == 0:
      left = mid + 1
    else:
      right = mid - 1

  return left


# print(count_zeroes([0, 0, 0]))
'''
Happy Case:
count_zeroes([0, 0, 0, 1, 1]) => 3

Edge Case: 
count_zeroes([]) => 0
count_zeroes([1, 1, 1]) => 0
count_zeroes([0, 0, 0]) => 3

Plan: 
- if the list is empty or the first element is 1 return 0
- setup the left and right pointers, to 0 and len(lst) - 1
- loop while left <= right
  calculate the mid with left + right // 2
  if lst[mid] == 0:
    left = mid + 1
  else:
    right = mid - 1

- return left

Review:
Time: O(log n)
Space: O(1)
'''


# Problem 3 How Many 0s (Recursive)
def count_zero_helper(lst: list[int], left: int, right: int) -> int:
  if left > right:
    return left

  mid = (left + right) // 2
  if lst[mid] == 0:
    return count_zero_helper(lst, mid + 1, right)
  else:
    return count_zero_helper(lst, left, mid - 1)


def count_zeroes_recursive(lst: list[int]) -> int:
  if not lst or lst[0] == 1:
    return 0
  left, right = 0, len(lst) - 1

  return count_zero_helper(lst, left, right)

# print(count_zeroes_recursive([0, 0, 0]))

'''
Happy Case:
count_zeroes([0, 0, 0, 1, 1]) => 3

Edge Case: 
count_zeroes([]) => 0
count_zeroes([1, 1, 1]) => 0
count_zeroes([0, 0, 0]) => 3

Plan: 
- same as iterative version

Review:
Time: O(log n)
Space: O(log n)
'''

# Problem 4: Special Numbers
def is_special(nums):
  n = len(nums)

  for x in range(n + 1):
      left, right = 0, n
      while left < right:
          mid = (left + right) // 2
          if nums[mid] >= x:
              right = mid
          else:
              left = mid + 1
      # low is now the first index where nums[low] >= x
      # The number of elements >= x is n - low
      if n - left == x:
          return x
  return -1
  
# print(is_special([3,5]))
'''
Happy Case:
is_special([3,5]) => 2

Edge Case: 
is_special([]) => 0
is_special([0]) => -1
is_special([1]) => 1
is_special([1,2,3]) => 2
is_special([1,2,3,4]) => -1

Review:
Time: O(n log(n))
Space: O(1)
'''
# Problem 5: Merge Sort II
def merge_sort_II(lst):
  # If the length of the list is 0-1, the list is already sorted. 
  if len(lst) <= 1:
      return lst

  # Find the middle index of the array
  mid = len(lst) // 2
  # Divide the array into two halves
  left_half = lst[:mid]
  right_half = lst[mid:]

  # Recursive calls to merge_sort for sorting the left and right halves
  left_half = merge_sort_II(left_half)
  right_half = merge_sort_II(right_half)

  # Merge the sorted arrays
  return merge_II(left_half, right_half)

def merge_II(left, right):
  lst = []
  i, j = 0, 0

  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      lst.append(left[i])
      i += 1
    else:
      lst.append(right[j])
      j += 1
      
  while i < len(left):
    lst.append(left[i])
    i += 1
  while j < len(right):
    lst.append(right[j])
    j += 1
    
  return lst
  
# print(merge_sort_II([5, 3, 4, 2, 1]))

# Version 3
# Problem 1: Remove Char
def remove_char(s: str, char: str) -> str:
  if s == "":
    return ""
  if s[0] == char:
    return remove_char(s[1:], char)
  return s[0] + remove_char(s[1:], char)

# print(remove_char("apbplbe", "b"))

'''
Happy Case:
remove_char("apbplbe", "b") => "apple"

Edge Cases:
remove_char("", "b") => ""
remove_char("mango", "g") => "mango"
remove_char("mmmmm", "m") => ""

Plans:
1. Using the length to know
'''

# Problem 2: Where Does it Go (Iterative)
def binary_search_recursive(nums, target, left, right, find_insert = False):
  if left > right and find_insert:
    return left
  if left > right and not find_insert:
    return -1
    
  mid = left + (right - left) // 2
  if nums[mid] == target:
    return mid
  elif nums[mid] > target:
    return binary_search_recursive(nums, target, left, mid - 1, True)
  else:
    return binary_search_recursive(nums, target, mid + 1, right, True)

def search_insert_recursive(nums, target):
  left, right = 0, len(nums) - 1

  index = binary_search_recursive(nums, target, left, right)

  if index != -1:
    return index
    
  return binary_search_recursive(nums, target, left, right, find_insert=True)

print(search_insert_recursive([1, 3, 5, 7, 9, 11, 13, 15], 10))

# 
