# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        """
        Initialize a node in the singly linked list.
        
        Parameters:
        val (int): The value of this node. Defaults to 0.
        next (ListNode): The reference to the next node. Defaults to None.
        """
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted singly linked lists into one sorted list.
        
        This function takes two linked lists as input and returns a new merged linked list. The merging is done based on the value of each node in the original lists. If the values are equal, the nodes from both lists will be placed next to each other in the order they appear in the original lists.
        
        Parameters:
        list1 (ListNode): The first sorted linked list.
        list2 (ListNode): The second sorted linked list.
        
        Returns:
        ListNode: The head of the merged linked list.
        """
        # Create a dummy node to serve as a placeholder for our new merged list
        dummy = ListNode()
        
        # Initialize our "new" pointer to point at the dummy node
        new = dummy

        # Loop through both lists until we've processed all nodes from either one (or both)
        while list1 and list2:
            # Compare the values of the current nodes in both lists
            if list1.val < list2.val:
                # If the value of the current node in list1 is smaller, add it to our merged list
                new.next = list1
                # Move the pointer forward in list1 to point at the next node
                list1 = list1.next
            else:
                # Otherwise, add the node from list2 to our merged list
                new.next = list2
                # Move the pointer forward in list2 to point at the next node
                list2 = list2.next
            
            # Move our "new" pointer forward to point at the last added node
            new = new.next
        
        # If there are any remaining nodes in list1, add them to our merged list (if there aren't any)
        if list1:
            new.next = list1
        # Otherwise, if there are any remaining nodes in list2, add them to our merged list (if there aren't any)
        elif list2:
            new.next = list2
            
        # Return the head of our merged linked list (which is the node after our dummy node)
        return dummy.next
