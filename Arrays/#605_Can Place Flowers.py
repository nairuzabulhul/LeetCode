
def flower_bed(num, arr):
  
  if len(arr) == 0:
    return None
  
  
  for i in range (len(arr)):
    
    if arr[num] == 0 and arr[num-1] == 1 or arr[num] == 0 and arr[num +1 ] == 1 :
      
      return True
      
    else:
      
      return False
      

#Testing:
#=2
#rr= [1,0,0,0,1]
#rint flower_bed(n,arr)
#output : False if n = 2 , and True if n =1 
