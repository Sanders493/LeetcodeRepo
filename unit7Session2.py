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
  target = 1

  left, right = 0, len(lst) - 1

  while left <= right:
    mid = (left + right) // 2
    if lst[mid] == target:
      count += 1
      left = mid + 1
    elif lst[mid] > target:
      right = mid - 1
    else:
      left = mid + 1

  return count

print(count_ones([1,1,1,1]))
'''
Happy Case:
count_ones([0,0,0,0,1,1,1]) => 3

Edge Case:
count_ones([1,1,1,2,3,4,5]) => 3
count_ones([]) => 0
count_ones([0,0,2,5,13,16,21]) => 0
count_ones([1,1,1,1]) => 4
'''