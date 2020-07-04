class Solution:
    def isPalindrome(self, s1, s2):
        return s1 == reversed(s2)

    def longestPalindrome(self, s):
        for i, c in enumerate(s):
            pass




if __name__ == "__main__":
    solution = Solution()

    s = "babad"
    print(solution.longestPalindrome(s))

    s = "cbbd"
    print(solution.longestPalindrome(s))
        