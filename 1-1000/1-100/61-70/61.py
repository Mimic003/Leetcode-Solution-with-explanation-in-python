class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not k:
            return head

        length = 1

        tail = head


        while tail.next:
            tail = tail.next 
            length += 1
        
        k %= length

        if k < 1:
            return head

        r = head
        
        for _ in range(length - k-1):
            r = r.next

        newHead = r.next
        r.next = None
        tail.next = head


        return newHead