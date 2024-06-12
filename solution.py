from typing import TypeVar, List

# for more information on type hinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
Node = TypeVar("Node")  # represents a Node object (forward-declare to use in Node __init__)
DLL = TypeVar("DLL")


class Node:
    """
    Implementation of a doubly linked list node.
    DO NOT MODIFY
    """
    __slots__ = ["value", "next", "prev", "child"]

    def __init__(self, value: T, next: Node = None, prev: Node = None, child: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :return: None.
        DO NOT MODIFY
        """
        self.next = next
        self.prev = prev
        self.value = value

        # The child attribute is only used for the application problem
        self.child = child

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.
        DO NOT MODIFY
        """
        return f"Node({str(self.value)})"

    __str__ = __repr__


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.
    Modify only below indicated line.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.

        :return: None.
        DO NOT MODIFY
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        DO NOT MODIFY
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
            if node is self.head:
                break
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        return repr(self)

    def __eq__(self, other: DLL) -> bool:
        """
        :param other: compares equality with this List
        :return: True if equal otherwise False
        DO NOT MODIFY
        """
        cur_node = self.head
        other_node = other.head
        while True:
            if cur_node != other_node:
                return False
            if cur_node is None and other_node is None:
                return True
            if cur_node is None or other_node is None:
                return False
            cur_node = cur_node.next
            other_node = other_node.next
            if cur_node is self.head and other_node is other.head:
                return True
            if cur_node is self.head or other_node is other.head:
                return False

    # MODIFY BELOW #
    # Refer to the classes provided to understand the problems better#

    def empty(self) -> bool:
        """
        Checks whether the linked list is empty.

        Returns:
        bool: True if the linked list is empty (head is None), False otherwise.
        """
        return self.head is None

    def push(self, val: T, back: bool = True) -> None:
        """
        Adds a new node with the given value to the linked list.

        Args:
        val (T): The value to be stored in the new node.
        back (bool, optional): If True (default), the new node is added to the back of the list.
                              If False, the new node is added to the front of the list.

        Returns:
        None
        """
        new_node = Node(val)
        if back:
            if not self.head:
                # If the list is empty, set new_node as both head and tail
                self.head = new_node
                self.tail = new_node
                self.tail.next = None
                self.head.prev = None
            else:
                # Add new_node to the back of the list
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
                self.tail.next = None
                self.head.prev = None
        else:
            if not self.head:
                # If the list is empty, set new_node as both head and tail
                self.head = new_node
                self.tail = new_node
            else:
                # Add new_node to the front of the list
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node

        # Update the size of the list
        self.size += 1

    def pop(self, back: bool = True) -> None:
        """
        Removes and returns the node from the linked list.

        Args:
        back (bool, optional): If True (default), removes the node from the back of the list.
                              If False, removes the node from the front of the list.

        Returns:
        None
        """
        # If DLL is empty, do nothing
        if not self.head:
            return

        if back:
            # Remove from the back of the list
            popped_node = self.tail
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                # If the last node is removed, update head to None
                self.head = None
        else:
            # Remove from the front of the list
            popped_node = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                # If the last node is removed, update tail to None
                self.tail = None

        self.size -= 1

    def list_to_dll(self, source: List[T]) -> None:
        """
        Converts a list of values into a doubly linked list.

        Args:
        source (List[T]): The list of values to be converted into a doubly linked list.

        Returns:
        None
        """
        # Clear the existing DLL
        self.head = None
        self.tail = None
        self.size = 0

        # Push each value from the list onto the doubly linked list
        for val in source:
            self.push(val)

    def dll_to_list(self) -> List[T]:
        """
        Converts the doubly linked list to a list of values.

        Returns:
        List[T]: A list containing the values stored in the doubly linked list.
        """
        # Initialize an empty list to store DLL values
        result_list = []

        # Traverse the DLL and append each node's data to the list
        current_node = self.head
        while current_node:
            result_list.append(current_node.value)
            current_node = current_node.next

        return result_list

    def _find_nodes(self, val: T, find_first: bool = False) -> List[Node]:
        """
        Finds nodes with a specific value in the doubly linked list.

        Args:
        val (T): The value to search for in the nodes.
        find_first (bool, optional): If True, returns a list containing the first node with the specified value.
                                     If False (default), returns a list containing all nodes with the specified value.

        Returns:
        List[Node]: A list containing nodes with the specified value.
        """
        node_list = []
        current = self.head
        while current:
            if current.value == val and find_first:
                node_list.append(current)
                return node_list
            elif current.value == val and not find_first:
                node_list.append(current)
            current = current.next
        return node_list

    def find(self, val: T) -> Node:
        """
        Finds the first occurrence of a node with a specific value in the doubly linked list.

        Args:
        val (T): The value to search for in the nodes.

        Returns:
        Node: The first node with the specified value, or None if not found.
        """
        node_list = self._find_nodes(val, find_first=True)
        return node_list[0] if len(node_list) > 0 else None

    def find_all(self, val: T) -> List[Node]:
        """
        Finds all nodes with a specific value in the doubly linked list.

        Args:
        val (T): The value to search for in the nodes.

        Returns:
        List[Node]: A list containing all nodes with the specified value, or an empty list if none are found.
        """
        node_list = self._find_nodes(val, find_first=False)
        return node_list if len(node_list) > 0 else []

    def _remove_node(self, to_remove: Node) -> None:
        """
        Removes a given node from the doubly linked list.

        Parameters:
        - to_remove (Node): Node to be removed from the DLL.

        Returns:
        None
        """
        # Check if the node to remove is the head
        if to_remove.prev is None:
            self.head = to_remove.next
        else:
            to_remove.prev.next = to_remove.next

        # Check if the node to remove is the tail
        if to_remove.next is None:
            self.tail = to_remove.prev
        else:
            to_remove.next.prev = to_remove.prev

    def remove(self, val) -> bool:
        """
        Removes the first node with the specified value from the DLL.

        Parameters:
        - val (T): Value to be removed from the DLL.

        Returns:
        True if a Node with the specified value was found and removed, else False.
        """
        found_node = self.find(val)
        if found_node:
            self._remove_node(found_node)
            self.size -= 1
            return True
        return False

    def remove_all(self, val) -> int:
        """
        Removes all nodes with the specified value from the DLL.

        Parameters:
        - val (T): Value to be removed from the DLL.

        Returns:
        Number of Node objects with the specified value removed from the DLL.
        If no node containing val exists in the DLL, returns 0.
        """
        found_nodes = self.find_all(val)
        for node in found_nodes:
            self._remove_node(node)
            self.size -= 1
        return len(found_nodes)

    def reverse(self) -> None:
        """
        Reverses the order of nodes in the doubly linked list.

        Returns:
        None
        """
        current = self.head

        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev

        self.head, self.tail = self.tail, self.head


def dream_escaper(dll: DLL) -> DLL:
    """
    Creates a new doubly linked list by escaping dream sequences in the input doubly linked list.

    Args:
    dll (DLL): The input doubly linked list representing dream sequences.

    Returns:
    DLL: A new doubly linked list with dream sequences escaped.
    """
    result_dll = DLL()
    current = dll.head
    stack = []

    while current or stack:
        if current:
            result_dll.push(current.value)
            if current.child:
                if current.next:
                    stack.append(current.next)
                current = current.child
            elif current.next:
                current = current.next
            else:
                if stack:
                    current = stack.pop()
                else:
                    break
        else:
            current = stack.pop()

    return result_dll
