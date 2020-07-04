# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Solution 1
class Solution:
    def getNumber(self, l):
        numbers = []
        while l.next is not None:
            numbers += [l.val]
            l = l.next
        numbers += [l.val]
        
        return int("".join([str(s) for s in reversed(numbers)]))
    
    def toLinkedList(self, number):
        s = [n for n in str(number)]
        
        l = None
        for i in s:
            if l is None:
                l = ListNode(int(i), None)
            else:
                l = ListNode(int(i), l)
        return l
    
    def addTwoNumbers(self, l1, l2):
        n1 = self.getNumber(l1)
        n2 = self.getNumber(l2)
        
        add = n1 + n2
        print(n1, n2, add)
        
        l = self.toLinkedList(add)
        
        return l