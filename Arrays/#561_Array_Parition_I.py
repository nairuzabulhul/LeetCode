def array_partiton(num,arr):
  
  
  output = []
  sum_n = 0 
  array_size = len(arr)
  
  if array_size >= num :
    
    for i in arr:
        sub_arr1 = arr[:num]
        sub_arr2 = arr[num:]
        
    output.append(sub_arr1)    
    output.append(sub_arr2)
    
  for n in output:
    sum_n += min(n)
  return sum_n 
  
  
n = 2
arr = [1,2,3,4]
print array_partiton(n ,arr)



##Testing ::

def array_partiton(num, arr):  

  sum_n = 0   
  array_size = len(arr)
  sorted_arr = sorted(arr)
  res = []

  # this loops if 0 in the array
  for n in sorted_arr:
        if n != 0:
            res.append(n)
  
  size = len(res)/num 
  
  if size == 2 and array_size > size:
    
      k = [res[i:i+size] for i  in range(0, len(res), size)]
     
      # loop through the second array and get the min of each sub array 
      for m in k :
        sum_n += min(m)
      return sum_n
     
  elif size == 3:
    
     size = 2
     k = [res[i:i+size] for i  in range(0, len(res), size)]
     
     for m in k :
       sum_n += min(m)
     return sum_n
    
  else:
          return min(res)   
    
 
#Test cases:  
n = 2
arr = [1,4,3,2] #output 4
#arr =[1,1] # output 1
#arr = [7,3,1,0,0,6] # output 7 
#arr = [9,1,5,6,7,2] #output 13
print array_partiton(n ,arr)


## Acceptable solution by Leetcode:
def arrayPairSum(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # sorte the array 
        new_nums = sorted(nums)
        
        
        return sum(new_nums[::2])
    


