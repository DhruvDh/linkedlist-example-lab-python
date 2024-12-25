from .list_adt import ListADT
from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None


class LinkedList(ListADT):
    def __init__(self):
        self.head = None
        self._size = 0

    def clear(self) -> None:
        self.head = None
        self._size = 0

    def contains(self, item) -> bool:
        return self.index_of(item) != -1

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size

    def add(self, index: int, item) -> None:
        if item is None:
            raise ValueError("Item cannot be None")
        if index < 0 or index > self._size:
            raise IndexError(f"Index out of bounds: {index}")

        new_node = Node(item)
        if index == 0:
            # Insert at head
            new_node.next = self.head
            self.head = new_node
        else:
            # Traverse to (index-1)th node
            prev = self._get_node(index - 1)
            new_node.next = prev.next
            prev.next = new_node

        self._size += 1

    def add_first(self, item) -> None:
        self.add(0, item)

    def add_last(self, item) -> None:
        self.add(self._size, item)

    def add_after(self, existing, item) -> bool:
        if existing is None or item is None:
            raise ValueError("Existing or item cannot be None")
        index = self.index_of(existing)
        if index == -1:
            return False
        self.add(index + 1, item)
        return True

    def remove_first(self):
        if self.is_empty():
            raise IndexError("List is empty")
        return self.remove(0)

    def remove_last(self):
        if self.is_empty():
            raise IndexError("List is empty")
        return self.remove(self._size - 1)

    def remove(self, index: int):
        if index < 0 or index >= self._size:
            raise IndexError(f"Index out of bounds: {index}")

        if index == 0:
            removed_data = self.head.data
            self.head = self.head.next
        else:
            prev = self._get_node(index - 1)
            removed_data = prev.next.data
            prev.next = prev.next.next

        self._size -= 1
        return removed_data

    def remove_item(self, item) -> bool:
        pos = self.index_of(item)
        if pos == -1:
            return False
        self.remove(pos)
        return True

    def first(self):
        if self.is_empty():
            raise IndexError("List is empty")
        return self.head.data

    def last(self):
        if self.is_empty():
            raise IndexError("List is empty")
        return self._get_node(self._size - 1).data

    def get(self, index: int):
        if index < 0 or index >= self._size:
            raise IndexError(f"Index out of bounds: {index}")
        return self._get_node(index).data

    def set(self, index: int, item):
        if item is None:
            raise ValueError("Item cannot be None")
        if index < 0 or index >= self._size:
            raise IndexError(f"Index out of bounds: {index}")

        node = self._get_node(index)
        old_data = node.data
        node.data = item
        return old_data

    def index_of(self, item) -> int:
        current = self.head
        idx = 0
        while current:
            # Check equality
            if current.data == item:
                return idx
            current = current.next
            idx += 1
        return -1

    def _get_node(self, index: int) -> Node:
        """Traverse and return the Node at position `index`."""
        current = self.head
        for _ in range(index):
            current = current.next
        return current
