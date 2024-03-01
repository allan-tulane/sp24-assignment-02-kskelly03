from main import *

## Feel free to add your own tests here.
def test_multiply():
    assert subquadratic_multiply(BinaryNumber(4), BinaryNumber(3)). decimal_val== 4*3
    assert subquadratic_multiply(BinaryNumber(3), BinaryNumber(3)).decimal_val == 3*3
    assert subquadratic_multiply(BinaryNumber(4), BinaryNumber(4)).decimal_val == (4*4)
    assert subquadratic_multiply(BinaryNumber(5), BinaryNumber(6)).decimal_val == 5*6

time_multiply(BinaryNumber(4), BinaryNumber(5), subquadratic_multiply)
time_multiply(BinaryNumber(20), BinaryNumber(30), subquadratic_multiply)
time_multiply(BinaryNumber(1000), BinaryNumber(1000), subquadratic_multiply)
time_multiply(BinaryNumber(100000), BinaryNumber(100000), subquadratic_multiply)

#Code scales subquadratically