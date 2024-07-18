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
  if n == 2 or n == 1:
    return True
  if n % 2 != 0:
    return False

  return is_power_of_two(n / 2)

# print(is_power_of_two(1024))
