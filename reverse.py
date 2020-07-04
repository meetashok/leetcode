# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        value = int(str(abs(x))[::-1])
        if value > 2**31 -1:
            return 0
        else:
            return sign * value
        