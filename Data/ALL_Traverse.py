class TreeNode:
    def __init__(self, val):
        self.root = val
        self.left = None
        self.right = None

# 前序循环法一
def pre_order_iter1(root):
    stack = []
    stack.append(root)
    while stack:
        # 找出最左边的
        node = stack.pop(0)
        if node.right:
            stack.insert(0, node.right)
        if node.left:
            stack.insert(0, node.left)
        print(node.val, end=" ")

# 前序循环法二
def pre_order_iter2(root):
    node = root
    stack = []
    while stack or node:
        while node:
            print(node.val, end=" ")
            stack.append(node)
            node = node.left
        if stack:
            node = stack.pop()
            node = node.right

# 前序递归
def pre_order_recu(root):
    if root is None:
        return
    print(root.val, end= " ")
    pre_order_iter1(root.left)
    pre_order_iter1(root.right)
    
# 中序循环    
def in_order_iter(root):
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        if stack:
            node = stack.pop()
            print(node.val, end=" ")
            node = node.right
            
            
# 中序递归
def pre_order_recu(root):
    if root is None:
        return
    pre_order_iter1(root.left)
    print(root.val, end= " ")
    pre_order_iter1(root.right)

# 后序循环
def post_iter_rlc(root):
    if root is None:
        return

    stack1 = []
    stack2 = []
    node = root
    stack1.append(node)
    while stack1:
        node = stack1.pop()

        # TODO：是这里先加入的左右节点，造成了是左右中，还是右左中。
        if node.right:
            stack1.append(node.right)

        if node.left:
            stack1.append(node.left)

        # 获得后序遍历反向
        stack2.append(node)

    while stack2:
        print(stack2.pop().val, end=" ")



    
    
 # 后序递归
def post_order_rec(root):
    node = root
    if node:
        return
    self.post_order_rec(node.lchild)
    self.post_order_rec(node.rchild)
    print(node.val, end=" ")
