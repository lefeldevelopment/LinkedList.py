class Node:
    def __init__(self, data) -> None:
        self._data = data
        self._next = None

    def get_next(self):
        return self._next

    def get_data(self):
        return self._data

    def set_next(self, next):
        self._next = next

    def set_data(self, data):
        self._data = data

    def __repr__(self) -> str:
        return str(self.get_data())
    
    def __lt__(self, other):
        return self.get_data() < other.get_data()