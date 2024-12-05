"Base file"
import numpy as np

def sin_fonction(a:float)->float:
    """_summary_

    Args:
        a (float): _description_

    Returns:
        float: _description_
    """
    return np.sin(a)

def add(a: int, b: int) -> int:
    """Adds two numbers."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Subtracts b from a."""
    return a - b

def multiply(a: int, b: int) -> int:
    """Multiplies two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Divides a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def factorial(n: int) -> int:
    """Calculates the factorial of a number."""
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def is_prime(n: int) -> bool:
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def fibonacci(n: int) -> int:
    """Returns the nth Fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def gcd(a: int, b: int) -> int:
    """Calculates the greatest common divisor of a and b."""
    while b:
        a, b = b, a % b
    return a

def lcm(a: int, b: int) -> int:
    """Calculates the least common multiple of a and b."""
    return abs(a * b) // gcd(a, b)

def is_even(n: int) -> bool:
    """Checks if a number is even."""
    return n % 2 == 0

def is_odd(n: int) -> bool:
    """Checks if a number is odd."""
    return n % 2 != 0


