# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
        You are given the heads of two sorted linked lists list1 and list2.
        Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
        Return the head of the merged linked list.

        Example 1:
            Input: list1 = [1,2,4], list2 = [1,3,4]
            Output: [1,1,2,3,4,4]

        Example 2:
            Input: list1 = [], list2 = []
            Output: []

        Example 3:
            Input: list1 = [], list2 = [0]
            Output: [0]

        Constraints:
            The number of nodes in both lists is in the range [0, 50].
            -100 <= Node.val <= 100
            Both list1 and list2 are sorted in non-decreasing order.
    """

    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to serve as the start of the merged list
        dummy = ListNode()
        tail = dummy

        # Merge the two lists
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # If either list runs out, attach the remaining elements of the other list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next


def create_linkdlist(arr):
    if not arr:
        return None
    
    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        new_node = ListNode(val)
        current.next = new_node
        current = current.next
    return head

def list_to_linkdlist(head):
    result = []
    current = head
    while current is not None:
        result.append(current.val)
        current = current.next
    return result

# Create linked lists from arrays
linkd_list = create_linkdlist([1,2,4])
linkd_list2 = create_linkdlist([1,3,4])

# Merge the linked lists
s = Solution()
res = s.mergeTwoLists(linkd_list, linkd_list2)

# Convert the merged linked list back to a list and print the result
lis = list_to_linkdlist(res)
print(lis)
