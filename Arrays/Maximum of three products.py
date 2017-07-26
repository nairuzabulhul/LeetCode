
arr = [1,2,3, 4, 5]

# output is 60 

def max_three_products(arr):
    
    
    # get the mins together, get the maxs together
    # set maxs and mins
    min1, min2, min3 = float('inf'), float('inf'), float('inf')
    max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
    
    
    for i in arr:
        
        if i <= min1:
            min3 = min2 
            min2 = min1 
            min1 = i 
            
        elif i<= min2:
            min3 = min2 
            min2 = i 
            
        elif i <= min3:
            min3 = i 
            
        if i >= max1:
            max3 = max2 
            max2 = max1
            max1 = i 
            
        elif i >= max2:
            max3 = max2
            max2 = i 
            
        elif i >= max3:
            max3 = i 
            
    return max(min1 * min2 * min3 , max1 * max2 * max3 )


print max_three_products(arr)
