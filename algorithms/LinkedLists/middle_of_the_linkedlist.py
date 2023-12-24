from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        old_head = head
        length_counter = 0
        if head.val:
            length_counter += 1
        while head.next is not None:
            if head.next.val:
                length_counter += 1
            head = head.next
        middle_of_node = length_counter // 2 + 1
        result_of_nodes = []
        node_counter = 1
        print("middle: ", middle_of_node)
        while old_head.next is not None:
            print("Node: ", old_head.val, node_counter, middle_of_node)
            if node_counter == middle_of_node:
               return old_head
            node_counter += 1
            old_head = old_head.next
        return old_head


obj = Solution()
list_node_obj = ListNode()
list_node_obj.val = 1
list_node_obj.next = ListNode()
list_node_obj.next.val = 2
list_node_obj.next.next = ListNode()
list_node_obj.next.next.val = 3
list_node_obj.next.next.next = ListNode()
list_node_obj.next.next.next.val = 4
list_node_obj.next.next.next.next = ListNode()
list_node_obj.next.next.next.next.val = 5


res = obj.middleNode(head=list_node_obj)
print("Res: ", res.val)
