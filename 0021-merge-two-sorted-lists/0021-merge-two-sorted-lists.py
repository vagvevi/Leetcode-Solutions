# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        
        # While both lists are not empty
        while list1 and list2:
            # Compare the values in the current nodes of both lists
            if list1.val <= list2.val:
                # If list1's value is smaller, attach it to the current node
                current.next = list1
                list1 = list1.next
            else:
                # If list2's value is smaller, attach it to the current node
                current.next = list2
                list2 = list2.next
            
            # Move to the next node in the merged list
            current = current.next
        
        # If one of the lists is not empty, attach it to the merged list
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        # Return the merged list, starting from dummy.next (the real head)
        return dummy.next

        