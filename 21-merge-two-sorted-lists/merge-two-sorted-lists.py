class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1)
        current = dummy
        
        i, j = list1, list2
        
        while i is not None and j is not None:
            if i.val <= j.val:
                current.next = i
                i = i.next
            else:
                current.next = j
                j = j.next
            current = current.next
            
        if i is not None:
            current.next = i
        else:
            current.next = j
            
        return dummy.next