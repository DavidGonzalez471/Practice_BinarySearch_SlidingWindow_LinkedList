#Solution finds the halfway point of the linked list and splits the list in two and traverses the right side backwards combining the two lists.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        right = slow.next
        prev = slow.next = None
        while right:
            temp = right.next
            right.next = prev
            prev = right
            right = temp
            print(prev)
            print(right)
        
        left,right = head, prev
        while right:
            temp1, temp2 = left.next, right.next
            left.next = right
            right.next = temp1
            left, right = temp1, temp2
