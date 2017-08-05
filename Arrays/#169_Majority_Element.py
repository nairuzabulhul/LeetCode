
 def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        output = {}
        arr_len = len(nums)/ 2
        
        for i in nums:

                if output.has_key(i) :

                        output[i] += 1
                        
                        if output[i] > arr_len:
                               
                                return i 
                
                else:
                        output[i] = 1
                        
        return i 
        
#arr = [2,4,5,6,3,2,3,7,2] # output 2    
arr =[1]                   # output 1
print marjority_elements(arr)                          
        
 ################################################################################################
 class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        return sorted(nums)[len(nums) / 2]
        
        
        
Complexity:
O(nlogn) time
O(1) space
 
 
