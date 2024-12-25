class CollectionADT:
    """
    An interface for a Collection Abstract Data Type (ADT).
    Provides basic operations that any collection should support.
    """

    def clear(self) -> None:
        """Removes all elements from the collection."""
        raise NotImplementedError

    def contains(self, item) -> bool:
        """Checks if a specific element is in the collection."""
        raise NotImplementedError

    def is_empty(self) -> bool:
        """Checks if the collection has no elements."""
        raise NotImplementedError

    def size(self) -> int:
        """Returns the number of elements in the collection."""
        raise NotImplementedError
