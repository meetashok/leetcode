import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        i = 0
        
        if x < 0:
            return False
        elif x // 10 == 0:
            return True
        else:
            n_digits = int(math.log(x, 10)) + 1
            print(n_digits)
            first_digit = x // 10**(n_digits-1)
            last_digit = x % 10
            
            print(first_digit, last_digit, first_digit != last_digit)
            
            if first_digit != last_digit:
                return False
            
            x = (x % 10**n_digits - x % 10) // 10
            
            i += 1
            print(i, n_digits // 2)
            
            print(n_digits)

            if i == n_digits // 2:
                return True

if __name__ == "__main__":
    n = 123456

    solution = Solution()

    print(solution.isPalindrome(n))
