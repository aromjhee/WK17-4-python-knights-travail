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

    def depth_search(self, value):
        if self.value == value:
            return self
        if self.children:
            next = self.children[0]
            self.remove_child(next)
            return next.depth_search(value)
        
        return None
    
    # def breadth_search(self, value):
    #     if self.value == value:
    #         return self
    #     if self.children:



# node1 = Node("root1")
# node2 = Node("root2")
# node3 = Node("root3")

# node2.parent = node1
# node3.parent = node2

# print(node1.depth_search('asdf'))
