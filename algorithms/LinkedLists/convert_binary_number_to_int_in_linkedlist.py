class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:


    def getDecimalValue(self, head: ListNode) -> int:
        value_list = []
        value_list.append(head.val)
        while head.next is not None:
            value_list.append(head.next.val)
            head = head.next

        _s = "".join(map(str, value_list))
        number = int(_s, 2)
        return number



obj = Solution()
list_node_obj = ListNode()
list_node_obj.val = 1
list_node_obj.next = ListNode()
list_node_obj.next.val = 0
list_node_obj.next.next = ListNode()
list_node_obj.next.next.val = 1

res = obj.getDecimalValue(head=list_node_obj)
print("Res: ", res)
