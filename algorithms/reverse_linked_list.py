from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def __init__(self) -> None:
        self.head = None

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        prev = None
        curr = head
        items = []
        while curr is not None:
            next_node = curr.next
            curr.next = prev
            prev = curr
            items.append(curr.val)
            curr = next_node

        reversed_items = items[::-1]
        new_node = ListNode(reversed_items[0])
        self.head = new_node
        for i in range(1, len(reversed_items)):
            new_node.next = ListNode(reversed_items[i])
            new_node = new_node.next
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

res = obj.reverseList(list_node_obj)
print("Res: ", res.val)
print("Res1: ", res.next.val)
print("Res2: ", res.next.next.val)
print("Res3: ", res.next.next.next.val)
print("Res4: ", res.next.next.next.next.val)
print("Res5: ", res.next.next.next.next.next.val)
print("Res6: ", res.next.next.next.next.next.next.val)