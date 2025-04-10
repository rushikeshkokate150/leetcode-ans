#include<bits/stdc++.h>
class Solution {
public:
    bool count_of_flower(vector<int>& bloomDay,int mid,int k,int m){
        int count=0;
        int book=0;
        for(int i=0;i<bloomDay.size();i++){
            if(bloomDay[i]<=mid) 
            {
                count++;
            }
            else
            {  
            book+=(count/k);
            count=0;
            }
        }
        book+=(count/k);
        return book>=m;
    }

    int minDays(vector<int>& bloomDay, int m, int k) {
        int n=bloomDay.size();
        long long val=m* 1LL* k* 1LL;
        if(val>n) return -1;
        int low=*min_element(bloomDay.begin(),bloomDay.end());
        int high=*max_element(bloomDay.begin(),bloomDay.end());
        while(low<=high){
            int mid=(low+high)/2;
            if(count_of_flower(bloomDay,mid,k,m)==true)
            { 
            high=mid-1;
            }
            else low=mid+1;
            
        }
        return low;

    }
};