class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #loop thorught the list
        #for ith elementcheck jth elment from i+1 to end of the list
            #if ith element is equal to jth element return true
        #if the loop ends return false