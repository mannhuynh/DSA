import unittest

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""
This function reverses a singly-linked list.

The process is as follows:

1. Initialize three pointers: `prev` to keep track of the previous node (initially set to None), 
   `curr` to keep track of the current node (set to the head of the list), and
   `temp` to keep track of the next node in the list.

2. Loop through the list until there are no more nodes (`curr` becomes None).

3. In each iteration, we:
    a. Store the next node in the list in `temp`.
    b. Reverse the `next` pointer of the current node to point back to the previous node.
    c. Move the `prev` and `curr` pointers one step forward.

4. After the loop completes, return the new head of the reversed list (which is stored in `prev`).
"""

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head

        while curr:
            # Store the next node in the list to avoid losing it after we modify the current node's next pointer.
            temp = curr.next
            # Reverse the next pointer of the current node by pointing it back to the previous node (if it exists).
            curr.next = prev
            # Move the previous and current pointers one step forward for the next iteration.
            prev = curr
            curr = temp

        return prev







class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertIsNone(self.solution.reverseList(None))

    def test_single_node(self):
        head = ListNode(1)
        expected = ListNode(1, None)
        self.assertEqual(self.solution.reverseList(head), expected)

    def test_three_nodes(self):
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        expected = ListNode(3)
        expected.next = ListNode(2)
        expected.next.next = ListNode(1)
        self.assertEqual(self.solution.reverseList(head), expected)

    def test_large_list(self):
        # Create a large linked list
        head = ListNode(1)
        for i in range(100):
            head.next = ListNode(i+2, head.next)

        # Reverse the list and check if it's correct
        reversed_head = self.solution.reverseList(head)
        prev = None
        while reversed_head:
            curr = reversed_head
            reversed_head = reversed_head.next
            curr.next = prev
            prev = curr

        expected = ListNode(100)
        for i in range(99, 0, -1):
            expected.next = ListNode(i+1, expected.next)

        self.assertEqual(prev, expected)


# if __name__ == '__main__':
#     unittest.main()

        print("Running tests...")
        self.test_empty_list()
        self.test_single_node()
        self.test_three_nodes()
        self.test_large_list()

        print("Test case 4: Test with random linked list")
        head = ListNode(5)
        head.next = ListNode(2, head.next)
        head.next.next = ListNode(3, head.next.next)

        reversed_head = self.solution.reverseList(head)

        print("Reversed list:")
        while reversed_head:
            print(reversed_head.val, end=" ")
            reversed_head = reversed_head.next

        self.assertEqual(self.solution.reverseList(head), expected)

        print("\nTest case 5: Test with linked list containing duplicates")
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        head.next.next.next = ListNode(2)

        reversed_head = self.solution.reverseList(head)

        print("Reversed list:")
        while reversed_head:
            print(reversed_head.val, end=" ")
            reversed_head = reversed_head.next

        self.assertEqual(self.solution.reverseList(head), expected)


test = TestSolution()
print(test)
