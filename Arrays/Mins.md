def second_smallest(arr_nums):
    
    """
    Function that returns first, second and third smallest numbers in an array 
    """
    
    
    # set the variables 
    
    first_min = float('inf')
    second_min = float('inf')
    third_min = float('inf')
    fourth_min = float('inf')
    
    # loop through the arr
    for i  in arr_nums:
        
        # to find the minimum numbers,
        # third number becomes second
        #second becomes first 
        #first is = i 
        
        if i <= first_min:
            fourth_min = third_min 
            third_min = second_min
            second_min = first_min
            first_min = i
        
        elif i <= second_min:
            fourth_min = second_min 
            second_min = i 
            
        elif i <= third_min:
            foutrth_min = third_min 
            third_min = i 
            
        elif i <= fourth_min:
            fourth_min  = i 

    return first_min, second_min, third_min,fourth_min

print(second_smallest([1, 2, -8, -10, -9]))
