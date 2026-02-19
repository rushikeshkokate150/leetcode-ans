class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans=[]
        def combi2(ind,target,arr):
            if target == 0:
                ans.append(arr[:])
                return 
                
            if ind == len(candidates):
                return
            for i in range(ind,len(candidates)):
                if candidates[i] > target:
                    break
                elif i>ind and candidates[i]==candidates[i-1]:
                    continue
                
                arr.append(candidates[i])
                combi2(i+1,target-candidates[i],arr)
                arr.pop()
                
        combi2(0,target,[])
        
        return ans 