arr = [2,8,1]


class Solution(object):
    
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        max3 = float('-inf')
        max2 = float('-inf')
        max1 = float('-inf')

        new_nums = set(nums)
        
        # check for non- empty array 
        if len(nums) == 0:
                return None

          # loop through the array 
        elif len(new_nums) >= 3:
            
            for i in new_nums :
            # if the length is greater than 2, return the 3rd max number
                if i >= max1:
                    max3 = max2 
                    max2 = max1 
                    max1 =i 

                elif i >= max2 :
                    max3 = max2 
                    max2 = i 

                elif i >= max3 :
                    max3 = i 

            return max3   

        else:
            if len(new_nums) <= 2  :
                return max(new_nums)

  
