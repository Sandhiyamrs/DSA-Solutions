class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head, n):
    dummy = ListNode(0, head)
    first = second = dummy
    for _ in range(n+1):
        first = first.next
    while first:
        first = first.next
        second = second.next
    second.next = second.next.next
    return dummy.next

# Helper to print list
def print_list(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

# Example usage
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
new_head = remove_nth_from_end(head, 2)
print("Output:", end=" ")
print_list(new_head)
