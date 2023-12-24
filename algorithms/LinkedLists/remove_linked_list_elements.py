from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.head = None

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        global prev

        self.head = head
        current = head
        while current is not None:

            if current.val == val:
                prev.next = current.next

            prev = current
            current = current.next


        return self.head


obj = Solution()
[1, 2, 6, 3, 4, 5, 6]
list_node_obj = ListNode()
list_node_obj.val = 1
list_node_obj.next = ListNode()
list_node_obj.next.val = 6
list_node_obj.next.next = ListNode()
list_node_obj.next.next.val = 6
list_node_obj.next.next.next = ListNode()
list_node_obj.next.next.next.val = 4
list_node_obj.next.next.next.next = ListNode()
list_node_obj.next.next.next.next.val = 5
list_node_obj.next.next.next.next.next = ListNode()
list_node_obj.next.next.next.next.next.val = 6

res = obj.removeElements(list_node_obj, 6)
print("Res: ", res.val)
print("Res1: ", res.next.val)
print("Res2: ", res.next.next.val)
print("Res3: ", res.next.next.next.val)
print("Res4: ", res.next.next.next.next.val)
