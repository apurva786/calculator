from calc import *

def test_sum():
    assert do_addition(6,4) == 10

def test_diff():
    assert do_subtraction(6,4) == 2

def test_multiply():
    assert do_multiplication(6,4) == 24

def test_divide():
    assert do_divide(14,7) == 2
