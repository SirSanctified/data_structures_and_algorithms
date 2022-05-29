"""
A binary search tree is a special type of binary tree in which every subtree to the left of a given node is smaller than
that node, and every subtree to the right of that node is greater than or equal to that node.

Traversal methods are the same as those of the general binary tree.

searchLargestNode(), searchSmallestNode() and searchBST() are implemented here to search for
the largest, the smallest and the target data item respectively
"""


class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def inorder(self, start):
        if not start:
            return
        self.inorder(start.left)
        print(start.data)
        self.inorder(start.right)

    def postorder(self, start):
        if not start:
            return
        self.postorder(start.left)
        self.postorder(start.right)
        print(start.data)

    def preorder(self, start):
        if not start:
            return
        print(start.data)
        self.preorder(start.left)
        self.preorder(start.right)

    def searchSmallestNode(self, start):
        if not start.left:
            return start.data  # if the tree's left subtree is empty return the current data item
        return self.searchSmallestNode(
            start.left)  # recursively call searchSmallestNode() towards the left until the far left data item

    def searchLargestNode(self, start):
        if not start.right:
            return start.data  # if the tree's right subtree is empty return the current data item
        return self.searchLargestNode(start.right)  # recursively call searchLargestNode() towards the right until
        # the far left data item

    def searchBST(self, _target):
        if _target == self.data:
            return True

        elif _target < self.data:
            if self.left:
                self.left.searchBST(_target)  # recursively search the left subtree
            else:
                return False
        elif _target > self.data:
            if self.right:
                return self.right.searchBST(_target)  # recursively search the right subtree
            else:
                return False

    def addBST(self, data):
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.addBST(data)  # search for a suitable left leaf or leaf-like node to insert
            else:
                self.left = BST(data)
                return self.left
        else:
            if self.right:
                self.right.addBST(data)  # search for a suitable right leaf or leaf-like node to insert
            else:
                self.right = BST(data)
                return self.right


if __name__ == '__main__':

    dt = input("Enter the root data: ")
    root = BST(dt)


    def choice():
        option = int(input('Enter your choice:  '))
        return option


    while True:
        print('0. Exit\n1. Add data\n2. Print tree data using preorder traversal\n3. Print tree data using inorder '
              'traversal\n4. Print tree data using postorder traversal\n5. Search smallest data item\n6. Search '
              'largest data item\n7. Search for a specific data item')
        opt = choice()
        if opt == 0:
            break
        elif opt == 1:
            data = int(input('Enter data to input: '))
            print('Data inserted at ', root.addBST(data))
        elif opt == 2:
            root.preorder(root)
        elif opt == 3:
            root.inorder(root)
        elif opt == 4:
            root.postorder(root)
        elif opt == 5:
            print(root.searchSmallestNode(root))
        elif opt == 6:
            print(root.searchLargestNode(root))
        elif opt == 7:
            target = int(input('Enter data for searching: '))
            print(root.searchBST(target))
