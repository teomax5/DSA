class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #if head is null return null
        #call reverseList with head.next and store the result in a variable
        #set head.next.next to head
        #set head.next to null
        #return the newhead