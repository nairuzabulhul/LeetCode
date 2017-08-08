class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
    
            return []
    
        # sort the array 
        sorted_arr = sorted(nums)
        
        first_num = -1
        last_num = -1 

        # loop through the arr:
        for index in range(len(nums)):

            # the arr elemetns are not == sorted array 
            if  nums[index] != sorted_arr[index]:

                # mark the first unequal element 
                if first_num == -1 :
                    first_num = index 

                # mark last index of the unequal element   
                last_num = index 


          # get the difference between the first element and 
          # last element 
          # +1 is added because we start from 0 index
        return last_num - first_num + 1 if last_num != -1 else 0 


#Testing 
#arr=[5,9,8,7]     # output 3 
#arr = [2,1]      # output 2
#arr= [1,2,3,4]   # output 0    
arr= [2,6,4,8,10,9,15]  # otuput 5 
