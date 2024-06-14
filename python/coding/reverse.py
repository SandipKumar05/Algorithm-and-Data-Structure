class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverseKGroup(head, k):
    # Function to reverse a part of the linked list
    def reverseLinkedList(head, k):
        new_head = None
        ptr = head
        while k > 0:
            next_node = ptr.next
            ptr.next = new_head
            new_head = ptr
            ptr = next_node
            k -= 1
        return new_head
    
    count = 0
    ptr = head
    
    # Count the number of nodes in the linked list
    while ptr is not None and count != k:
        ptr = ptr.next
        count += 1
    
    # If we have k nodes, then we reverse them
    if count == k:
        # Reverse the first k nodes of the list and get the reversed list's head
        reversed_head = reverseLinkedList(head, k)
        
        # Recursively call the function with the rest of the list and attach it to the end of the first k nodes
        head.next = reverseKGroup(ptr, k)
        
        # Return the new head of the reversed list
        return reversed_head
    
    # If we don't have k nodes, return the head as is
    return head

# Helper function to print the linked list
def printList(head):
    while head is not None:
        print(head.value, end=" -> ")
        head = head.next
    print("None")

# Example Usage
# Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("Original list:")
printList(head)

# Reversing in groups of 2
k = 2
reversed_head = reverseKGroup(head, k)

print(f"Reversed list in groups of {k}:")
printList(reversed_head)

# Reversing in groups of 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 3
reversed_head = reverseKGroup(head, k)

print(f"Reversed list in groups of {k}:")
printList(reversed_head)
