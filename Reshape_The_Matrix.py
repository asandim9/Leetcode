class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        count = 0
        for i in mat:
            count += len(i)
            
        if count != r*c:
            return mat
        else:
            temp = []
            for i in mat:
                for j in i:
                    temp.append(j)
            res = []
            for i in range(0,len(temp),c):
                res.append(temp[i:i+c])
                
            return res
            
        
