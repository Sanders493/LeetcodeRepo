# Problem 1: Hello Hello


def repeat_hello(n):
  if n > 0:
    print("Hello")
    repeat_hello(n - 1)


# repeat_hello(5)


def repeat_hello_iterative(n):
  for _ in range(n):
    print("Hello")


# repeat_hello_iterative(5)

# Problem 2: Factorial Cases


def factorial(n: int) -> int:
  if n == 1 or n == 0:
    return 1

  return n * factorial(n - 1)


# print(factorial(5))

# Problem 3: Recursive Sum


def sum_list(lst: list[int]) -> int:
  if not lst:
    return 0
  return lst[0] + sum_list(lst[1:])


# print(sum_list([1,2,3,4,5]))

# Problem 4: Recursive Power of 2


def is_power_of_two(n: int | float) -> bool:
  if n == 1:
    return True
  if n % 2 != 0 or n < 1:
    return False

  return is_power_of_two(n / 2)


# print(is_power_of_two(1024))

# Problem 5: Binary Search I

def binary_search(lst, target) -> int:
  left = 0
  right = len(lst) - 1
  
  while left <= right:
    mid = (left + right) // 2
    if target == lst[mid]:
      return mid
    elif target < lst[mid]:
      right = mid - 1
    else:
      left = mid + 1

  return -1

# print(binary_search([1,2,3,4,6], 5))

# Problem 6: Backwards Binary Search

def find_last(lst, target):
  left, right = 0, len(lst) - 1
  last_occurence = -1
  
  while left <= right:
    mid = (left + right) // 2
    if lst[mid] == target:
        last_occurence = mid
        left = mid + 1
    elif target < lst[mid]:
      right = mid - 1
    else:
      left = mid + 1

  return last_occurence

# print(find_last([1,1,1,1,2,3,4,5,5,5,6], 8))

# Problem 7: Find Floor

def find_floor(lst: list[int], x: int) -> int:
  left, right = 0, len(lst) - 1
  last_smaller = -1

  while left <= right:
    mid = (left + right) // 2
    if lst[mid] == x:
      return mid
    elif lst[mid] > x:
      right = mid - 1
    else:
      last_smaller = mid
      left = mid + 1
      
  return last_smaller

# print(find_floor([2, 6, 9, 11, 11, 15, 23, 25], 11))

'''
Happy case:
find_floor([1,2,9,13,25,26], 3) => 1

Edge case:
find_floor([],2) => -1
find_floor([6, 7, 10, 12],4) => -1 
find_floor([2, 6, 9, 11, 11, 15, 23, 25], 11) => 3
'''
