class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i * i <= x:
            i += 1
        return i - 1
"""def mySqrt(x: int) -> int:
    if x < 2:
        return x
    
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    return right


def mySqrt(x: int) -> int:
    if x == 0:
        return 0
    guess = x
    while guess * guess > x:
        guess = (guess + x // guess) // 2
    return guess
""" 