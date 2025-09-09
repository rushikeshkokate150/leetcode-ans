def changetree(root):
    if root==None:
        return
    child=0
    if root.left:
        child+=root.left.val
    if root.right:
        child+=root.right.val
    if child>=root.val:
        root.val=child
    else:
        root.left.val=root.val
        root.right.val=root.val
    changetree(root.left)
    changetree(root.right)
    
    total=0
    if root.left:
        total+=root.left.val
    if root.right:
        total+=root.right.val
    if(root.left or root.right):
        root.val=total