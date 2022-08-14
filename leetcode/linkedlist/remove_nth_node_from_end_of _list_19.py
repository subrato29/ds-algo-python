# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int):
        if head.next is None:
            return None

        first = head
        second = head
        counter = 1

        while counter <= n:
            second = second.next
            counter += 1

        if second is None:
            head.val = head.next.val
            head.next = head.next.next
            return head

        while not second.next is None:
            first = first.next
            second = second.next

        first.next = first.next.next

        return head
