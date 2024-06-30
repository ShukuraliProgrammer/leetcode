from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        list1_s = []
        list2_s = []
        while list1 or list2:
            if list1:
                list1_s.append(list1.val)
                list1 = list1.next
            list2_s.append(list2.val)
            list2 = list2.next
        result = sorted(list1_s + list2_s)

        i = 1
        new_llist = ListNode(result[0])
        cur_node = new_llist
        print("length", len(result))
        while i < len(result):
            cur_node.next = ListNode(result[i])
            cur_node = cur_node.next
            i += 1
            print(i)
        return new_llist

obj = Solution()
list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)
r = obj.mergeTwoLists(list1, list2)
print(r.val)
print(r.next.val)
print(r.next.next.val)
print(r.next.next.next.val)
print(r.next.next.next.next.val)
print(r.next.next.next.next.next.val)
