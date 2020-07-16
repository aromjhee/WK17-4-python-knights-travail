class Node:
    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value(self):
        return self._value

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if self.parent != None:
            if self.parent.value == node.value:
                return
            else:
                node.parent = None
        self._parent = node
        node.add_child(self)
    
    def add_child(self, node):
        if node not in self.children:
            self._children.append(node)
            self._parent = self
    
    def remove_child(self, node):
        self._children.remove(node)
        node.parent = None
        self.parent = None


# testNode = Node('some value')
# childNode = Node('im a child')
# testNode.parent = childNode
# print(testNode.value)
# print(testNode.children)
# print(childNode.value)
# print(testNode.children)

node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")

node3.parent = node1
print(node3.parent)
node3.parent = node2

print(node1.children)
print(node2.children)

