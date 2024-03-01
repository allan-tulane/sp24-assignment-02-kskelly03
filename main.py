"""
CMPS 2200  Assignment 2.
See assignment-02.pdf for details.
"""
from re import sub
import time


class BinaryNumber:
  """ done """

  def __init__(self, n):
    self.decimal_val = n
    self.binary_vec = list('{0:b}'.format(n))

  def __repr__(self):
    return ('decimal=%d binary=%s' %
            (self.decimal_val, ''.join(self.binary_vec)))


## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def binary2int(binary_vec):
  if len(binary_vec) == 0:
    return BinaryNumber(0)
  return BinaryNumber(int(''.join(binary_vec), 2))


def split_number(vec):
  return (binary2int(vec[:len(vec) // 2]), binary2int(vec[len(vec) // 2:]))


def bit_shift(number, n):
  # append n 0s to this number's binary string
  return binary2int(number.binary_vec + ['0'] * n)


def pad(x, y):
  # pad with leading 0 if x/y have different number of bits
  # e.g., [1,0] vs [1]
  if len(x) < len(y):
    x = ['0'] * (len(y) - len(x)) + x
  elif len(y) < len(x):
    y = ['0'] * (len(x) - len(y)) + y
  # pad with leading 0 if not even number of bits
  if len(x) % 2 != 0:
    x = ['0'] + x
    y = ['0'] + y
  return x, y


def subquadratic_multiply(x, y):
  x_vec = x.binary_vec
  y_vec = y.binary_vec
  x_vec, y_vec = pad(x_vec, y_vec)
  if x.decimal_val <= 1 and y.decimal_val <= 1:
    return BinaryNumber(x.decimal_val * y.decimal_val)
  else:
    x_left, x_right = split_number(x_vec)
    y_left, y_right = split_number(y_vec)
    p1 = subquadratic_multiply(x_left, y_left)
    p2 = subquadratic_multiply(x_right, y_right)
    sum1 = BinaryNumber(x_left.decimal_val + x_right.decimal_val)
    sum2 = BinaryNumber(y_left.decimal_val + y_right.decimal_val)
    p3 = subquadratic_multiply(sum1, sum2)

    n = len(x_vec)
    middle = BinaryNumber(p3.decimal_val - p1.decimal_val - p2.decimal_val)
    new_middle = bit_shift(middle, n // 2)
    p1 = bit_shift(p1, n)
    return BinaryNumber(p1.decimal_val + new_middle.decimal_val + p2.decimal_val)


def time_multiply(x, y, f):
  start = time.time()
  f(x,y)
  return (time.time() - start) * 1000
