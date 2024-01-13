import linkedlist

# **** EX1 ****
# LL: Find Middle Node ( ** Interview Question)
# Implement the find_middle_node method for the LinkedList class.
# The find_middle_node method should return the middle node in the linked list WITHOUT using the length attribute.
# If the linked list has an even number of nodes, return the first node of the second half of the list.
# Keep in mind the following requirements:
# The method should use a two-pointer approach, where one pointer (slow) moves one node at a time and the other pointer (fast) moves two nodes at a time.
# When the fast pointer reaches the end of the list or has no next node, the slow pointer should be at the middle node of the list.
# The method should return the middle node or the first node of the second half of the list if the list has an even number of nodes.
# The method should only traverse the linked list once.  In other words, you can only use one loop.

def find_middle_node(linkedlist):
    one_step = linkedlist.head
    two_steps = linkedlist.head
    while two_steps and two_steps.next:
        one_step = one_step.next
        two_steps = two_steps.next.next
    return one_step


my_linked_list = linkedlist.LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print( "find_middle_node: ", find_middle_node(my_linked_list).value )

# **** EX2 ****
# LL: Has Loop ( ** Interview Question)
# Write a method called has_loop that is part of the linked list class.
# The method should be able to detect if there is a cycle or loop present in the linked list.
# The method should utilize Floyd's cycle-finding algorithm, also known as the "tortoise and hare" algorithm, to determine the presence of a loop efficiently.
# The method should follow these guidelines:
# Create two pointers, slow and fast, both initially pointing to the head of the linked list.
# Traverse the list with the slow pointer moving one step at a time, while the fast pointer moves two steps at a time.
# If there is a loop in the list, the fast pointer will eventually meet the slow pointer. If this occurs, the method should return True.
# If the fast pointer reaches the end of the list or encounters a None value, it means there is no loop in the list. In this case, the method should return False.

def has_loop(linkedlist):
    one_step = linkedlist.head
    two_steps = linkedlist.head
    while two_steps and two_steps.next:
        one_step = one_step.next
        two_steps = two_steps.next.next
        if one_step == two_steps:
            return True
    return False


my_linked_list_1 = linkedlist.LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print("my_linked_list_1: has_loop is ", has_loop(my_linked_list_1) ) # Returns True




my_linked_list_2 = linkedlist.LinkedList(1)
my_linked_list_2.append(2)
my_linked_list_2.append(3)
my_linked_list_2.append(4)
print("my_linked_list_2: has_loop is ", has_loop(my_linked_list_2) ) # Returns False
