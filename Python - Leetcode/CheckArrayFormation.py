# Problem name
# Check Array Formation Through Concatenation
class Solution:    
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        index = {} 
        for i in range(len(pieces)): 
            piece = pieces[i]
            f_item_of_piece = piece[0]
            index[f_item_of_piece] = i 
        
        canForm = True 
        while canForm and len(arr) != 0: 
            next_item = arr[0]
            checkSubInd = index.get(next_item,None)
            if checkSubInd == None:
                return False
            checkSub = pieces[checkSubInd]
            if checkSub == arr[0:len(checkSub)]: 
                arr = arr[len(checkSub):]
            else:
                canForm = False 
                
        return canForm 