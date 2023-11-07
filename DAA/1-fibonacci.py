#  non recursive fibonacci
# def non_recursive_fibonacci(n):
#     if n <= 1:
#         return n

#     a, b = 0, 1
#     result = 0
#     for i in range(2, n):
#         result = a + b
#         a, b = b, result

#     return result

# if __name__ == "__main__":
#     n = 5
#     print(f"Fibonacci({n}) = {non_recursive_fibonacci(n)}")


# recursive fibonacci

def recursive_fibonacci(n):
    if n <= 1:
        return n
    
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

if __name__ == "__main__":
    n = 5
    print(f"Fibonacci({n}) = {recursive_fibonacci(n-1)}")
    