#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        newhead = None
        while(head != None):
            dum = head.next
            head.next = newhead
            newhead = head
            head = dum
        return newhead
# @lc code=end

