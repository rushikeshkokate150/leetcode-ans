class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def nofosubarray(nums,k):
            l,r,cnt=0,0,0
            mpp = {}
            while r<len(nums):
                if nums[r] not in mpp:
                    mpp[nums[r]] = 1
                else:
                    mpp[nums[r]]+=1
                
                while len(mpp) > k:
                    
                    mpp[nums[l]]-=1
                    
                    if mpp[nums[l]] == 0:
                        del mpp[nums[l]]
                    l+=1
                    
                cnt = cnt + (r-l+1)
                r+=1
            
            return cnt
        
        return nofosubarray(nums,k) - nofosubarray(nums,k-1)