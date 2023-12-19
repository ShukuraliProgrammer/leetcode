from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self) -> None:
        self.head = None

    def append(self, value: any) -> None:
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_list = [l1.val]
        l2_list = [l2.val]

        while l1.next is not None:
            l1_list.append(l1.next.val)
            l1 = l1.next
        while l2.next is not None:
            l2_list.append(l2.next.val)
            l2 = l2.next

        summ = int("".join(map(str, l1_list[::-1]))) + int("".join(map(str, l2_list[::-1])))
        my_list = Solution()
        [my_list.append(int(x)) for x in str(summ)[::-1]]

        return my_list.head



obj = Solution()
list_node_obj = ListNode()
list_node_obj.val = 9
list_node_obj.next = ListNode()
list_node_obj.next.val = 9
list_node_obj.next.next = ListNode()
list_node_obj.next.next.val = 9
list_node_obj.next.next.next = ListNode()
list_node_obj.next.next.next.val = 9
list_node_obj.next.next.next.next = ListNode()
list_node_obj.next.next.next.next.val = 9
list_node_obj.next.next.next.next.next = ListNode()
list_node_obj.next.next.next.next.next.val = 9
list_node_obj.next.next.next.next.next.next = ListNode()
list_node_obj.next.next.next.next.next.next.val = 9

list2_node_obj = ListNode()
list2_node_obj.val = 9
list2_node_obj.next = ListNode()
list2_node_obj.next.val = 9
list2_node_obj.next.next = ListNode()
list2_node_obj.next.next.val = 9
list2_node_obj.next.next.next = ListNode()
list2_node_obj.next.next.next.val = 9

res = obj.addTwoNumbers(l1=list_node_obj, l2=list2_node_obj)
print("Res: ", res.val)
print("Res1: ", res.next.val)
print("Res2: ", res.next.next.val)
print("Res3: ", res.next.next.next.val)
print("Res4: ", res.next.next.next.next.val)
print("Res5: ", res.next.next.next.next.next.val)

