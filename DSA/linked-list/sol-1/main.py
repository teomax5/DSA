class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #create a set to store the visited nodes
        #start from the head node and move thorugh the list node at a time
            #if the current node is in the set return true
            #otherwise add the current node to the set
        #if you reach null return false    