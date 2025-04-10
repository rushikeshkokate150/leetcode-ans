#include<bits/stdc++.h>
class Solution {
public:
bool sum1(vector<int>& nums,int val ,int threshold){
    int cnt=0;
    for(int i=0;i<nums.size();i++){
        cnt+=ceil((double)(nums[i])/(double)(val));
    }
    return cnt<=threshold;
}
    int smallestDivisor(vector<int>& nums, int threshold) {
        int n=nums.size();
        if (n>threshold) return -1;
        int low=1;
        int high=*max_element(nums.begin(),nums.end());
        
        while(low<=high){
            int mid=(low+high)/2;
            if(sum1(nums,mid,threshold)==true) high=mid-1;
            else low=mid+1;
        }
        return low;
    }
};