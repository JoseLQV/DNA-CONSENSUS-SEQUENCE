countData = [
{'A': 3, 'G': 1, 'C': 0, 'T': 0}, 
{'A': 3, 'G': 0, 'C': 1, 'T': 0}, 
{'A': 0, 'G': 0, 'C': 0, 'T': 4}, 
{'A': 0, 'G': 1, 'C': 3, 'T': 0}, 
{'A': 1, 'G': 0, 'C': 2, 'T': 1}, 
{'A': 0, 'G': 4, 'C': 0, 'T': 0}, 
{'A': 1, 'G': 0, 'C': 3, 'T': 0}, 
{'A': 0, 'G': 1, 'C': 0, 'T': 3}, 
{'A': 2, 'G': 0, 'C': 1, 'T': 1}, 
{'A': 0, 'G': 4, 'C': 0, 'T': 0}]

  
def funct(countData):
    map = {'A': 0, 'G': 1, 'C': 3, 'T': 0}
    
    listed = list(map.items())
    newList = []
    i = 0
    while len(listed) != 0:
        tuple = listed[0]
        max_tuple = tuple
        for j in range(i+1,len(listed)):
            next_tuple = listed[j]
            if next_tuple[1] > tuple[1]:
                max_tuple = next_tuple
                
        listed.remove(max_tuple)
        newList.append(max_tuple)
            
            
            
        
    return newList


print(funct(countData))
    
    
    
    

        
        
        
        
        
        
# def key_function(x):
#     return x[1]
# key_function([1,2])
# key_function = lambda x: x[1]
# key_function([1,2])

# def sort_it(countData):
#     val = {'A': 0, 'G': 1, 'C': 3, 'T': 0}
#     popeye = list(val.items())
#     popeye.sort(reverse=True, key=lambda x: x[1])
#     # import pdb; pdb.set_trace()
#     val = {x:y for x,y in popeye}           
            
#     return countData

# sortedData = sort_it(countData)
# print(sortedData)

     
            
        