# 代码好像就是这么丑，但是事实就是这样
def is_same_tree(root1, root2):
    if (root1 is None) or (root2 is None):
        if (root1 is None) and (root2 is None):
            return True
        else:
            return False

    if root1.val == root2.val:
        if is_same_tree(root1.left, root2.left) and is_same_tree(root1.right, root2.right):
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    root1 = TreeNode(1)
    root1.left = TreeNode(3)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(5)
    root1.right.right = TreeNode(7)

    root2 = TreeNode(1)
    root2.left = TreeNode(3)
    root2.right = TreeNode(2)
    root2.left.left = TreeNode(5)
    root2.right.right = TreeNode(78)

    res = is_same_tree(root1, root2)
    print(res)
