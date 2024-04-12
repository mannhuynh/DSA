# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        temp1 = ListNode()
        temp2 = ListNode()
        prev1 = temp1
        prev2 = temp2
        curr = head 
        while curr:
            if curr.val < x:
                prev1.next = curr
                prev1 = curr
            else:
                prev2.next = curr
                prev2 = curr
            curr = curr.next
        prev1.next = temp2.next
        prev2.next = None
        return temp1.next
        