class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        arr = []
        j = 0
        len2 = len(nums2)
        len1 = len(nums1)
        
        if len1 == 0 or len2 == 0:
            arr = nums1 + nums2
        else:
            for n1 in nums1:
                if j == len2:
                    arr += [n1]
                elif n1 <= nums2[j]:
                    arr += [n1]
                else:
                    while (j < len2) and (n1 > nums2[j]):
                        arr += [nums2[j]]
                        j += 1
                
                    arr += [n1]

            if j < len2:
                arr += nums2[j:]
        
        # print(arr)

        total = len1+len2
        if (total % 2 == 0):
            return (arr[total//2 - 1] + arr[total //2]) / 2.0
        else:
            
            return arr[total // 2]

if __name__ == "__main__":
    solution = Solution()

    nums1, nums2 = [1, 3], [2]
    print(solution.findMedianSortedArrays(nums1, nums2))

    nums1, nums2 = [1, 2], [3, 4]
    print(solution.findMedianSortedArrays(nums1, nums2))

    nums1, nums2 = [0, 0], [0, 0]
    print(solution.findMedianSortedArrays(nums1, nums2))

    nums1, nums2 = [], [0, 0]
    print(solution.findMedianSortedArrays(nums1, nums2))

    nums1, nums2 = [1], [1]
    print(solution.findMedianSortedArrays(nums1, nums2))

    nums1, nums2 = [1, 2], [-1, 3]
    print(solution.findMedianSortedArrays(nums1, nums2))

    nums1, nums2 = [2, 3], [1]
    print(solution.findMedianSortedArrays(nums1, nums2))
