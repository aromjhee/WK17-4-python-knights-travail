class Node:
    # __slots__ = ['_value', '_parent', '_children']

    def __init__(self, value):
        self._value = value
        self._parent = None
        self._children = []

    def __repr__(self):
        return f'<Node value: {self._value}, parent: {self._parent}, children: {list(map(lambda x: x.value, self._children))}s>'

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
        if self.parent == node:
            return
        if self.parent:
            self.parent.remove_child(self)
        self._parent = node
        if node != None:
            node.add_child(self)
    
    def add_child(self, node):
        if node not in self.children:
            self._children.append(node)
            node.parent = self
    
    def remove_child(self, node):
        if node in self.children:
            self._children.remove(node)
            node.parent = None

    def depth_search(self, value):
        if self.value == value:
            return self
        
        for child in self.children:
            print(child.value)
            res = child.depth_search(value)
            if res != None:
                return res
        
        return None
    
    def breadth_search(self, value):
        child = []
        queue = [self]

        while queue:
            node = queue.pop(0)
            # print(node.value)
            if node.value == value:
                return node
            else:
                child = node.children
                for n in child:
                    queue.append(n)

        return None


# node1 = Node("root1")
# node2 = Node("root2")
# node3 = Node("root3")
# node4 = Node("root4")
# node5 = Node("root5")
# node6 = Node("root6")

# node2.parent = node1
# node3.parent = node1
# node4.parent = node2
# node5.parent = node2
# node6.parent = node3

# print(node1.breadth_search('root6'))
