class Solution:
    def sumNumbers(self, root: TreeNode):
        def dfs(node, bits, res):
            if node.left == None and node.right == None:
                res[0] += int(bits + str(node.val), 10)
            if node.left:
                dfs(node.left, bits + str(node.val), res)
            if node.right:
                dfs(node.right, bits + str(node.val), res)
        if root == None:
            return 0
        bits, res = '', [0]
        dfs(root, bits, res)
        return res[0]



