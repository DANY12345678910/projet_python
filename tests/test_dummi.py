"""test file"""
import numpy as np
import pytest

from danproject.dummy import sin_fonction, add, subtract, multiply, divide, factorial, is_prime, fibonacci, gcd, lcm, is_even, is_odd

def test_dummy()->None:
    """sin test
    """
    assert sin_fonction(35) == np.sin(35)

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(3, 5) == -2

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5

def test_divide():
    assert divide(6, 2) == 3
    with pytest.raises(ValueError):
        divide(1, 0)

def test_factorial():
    assert factorial(0) == 1
    assert factorial(5) == 120

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(4) is False
    assert is_prime(17) is True

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

def test_gcd():
    assert gcd(12, 15) == 3
    assert gcd(100, 10) == 10

def test_lcm():
    assert lcm(4, 5) == 20
    assert lcm(6, 8) == 24

def test_is_even():
    assert is_even(2) is True
    assert is_even(3) is False

def test_is_odd():
    assert is_odd(3) is True
    assert is_odd(4) is False