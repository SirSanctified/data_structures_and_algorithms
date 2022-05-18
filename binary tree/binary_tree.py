"""Binary tree is a none linear data structure in which each node contains at most two children. this implementation
uses recursion. You must understand recursion first before looking at this code. All traversal methods are implemented
"""


class DataItem:
    def __int__(self):
        self.data = None
        self.left = None
        self.right = None


class BinaryTree:
    def __int__(self):
        self.root = None

    def create(self) -> DataItem:
        data_item = DataItem()
        data = input('Enter node data (q when done) ')
        if data == 'q':
            return
        data_item.data = data
        print(f'Left node of {data}')
        data_item.left = self.create()
        print(f'Right node of {data}')
        data_item.right = self.create()
        return data_item

    def preorder(self, root):
        if not root:
            return
        print(root.data)
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.data)
        self.inorder(root.right)

    def postorder(self, root):
        if not root:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data)


bt = BinaryTree()
bt.root = bt.create()
print('============================================================================\n')
print('How do you want your data to be printed?\n1.Preorder\n2.Inorder\n3.Postorder')
ch = int(input())
print('____________________________________________________________')
if ch == 1:
    bt.preorder(bt.root)
elif ch == 2:
    bt.inorder(bt.root)
elif ch == 3:
    bt.postorder(bt.root)
else:
    print('Invalid option')
