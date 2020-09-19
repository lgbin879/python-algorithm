import time

def calc_time(func):  
    def wrapper(*args, **kw):  
        start_time = time.time()  
        func(*args, **kw)
        end_time = time.time()
        print('\n[%s] run time is %.6f s' % (func.__name__, end_time - start_time))
    return wrapper 


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree(object):
    """docstring for Tree"""
    def __init__(self, node=None):
        self.root = node


    def add(self, val):
        node = Node(val)
        if self.root is None:
            self.root = node
            return

        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)

            if cur_node.left is None:
                cur_node.left = node
                return
            else:
                queue.append(cur_node.left)

            if cur_node.right is None:
                cur_node.right = node
                return
            else:
                queue.append(cur_node.right)


    def print_queue(self, queue):
        print("queue: ")
        if queue:
            for node in queue:
                if node is not None:
                    print(node.val, end=" ")
                else:
                    print("_", end=" ")
        print()


    def preorder_travel_recursive(self, root):
        """3行code递归实现前序遍历"""
        if root is None:
            return

        print(root.val, end=" ")
        self.preorder_travel_recursive(root.left)
        self.preorder_travel_recursive(root.right)


    def inorder_travel_recursive(self, root):
        """3行code递归实现中序遍历"""
        if root is None:
            return

        self.inorder_travel_recursive(root.left)
        print(root.val, end=" ")
        self.inorder_travel_recursive(root.right)           


    def postorder_travel_recursive(self, root):
        """3行code递归实现后序遍历"""
        if root is None:
            return

        self.postorder_travel_recursive(root.left)
        self.postorder_travel_recursive(root.right)
        print(root.val, end=" ")
                
    @calc_time
    def preorder_travel_nonrecursive(self, root):
        """非递归前序遍历，利用1个stack"""
        if root is None:
            return

        stack = []
        cur_node = root

        while stack or cur_node:
            if cur_node:
                print(cur_node.val, end=" ")
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop()
                cur_node = cur_node.right

    @calc_time
    def inorder_travel_nonrecursive(self, root):
        """非递归中序遍历，利用1个stack"""
        if root is None:
            return

        stack = []
        cur_node = root

        while stack or cur_node:
            if cur_node:
                stack.append(cur_node)
                cur_node = cur_node.left
            else:
                cur_node = stack.pop()
                print(cur_node.val, end=" ")
                cur_node = cur_node.right

    @calc_time
    def postorder_travel_nonrecursive(self, root):
        """TODO: 非递归后序遍历，利用2个stack"""
        if root is None:
            return

        stack1 = []
        stack2 = []
        stack1.append(root)

        while stack1:
            top = stack1.pop()
            stack2.append(top)

            if top.left:
                stack1.append(top.left)
            if top.right:
                stack1.append(top.right)

        while stack2:
            top = stack2.pop()
            print(top.val, end=" ")
   
    @calc_time
    def broad_travel(self):
        """广度优先遍历，利用1个queue"""
        if self.root is None:
            return
            
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.val, end=' ')

            if cur_node.left is not None:
                queue.append(cur_node.left)
            if cur_node.right is not None:
                queue.append(cur_node.right)
        print()



def main():
    tree = Tree()

    for i in range(0,160):
        tree.add(i)

    print("broad_travel:")
    tree.broad_travel()
    print()

    print("preorder_travel_recursive:")
    start_time = time.time()
    tree.preorder_travel_recursive(tree.root)
    end_time = time.time()
    print('\n[%s] run time is %.6f' % ("preorder_travel_recursive", end_time - start_time))
    print("preorder_travel_nonrecursive:")
    tree.preorder_travel_nonrecursive(tree.root)
    print()

    print("inorder_travel_recursive:")
    start_time = time.time()
    tree.inorder_travel_recursive(tree.root)
    end_time = time.time()
    print('\n[%s] run time is %.6f' % ("inorder_travel_recursive", end_time - start_time))
    print("inorder_travel_nonrecursive:")
    tree.inorder_travel_nonrecursive(tree.root)
    print()

    print("postorder_travel_recursive:")
    start_time = time.time()
    tree.postorder_travel_recursive(tree.root)
    end_time = time.time()
    print('\n[%s] run time is %.6f' % ("postorder_travel_recursive", end_time - start_time))
    print("postorder_travel_nonrecursive:")
    tree.postorder_travel_nonrecursive(tree.root)
    print()


if __name__ == '__main__':
    main()


