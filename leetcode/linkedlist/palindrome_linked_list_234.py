# 234. Palindrome Linked List
# Easy
#
# 9863
#
# 600
#
# Add to List
#
# Share
# Given the head of a singly linked list, return true if it is a palindrome.
#
# Example 1:
# Input: head = [1,2,2,1]
# Output: true
#
# Example 2:
# Input: head = [1,2]
# Output: false

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        slow = self.reverse_list(slow)
        fast = head
        while slow is not None:
            if fast.val is not slow.val:
                return False

            fast = fast.next
            slow = slow.next

        return True

    def reverse_list(self, head):
        prev = None
        while head is not None:
            next = head.next
            head.next = prev
            prev = head
            head = next

        return prev
