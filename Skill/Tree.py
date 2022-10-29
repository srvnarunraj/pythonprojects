class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert_by_condition(self, data):
        if data < self.data:
            # add to the left Node
            if self.left is None:
                # Recursively call the node
                self.left = Node(data)
            else:
                # Recursively calls the insert_by_condition function
                self.left.insert_by_condition(data)

        else:
            # add to right Node
            if self.right is None:
                # No data , then add
                self.right = Node(data)
            else:
                # if there is data then recursively call the insert_by_condition function
                self.right.insert_by_condition(data)

    def inordertraversal(self):
        elements = []
        if self.left:
            elements += self.left.inordertraversal()

        elements.append(self.data)

        if self.right:

            elements += self.right.inordertraversal()
        return elements


rootNode=Node(6)
rootNode.insert_by_condition(4)
rootNode.insert_by_condition(7)
rootNode.insert_by_condition(8)
rootNode.insert_by_condition(5)
print(rootNode.inordertraversal())
