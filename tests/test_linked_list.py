import pytest
from python_linkedlist_lab.linked_list import LinkedList


@pytest.fixture
def linked_list():
    return LinkedList()


def test_new_list_is_empty(linked_list):
    assert linked_list.is_empty()
    assert linked_list.size() == 0


def test_add_first(linked_list):
    linked_list.add_first("A")
    assert linked_list.first() == "A"
    assert linked_list.size() == 1


def test_add_last(linked_list):
    linked_list.add_last("A")
    assert linked_list.last() == "A"
    assert linked_list.size() == 1


def test_add_at_index(linked_list):
    linked_list.add(0, "A")  # [A]
    linked_list.add(1, "B")  # [A, B]
    linked_list.add(1, "C")  # [A, C, B]
    assert linked_list.get(0) == "A"
    assert linked_list.get(1) == "C"
    assert linked_list.get(2) == "B"


def test_add_after(linked_list):
    linked_list.add_last("A")  # [A]
    linked_list.add_last("B")  # [A, B]
    assert linked_list.add_after("A", "C") is True  # [A, C, B]
    assert linked_list.get(1) == "C"


def test_add_after_edge_cases(linked_list):
    # Attempt adding after an item not in the list
    assert linked_list.add_after("nonexistent", "A") is False

    # Now add some items
    linked_list.add_first("A")  # [A]
    assert linked_list.add_after("A", "B") is True  # [A, B]
    assert linked_list.last() == "B"


def test_remove_first(linked_list):
    linked_list.add_last("A")
    linked_list.add_last("B")
    removed = linked_list.remove_first()
    assert removed == "A"
    assert linked_list.first() == "B"


def test_remove_last(linked_list):
    linked_list.add_last("A")
    linked_list.add_last("B")
    removed = linked_list.remove_last()
    assert removed == "B"
    assert linked_list.last() == "A"


def test_remove_by_item(linked_list):
    linked_list.add_last("A")
    linked_list.add_last("B")
    assert linked_list.remove_item("A") is True
    assert linked_list.first() == "B"


def test_remove_edge_cases(linked_list):
    assert linked_list.remove_item("nonexistent") is False
    linked_list.add_last("A")
    assert linked_list.remove_item("A") is True
    assert linked_list.remove_item("A") is False


def test_get(linked_list):
    linked_list.add_last("A")
    linked_list.add_last("B")
    assert linked_list.get(0) == "A"
    assert linked_list.get(1) == "B"


def test_set(linked_list):
    linked_list.add_last("A")
    old_val = linked_list.set(0, "B")
    assert old_val == "A"
    assert linked_list.get(0) == "B"


def test_growth(linked_list):
    # Insert more than typical capacity in array-based approach
    for i in range(15):
        linked_list.add_last(f"Item{i}")
    assert linked_list.size() == 15
    assert linked_list.first() == "Item0"
    assert linked_list.last() == "Item14"


def test_null_item_exception(linked_list):
    with pytest.raises(ValueError):
        linked_list.add_first(None)
    with pytest.raises(ValueError):
        linked_list.add_last(None)
    with pytest.raises(ValueError):
        linked_list.add(0, None)
    # set() as well
    linked_list.add_last("X")
    with pytest.raises(ValueError):
        linked_list.set(0, None)


def test_index_out_of_bounds(linked_list):
    with pytest.raises(IndexError):
        linked_list.get(-1)
    with pytest.raises(IndexError):
        linked_list.get(0)
    with pytest.raises(IndexError):
        linked_list.add(-1, "A")
    with pytest.raises(IndexError):
        linked_list.add(1, "A")


def test_remove_first_on_empty(linked_list):
    with pytest.raises(IndexError):
        linked_list.remove_first()


def test_remove_last_on_empty(linked_list):
    with pytest.raises(IndexError):
        linked_list.remove_last()


def test_first_on_empty(linked_list):
    with pytest.raises(IndexError):
        linked_list.first()


def test_last_on_empty(linked_list):
    with pytest.raises(IndexError):
        linked_list.last()


def test_clear_and_contains(linked_list):
    linked_list.add_last("A")
    linked_list.add_last("B")
    assert linked_list.contains("A")
    linked_list.clear()
    assert linked_list.is_empty()
    assert not linked_list.contains("A")


def test_index_of(linked_list):
    linked_list.add_last("A")
    linked_list.add_last("B")
    linked_list.add_last("A")
    assert linked_list.index_of("A") == 0
    assert linked_list.index_of("B") == 1
    assert linked_list.index_of("C") == -1


def test_add_boundary_conditions(linked_list):
    linked_list.add(0, "A")
    linked_list.add(1, "B")
    assert linked_list.size() == 2
    with pytest.raises(IndexError):
        linked_list.add(-1, "C")
    with pytest.raises(IndexError):
        linked_list.add(3, "C")


def test_add_after_null(linked_list):
    with pytest.raises(ValueError):
        linked_list.add_after(None, "A")
    linked_list.add_first("A")
    with pytest.raises(ValueError):
        linked_list.add_after("A", None)
    with pytest.raises(ValueError):
        linked_list.add_after(None, None)


def test_remove_index(linked_list):
    linked_list.add_last("A")
    linked_list.add_last("B")
    linked_list.add_last("C")
    removed = linked_list.remove(1)  # remove "B"
    assert removed == "B"
    assert linked_list.get(1) == "C"
    removed = linked_list.remove(0)  # remove "A"
    assert removed == "A"
    removed = linked_list.remove(0)  # remove "C"
    assert removed == "C"
    assert linked_list.size() == 0
