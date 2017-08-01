def pluse_one(digits):
  
  
  if len(digits) == 0 :
      return None
      
  output = []
  
  for i in digits:
    output.append(str(i)) 
    
  join_nums = int(('').join(output)) + 1 
  
  final = []
  
  for n in str(join_nums):
    final.append(int(n))
    
  return final


#Testing
#arr= [9,9,9]
#print pluse_one(arr)

############################################################################################################################

##Solution 2 : ##optimized & shorter :
def plusOne2(digits): 
 
           digits = [str(x) for x in digits] 
           print digits
           
           num = int(''.join(digits)) + 1 
           print num
           
           return [int(x) for x in str(num)] 

#Testing
#srr= [9,9,9]
#print plusOne2(srr)
