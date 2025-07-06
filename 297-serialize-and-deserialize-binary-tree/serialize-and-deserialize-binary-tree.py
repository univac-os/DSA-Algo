# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    we want convert tree to str so store it using preOrder
    """
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res=[]
        def dfs(root):
            if root==None:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
            
        dfs(root)

        return ",".join(res)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        we have null to know its children
        """
        val=data.split(',')
        self.idx=0

        def preOrd():
            if val[self.idx]=="N":
                self.idx+=1 #ignore the N from serialize
                return None
            node=TreeNode(int(val[self.idx]))
            self.idx+=1
            node.left=preOrd()
            node.right=preOrd()
            return node

        return preOrd()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))