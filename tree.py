class Node:
    __slots__ = ['_value', '_parent', '_children']

    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    def __repr__(self):
        return f'<Node value: {self._value}, parent: {self._parent}, children: {list(map(lambda x: x.value, self._children))}>'

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
        if self.parent:
            self.parent.remove_child(self)
        self._parent = node
        if node != None:
            node.add_child(self)
    
    def add_child(self, node):
        if node not in self.children:
            self._children.append(node)
            node._parent = self
    
    def remove_child(self, node):
        self._children.remove(node)
        node._parent = None


# testNode = Node('some value')
# childNode = Node('im a child')
# print(childNode)
# childNode.parent = testNode
# print(childNode)
# print(testNode)
# testNode.remove_child(childNode)
# print(childNode)
# print(testNode)

node1 = Node("root1")
node2 = Node("root2")
node3 = Node("root3")

node3.parent = node1
node3.parent = node2


print(node1.children)
print(node2.children)
# print(node1)
# print(node2)
# print(node3)

