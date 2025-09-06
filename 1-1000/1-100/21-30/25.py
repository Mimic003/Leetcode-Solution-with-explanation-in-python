from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        """
        1. start at dummy = ListNode(next=head)
        2. search the next k elements repeatly
        3. if it does not reach `None`, reverse the nodes in between, return the new start and new end node
        4. connect the node, and go for the next k elements
        5. if it somehow reaches `None`, return head
        O(2n), O(1)
        """

        def reverseNode(node, k):
            cur = node
            prev = None

            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            
            node.next = cur
            return prev
        
        dummy = ListNode(next=head)
        cur = dummy

        while cur:
            start = cur
            for _ in range(k):
                start = start.next
                if not start:
                    return dummy.next
            temp = cur.next
            cur.next = reverseNode(cur.next, k)
            cur = temp
        
        return dummy.next