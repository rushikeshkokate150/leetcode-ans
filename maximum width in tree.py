# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        ans = 0
        if not root:
            return ans

        q = deque([[root,0]])
        
        while q:
            size = len(q)
            mmin=q[0][1]
            for i in range(size):
                curr_id=q[0][1]-mmin
                n1=q[0][0]
                q.popleft()
                if(i==0):
                    first=curr_id
                if i== size-1:
                    last=curr_id
                if n1.left:
                    q.append([n1.left,curr_id*2+1])
                if n1.right:
                    q.append([n1.right,curr_id*2+2])
            ans=max(ans,last-first+1)
        
        return ans