class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        def combi(ind,target,arr):
            if target == 0:
                ans.append(arr[:])
                return 
            if ind == len(candidates):
                return
            
            if ind < len(candidates) and candidates[ind] <= target:
                arr.append(candidates[ind])
                combi(ind,target-candidates[ind],arr)
                arr.pop(-1)
            combi(ind+1,target,arr)
        combi(0,target,[])
        return ans 