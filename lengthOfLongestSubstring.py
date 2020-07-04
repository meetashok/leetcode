class Solution:
    def lengthOfLongestSubstring(self, s):
        nonrepeating = []
        maxlength = 0
        for c in s:
            if c in nonrepeating:
                if len(nonrepeating) > maxlength:
                    maxlength = len(nonrepeating)
                nonrepeating = nonrepeating[nonrepeating.index(c)+1:] + [c]
            else:
                nonrepeating += [c]
        if len(nonrepeating) > maxlength:
            maxlength = len(nonrepeating)

        return maxlength

if __name__ == "__main__":
    solution = Solution()
    # print(solution.lengthOfLongestSubstring("abcabcbb"))
    # print(solution.lengthOfLongestSubstring("bbbbb"))
    # print(solution.lengthOfLongestSubstring("pwwkew"))
    print(solution.lengthOfLongestSubstring("aab"))
