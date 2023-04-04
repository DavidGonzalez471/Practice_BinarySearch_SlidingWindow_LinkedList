#Reversing the linked list iteratively until we get to the end and get a null value then iterating backwards through the list.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, head = None, head

        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

#recursive solution
class Solution:
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    newHead = head
    if head.next:
        newHead = self.reverseList(head.next)
        head.next.next = head
    head.next = None

    return newHead
