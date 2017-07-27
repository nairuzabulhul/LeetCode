arr = [2,8,1]


def max_third_num(arr):
  
  """Function that returns the third max number
  """
  max3 = float('-inf')
  max2 = float('-inf')
  max1 = float('-inf')
  
  # check for non- empty array 
  if len(arr) == 0:
    return None
    
  # loop through the array 
  elif len(arr) >= 3:
    for i in arr :
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
    if len(arr) <= 2  :
      return max(arr)

  

  
  
print max_third_num(arr)
