from Node import Node

class LinkedList:
    def __init__(self, head=None) -> None:
        if head:
            self._head = Node(head)
        else:
            self._head = None

    def create_from_list(list):
        linked = LinkedList()
        linked._head = LinkedList._list_to_linked(list)
        return linked

    def append(self, data):
        self._add_node_at_end(Node(data))

    def extend(self, list):
        self._add_node_at_end(LinkedList._list_to_linked(list))

    def insert(self, idx: int, data):
        new = Node(data)
        if not idx:
            new.set_next(self._head)
            self._head = new
        else:
            obj = self._idx(idx-1)
            new.set_next(obj.get_next())
            obj.set_next(new)

    def remove(self, idx):
        try:
            if not idx:
                self._head = self._head.get_next()
            else:
                obj = self._idx(idx-1)
                obj.set_next(obj.get_next().get_next())
        except:
            return IndexError

    def pop(self, idx):
        try:
            if not idx:
                out = self._head.get_data()
                self._head = self._head.get_next()
            else:
                obj = self._idx(idx-1)
                out = obj.get_data()
                obj.set_next(obj.get_next().get_next())
            return out
        except:
            return IndexError

    def clear(self):
        self._head = None

    def count(self, value):
        n = 0
        for elem in self:
            if elem.get_data() == value:
                n += 1
        return n

    def find(self, value):
        n = 0
        out = []
        for elem in self:
            if elem.get_data() == value:
                out.append(n)
            n += 1
        return out

    def index(self, idx):
        return self[idx]

    def reverse(self):
        previous = None
        current = self._head
        following = current.get_next()

        while current:
            current.set_next(previous)
            previous = current
            current = following
            if following:
                following = following.get_next()

        self._head = previous

    def sort(self,key=None,reverse:bool=False):
        sorted_list = list(sorted([v.get_data() for v in self],key=key,reverse=reverse))
        self._head = LinkedList._list_to_linked(sorted_list)
    
    def copy(self):
        node_list = [n.get_data() for n in self]
        linked = LinkedList()
        linked._head = LinkedList._list_to_linked(node_list)
        return linked
    
    def __iter__(self):
        node = self._head
        while node:
            yield node
            node = node._next

    def __repr__(self) -> str:
        return " -> ".join([str(node.get_data()) for node in self])

    def __getitem__(self, idx):
        return self._idx(idx)

    def __add__(self, val):
        if isinstance(val, LinkedList):
            self._add_node_at_end(val._head)
        elif isinstance(val, Node):
            self._add_node_at_end(val)
        elif isinstance(val, list):
            self._add_node_at_end(LinkedList._list_to_linked(list))
        else:
            self._add_node_at_end(Node(val))

    def __len__(self):
        n = 0
        for _ in self:
            n += 1
        return n
    
    def display(self):
        print(self)
    
    def __delitem__(self, idx):
        self.remove(idx)

    def _idx(self, idx):
        return list(self)[idx]

    def _add_node_at_end(self, node):
        if self._head:
            *_, obj = self.__iter__()
            obj.set_next(node)
        else:
            self._head = node

    def _list_to_linked(list):
        temporary = current = Node(None)
        for element in list:
            current.set_next(Node(element))
            current = current.get_next()
        return temporary.get_next()

if __name__ == "__main__":
    l = LinkedList.create_from_list([1,2,3,4,5])
    print(l)