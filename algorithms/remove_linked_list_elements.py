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
        current = head
        if current.val == val:
            self.head = current.next
        else:
            self.head = current
            while current:

                if current.val == val:
                    break

                prev = current
                current = current.next
            if current is None:
                return
            prev.next = current.next
            current = None

        return self.head



obj = Solution()

list_node_obj = ListNode()
list_node_obj.val = 9
list_node_obj.next = ListNode()
list_node_obj.next.val = 8
list_node_obj.next.next = ListNode()
list_node_obj.next.next.val = 7
list_node_obj.next.next.next = ListNode()
list_node_obj.next.next.next.val = 6
list_node_obj.next.next.next.next = ListNode()
list_node_obj.next.next.next.next.val = 5
list_node_obj.next.next.next.next.next = ListNode()
list_node_obj.next.next.next.next.next.val = 4
list_node_obj.next.next.next.next.next.next = ListNode()
list_node_obj.next.next.next.next.next.next.val = 3

res = obj.removeElements(list_node_obj, 4)
print("Res: ", res.val)
print("Res1: ", res.next.val)
print("Res2: ", res.next.next.val)
print("Res3: ", res.next.next.next.val)
print("Res4: ", res.next.next.next.next.val)
print("Res5: ", res.next.next.next.next.next.val)
