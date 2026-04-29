class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #if list1 is null return list2
        #if list2 is null return list1
        #if list1.val is less than list2.val
            #set list1.next to mergeTwoLists with list1.next and list2
            #return list1
        #else
            #set list2.next to mergeTwoLists with list1 and list2.next
            #return list2