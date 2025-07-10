class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        st=[]
        for i in range(0,len(num)):
            while(len(st)!=0 and k>0 and st[-1] > num[i]):
                st.pop()
                k-=1
            st.append(num[i])
        while(k>0):
            st.pop()
            k-=1
        if len(st)==0:
            return "0"
        res=""
        while(len(st)!=0):
            res=res+st[-1]
            st.pop()
        rev=res[::-1]
        ans=int(rev)
        return str(ans)