# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    """Given the head of a linked list, remove the nth node from the end of the list and return its head.

        Example 1:
            Input: head = [1,2,3,4,5], n = 2
            Output: [1,2,3,5]
       
        Example 2:
            Input: head = [1], n = 1
            Output: []
        
        Example 3:
            Input: head = [1,2], n = 1
            Output: [1]

        Constraints:
            The number of nodes in the list is sz.
            1 <= sz <= 30
            0 <= Node.val <= 100
            1 <= n <= sz
    """
    def removeNthFromEnd(self, head:ListNode,n: int):
        dummy = ListNode()
        print("dummy.....",dummy.val)
        print("dummy.....",dummy.next)
        L = dummy
        L.next = head
        print("dummy.....2",dummy.val)
        print("dummy.....2",dummy.next)
        print("L.....",L.val)
        print("L.....",L.next)
        R = head

        while n > 0 and R:
            print("r.....",R.val)
            R = R.next
            n -= 1
        print(R.val)
        while R:
            L = L.next
            R = R.next
        
        L.next = L.next.next

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
        

def linkdlist_to_list(head):
    result = []
    current = head
    while current is not None:
        result.append(current.val)
        current = current.next
    return result
        


linkd_list = create_linkdlist([1,2,3,4,5])
n = 2
s = Solution()
res = s.removeNthFromEnd(linkd_list,n)
lis = linkdlist_to_list(res)
print(lis)