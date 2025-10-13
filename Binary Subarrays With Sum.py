class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        def numberofsubarray(nums,goal):
            if goal<0:
                return 0
            l,r,sum1,count=0,0,0,0
            while r < len(nums):
                sum1+=nums[r]
                while sum1>goal:
                    sum1-=nums[l]
                    l+=1
                count=count+((r-l)+1)
                r+=1
            return count
        a=numberofsubarray(nums,goal)-numberofsubarray(nums,goal-1)
        return a