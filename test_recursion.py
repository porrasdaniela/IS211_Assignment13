from recursion import fibonacci, gcd, compareTo

# Test Fibonacci
print("Fibonacci Sequence:")
print(f"fibonacci(1): {fibonacci(1)}")   # should return 1
print(f"fibonacci(5): {fibonacci(5)}")   # should return 5
print(f"fibonacci(10): {fibonacci(10)}") # should return 55

# Test GCD
print("\nGreatest Common Divisor:")
print(f"gcd(48, 18): {gcd(48, 18)}")     # should return 6
print(f"gcd(17, 13): {gcd(17, 13)}")     # should return 1

# Test String Comparison
print("\nString Comparison:")
print(f"compareTo('apple', 'banana'): {compareTo('apple', 'banana')}")   # should return negative
print(f"compareTo('banana', 'apple'): {compareTo('banana', 'apple')}")   # should return positive
print(f"compareTo('apple', 'apple'): {compareTo('apple', 'apple')}")     # should return 0 