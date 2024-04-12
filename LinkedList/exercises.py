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


# **** EX3 ****
# LL: Find Kth Node From End ( ** Interview Question)
# Implement the find_kth_from_end function, which takes the LinkedList (ll) and an integer k as input, and returns the k-th node from the end of the linked list WITHOUT USING LENGTH.
# Given this LinkedList:
# 1 -> 2 -> 3 -> 4
# If k=1 then return the first node from the end (the last node) which contains the value of 4.
# If k=2 then return the second node from the end which contains the value of 3, etc.
# If the index is out of bounds, the program should return None.
# The find_kth_from_end function should follow these requirements:
# The function should utilize two pointers, slow and fast, initialized to the head of the linked list.
# The fast pointer should move k nodes ahead in the list.
# If the fast pointer becomes None before moving k nodes, the function should return None, as the list is shorter than k nodes.
# The slow and fast pointers should then move forward in the list at the same time until the fast pointer reaches the end of the list.
# The function should return the slow pointer, which will be at the k-th position from the end of the list.

def find_kth_from_end(linkedlist, k):
    slow = linkedlist.head
    fast = linkedlist.head 
    # 1. move fast pointer to the k node first and leave it there
    for _ in range(k):
        if fast is None:
            return None # if in one iteration, fast pointer become None because the length of the linkedlist is shorter that k
        fast = fast.next

    # 2. now start moving both slow and fast at the same time
    while fast:
        fast = fast.next
        slow = slow.next
        # slow pointer will be at the position of len(linkedlist) - k
    return slow

my_linked_list = linkedlist.LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)

k = 4
result = find_kth_from_end(my_linked_list, k)
print(f"find {k}th from end: {result.value}")

# Getting length of the linked list
def len_of_ll(ll):
    temp = ll.head
    count = 1
    while temp.next is not None:
        temp = temp.next
        count += 1
    return count

my_linked_list = linkedlist.LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
print(len_of_ll(my_linked_list))


# **** EX4 ****
# LL: Partition List ( ** Interview Question)
# ⚠️ CAUTION: Advanced Challenge Ahead!
# This Linked List problem is significantly more challenging than the ones we've tackled so far. It's common for students at this stage to find this exercise demanding, so don't worry if you're not ready to tackle it yet. It's perfectly okay to set it aside and revisit it later when you feel more confident.
# If you decide to take on this challenge, I strongly advise using a hands-on approach: grab a piece of paper and visually map out each step.
# This problem requires a clear understanding of how elements in a Linked List interact and move. By now, you've observed numerous Linked List animations in the course, which have prepared you for this moment.
# This exercise will be a true test of your ability to apply those concepts practically. Remember, patience and persistence are key here!
# Now, here is the exercise:
# ___________________________________
# Implement the partition_list member function for the LinkedList class, which partitions the list such that all nodes with values less than x come before nodes with values greater than or equal to x.
# Note:  This linked list class does NOT have a tail which will make this method easier to implement.
# The original relative order of the nodes should be preserved.
# Details:
# The function partition_list takes an integer x as a parameter and modifies the current linked list in place according to the specified criteria. If the linked list is empty (i.e., head is null), the function should return immediately without making any changes.
# Example 1:
# Input:
# Linked List: 3 -> 8 -> 5 -> 10 -> 2 -> 1 x: 5
# Process:
# Values less than 5: 3, 2, 1
# Values greater than or equal to 5: 8, 5, 10
# Output:
# Linked List: 3 -> 2 -> 1 -> 8 -> 5 -> 10
# Example 2:
# Input:
# Linked List: 1 -> 4 -> 3 -> 2 -> 5 -> 2 x: 3
# Process:
# Values less than 3: 1, 2, 2
# Values greater than or equal to 3: 4, 3, 5
# Output:
# Linked List: 1 -> 2 -> 2 -> 4 -> 3 -> 5
# Tips:
# While traversing the linked list, maintain two separate chains: one for values less than x and one for values greater than or equal to x
# Use dummy nodes to simplify the handling of the heads of these chains.
# After processing the entire list, connect the two chains to get the desired arrangement.
# Note:
# The solution must maintain the relative order of nodes. For instance, in the first example, even though 8 appears before 5 in the original list, the partitioned list must still have 8 before 5 as their relative order remains unchanged.
# Note:
# You must solve the problem WITHOUT MODIFYING THE VALUES in the list's nodes (i.e., only the nodes' next pointers may be changed.)

def partition_list():
    return



