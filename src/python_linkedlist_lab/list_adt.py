from .collection_adt import CollectionADT


class ListADT(CollectionADT):
    """
    An interface for a List Abstract Data Type (ADT).
    Extends CollectionADT with operations specific to lists.
    """

    def add(self, index: int, item) -> None:
        raise NotImplementedError

    def add_first(self, item) -> None:
        raise NotImplementedError

    def add_last(self, item) -> None:
        raise NotImplementedError

    def add_after(self, existing, item) -> bool:
        raise NotImplementedError

    def remove_first(self):
        raise NotImplementedError

    def remove_last(self):
        raise NotImplementedError

    def remove(self, index: int):
        raise NotImplementedError

    def remove_item(self, item) -> bool:
        """Remove the first occurrence of `item` (if it exists)."""
        raise NotImplementedError

    def first(self):
        raise NotImplementedError

    def last(self):
        raise NotImplementedError

    def get(self, index: int):
        raise NotImplementedError

    def set(self, index: int, item):
        raise NotImplementedError

    def index_of(self, item) -> int:
        raise NotImplementedError
