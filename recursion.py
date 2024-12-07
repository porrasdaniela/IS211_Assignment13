def fibonacci(n):
    """Returns the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def gcd(a, b):
    """Returns the greatest common divisor (GCD) of two numbers using recursion."""
    if b == 0:
        return a
    return gcd(b, a % b)

def compareTo(s1, s2):
    """
    Recursively compares two strings.
    Returns:
        Negative number if s1 < s2
        0 if s1 == s2
        Positive number if s1 > s2
    """
    if not s1 and not s2:
        return 0
    if not s1:
        return -1
    if not s2:
        return 1
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])
    return compareTo(s1[1:], s2[1:])