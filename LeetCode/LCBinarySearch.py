def nextGreatestLetter(letters: list[str], target: str) -> str:
  left, right = 0, len(letters) - 1

  last_seen = -1
  while left <= right:
    mid = left + (right - left) // 2

    if letters[mid] > target:
      last_seen = mid
      right = mid - 1
    else:
      left = mid + 1

  if letters[last_seen] > target:
    return letters[last_seen]
  return letters[0]


# print(nextGreatestLetter(["b", "d", "g"], "c"))
'''
Happy Case:
f(["b", "d", "g"], "a") => "b"

Edge Case:
f(["x", "x", "y"], "z") => "x"
f(["a", "b"], a) => "b"
f(["b", "d", "g"], "c") => "d"

Plan (BS):
- initialize the left and right pointers at 0, and len(lst) - 1
- while left <= right
  calculate the mid with left + (right - left) // 2
  if lst[mid] > target
    update right to mid - 1
  else 
    update left to mid + 1
- if lst[mid] > target:
    return lst[mid]
- return lst[0]

Review:
time: O(log n)
space: O(1)
'''

def singleNonDuplicate(nums: list[int]) -> int:
  if len(nums) == 1:
    return nums[0]

  mid = len(nums) // 2

  if nums[mid] == nums[mid - 1]:
    if len(nums[mid + 1:]) % 2 == 0:
      return singleNonDuplicate(nums[:mid - 1])
    else:
      return singleNonDuplicate(nums[mid + 1:])
  elif nums[mid] == nums[mid + 1]:
    if len(nums[:mid]) % 2 == 0:
      return singleNonDuplicate(nums[mid + 2:])
    else:
      return singleNonDuplicate(nums[:mid])
  else:
    return nums[mid]

# print(singleNonDuplicate([2, 2, 3, 3, 4]))
'''
Happy Case:
f([1, 1, 2, 3, 3, 4, 4, 5, 5]) => 2

Edge Case:
f([1, 2, 2]) => 1
f([2, 2, 3, 3, 4]) => 3
f([2]) => 2

Plan (BS):
- if len(lst) == 1
    return lst[0]
- calculate the mid with (len(lst) // 2)
- if lst[mid] == lst[mid - 1]:
    if len(lst[mid + 1:]) % 2 == 0:
      return function recalled with lst[:mid - 1]
    else 
      return function recalled with lst[mid + 1:]
- elif lst[mid] == lst[mid + 1]
    if len(lst[:mid]) % 2 == 0:
      return function recalled with lst[mid + 2:]
    else
      return function recalled with lst[:mid]
- else
    return lst[mid]
Review:
time: O(log n)
space: O(log n)
'''
def searchRange(nums: list[int], target: int) -> list[int]:
   # Write your code here
    if not nums:
        return [-1, -1]

    positions: list[int] = []
    left, right = 0, len(nums) - 1

    while left <= right:
        mid: int = left + (right - left) // 2
        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    if left < len(nums):
        if nums[left] == target:
            positions.append(left)
        else: 
            positions.append(-1)
    else:
        positions.append(-1)

    left, right = 0, len(nums) - 1

    while left <= right:
        mid: int = left + (right - left) // 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    if nums[right] == target:
        positions.append(right)
    else:
        positions.append(-1)
    return positions
# print(searchRange([5,7,7,8,8,8,10], 8))
