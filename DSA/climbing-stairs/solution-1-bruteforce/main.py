class solution:
    def climbStairs(self,n:int) -> int:
        #start from step 0
        #define a recursive function that takes the current step i as an argument
        #if the current step is equal to n return 1
        #if the current step is greater than n return 0
        #otherwise return the sum of the recursive function called with i+1 and i+2
        #call the recursive function with 0 as the argument and return the result