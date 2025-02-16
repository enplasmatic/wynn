import heapq
import bisect
import random
from collections import Counter
from collections import deque

class vector:
    def __init__(self, values=None):
        """
        Initialize the Vector. If values are provided, initialize with them.
        """
        if values is None:
            self._capacity = 1
            self._size = 0
            self._data = [None] * self._capacity
        else:
            self._capacity = max(1, len(values))
            self._size = len(values)
            self._data = list(values) + [None] * (self._capacity - self._size)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if 0 <= index < self._size:
            return self._data[index]
        raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if 0 <= index < self._size:
            self._data[index] = value
        else:
            raise IndexError("Index out of range")

    def _resize(self, new_capacity):
        """Resizes the internal array to at least new_capacity."""
        new_data = [None] * new_capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data
        self._capacity = new_capacity

    def push_back(self, value):
        """Adds an element to the end of the vector."""
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._data[self._size] = value
        self._size += 1

    def pb(self, value):
        self.push_back(value)

    def minarg(self):
        return self._data.index(min(self._data))

    def maxarg(self):
        return self._data.index(max(self._data))

    def pop_back(self):
        """Removes the last element from the vector."""
        if self._size == 0:
            raise IndexError("Pop from empty vector")
        self._size -= 1
        value = self._data[self._size]
        self._data[self._size] = None  # Optional: clear reference
        return value

    def clear(self):
        """Clears the vector, removing all elements."""
        self._size = 0
        self._data = []

    def __repr__(self):
        return f"vec<{self._data[:self._size]}>"

class array:
    def __init__(self, values=None):
        """
        Initialize the Vector. If values are provided, initialize with them.
        """
        if values is None:
            self._capacity = 1
            self._size = 0
            self._data = [None] * self._capacity
        else:
            self._capacity = max(1, len(values))
            self._size = len(values)
            self._data = list(values) + [None] * (self._capacity - self._size)

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if 0 <= index < self._size:
            return self._data[index]
        raise IndexError("Index out of range")

    def __setitem__(self, index, value):
        if 0 <= index < self._size:
            self._data[index] = value
        else:
            raise IndexError("Index out of range")
        
    def __repr__(self):
        return str(self._data)
    
    def minarg(self):
        return self._data.index(min(self._data))

    def maxarg(self):
        return self._data.index(max(self._data))

class queue:
    def __init__(self, iterable=None):
        """Initialize the queue, optionally with an iterable."""
        self._queue = deque(iterable) if iterable else deque()

    def push(self, value):
        """Push an element to the back of the queue (enqueue)."""
        self._queue.append(value)

    def pop(self):
        """Remove and return the front element (dequeue)."""
        if self._queue:
            return self._queue.popleft()
        raise IndexError("pop from an empty queue")

    def front(self):
        """Return the front element without removing it."""
        if self._queue:
            return self._queue[0]
        raise IndexError("front from an empty queue")

    def empty(self):
        """Check if the queue is empty."""
        return not bool(self._queue)

    def size(self):
        """Return the number of elements in the queue."""
        return len(self._queue)

    def clear(self):
        """Remove all elements from the queue."""
        self._queue.clear()

    def __repr__(self):
        return f"queue<{self._queue}>"


class heap:
    def __init__(self, iterable=None, min_heap=True):
        """Initialize a heap. Defaults to a min-heap. Use min_heap=False for max-heap."""
        self._min_heap = min_heap
        self._heap = []
        if iterable:
            self._heap = list(iterable)
            if not min_heap:
                self._heap = [-x for x in self._heap]  # Invert values for max-heap
            heapq.heapify(self._heap)

    def push(self, value):
        """Push an element into the heap."""
        heapq.heappush(self._heap, value if self._min_heap else -value)

    def pop(self):
        """Remove and return the smallest (min-heap) or largest (max-heap) element."""
        if not self._heap:
            raise IndexError("pop from an empty heap")
        return heapq.heappop(self._heap) if self._min_heap else -heapq.heappop(self._heap)

    def top(self):
        """Return the smallest (min-heap) or largest (max-heap) element without removing it."""
        if not self._heap:
            raise IndexError("top from an empty heap")
        return self._heap[0] if self._min_heap else -self._heap[0]

    def empty(self):
        """Check if the heap is empty."""
        return not bool(self._heap)

    def size(self):
        """Return the number of elements in the heap."""
        return len(self._heap)

    def clear(self):
        """Remove all elements from the heap."""
        self._heap.clear()

    def __repr__(self):
        return f"heap<{[x if self._min_heap else -x for x in self._heap]}>"
    

class sset:
    def __init__(self, iterable=None):
        """Initialize a sorted set. Elements are kept in sorted order."""
        self._data = sorted(set(iterable)) if iterable else []

    def add(self, value):
        """Add an element to the set, maintaining sorted order."""
        if value not in self:
            bisect.insort(self._data, value)

    def remove(self, value):
        """Remove an element from the set. Raises KeyError if not found."""
        index = bisect.bisect_left(self._data, value)
        if index != len(self._data) and self._data[index] == value:
            self._data.pop(index)
        else:
            raise KeyError(f"{value} not found in set")

    def contains(self, value):
        """Check if the set contains a value."""
        index = bisect.bisect_left(self._data, value)
        return index != len(self._data) and self._data[index] == value

    def __contains__(self, value):
        return self.contains(value)

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"sset<{self._data}>"

    def clear(self):
        """Remove all elements from the set."""
        self._data.clear()

    def first(self):
        """Return the smallest element. Raises IndexError if empty."""
        if not self._data:
            raise IndexError("Set is empty")
        return self._data[0]

    def last(self):
        """Return the largest element. Raises IndexError if empty."""
        if not self._data:
            raise IndexError("Set is empty")
        return self._data[-1]


class multiset:
    def __init__(self, iterable=None):
        """Initialize a multiset, allowing duplicate elements."""
        self._data = Counter(iterable) if iterable else Counter()

    def add(self, value):
        """Add an element to the multiset."""
        self._data[value] += 1

    def remove(self, value):
        """Remove one occurrence of an element from the multiset. Raises KeyError if not found."""
        if self._data[value] > 0:
            self._data[value] -= 1
            if self._data[value] == 0:
                del self._data[value]
        else:
            raise KeyError(f"{value} not found in multiset")

    def count(self, value):
        """Return the count of an element in the multiset."""
        return self._data[value]

    def __contains__(self, value):
        return self._data[value] > 0

    def __iter__(self):
        """Iterate over elements, repeating based on their count."""
        for value, count in self._data.items():
            for _ in range(count):
                yield value

    def __len__(self):
        """Return the total number of elements in the multiset (including duplicates)."""
        return sum(self._data.values())

    def __repr__(self):
        return f"multiset<{list(self._data.elements())}>"

    def clear(self):
        """Remove all elements from the multiset."""
        self._data.clear()

class hashmap:
    def __init__(self, iterable=None):
        """Initialize a key-value map."""
        self._data = dict(iterable) if iterable else {}

    def set(self, key, value):
        """Set a key-value pair in the map."""
        self._data[key] = value

    def get(self, key, default=None):
        """Retrieve a value by key, returning default if not found."""
        return self._data.get(key, default)

    def remove(self, key):
        """Remove a key from the map. Raises KeyError if not found."""
        if key in self._data:
            del self._data[key]
        else:
            raise KeyError(f"{key} not found in map {self._data}")
        
    def increment(self, value):
        if value in self._data:
            self._data[value] += 1
        else:
            self._data[value] = 1

    def contains(self, key):
        """Check if the map contains a key."""
        return key in self._data

    def __contains__(self, key):
        return self.contains(key)
    
    def __setitem__(self, key, value):
        """Set an item using bracket notation."""
        self._data[key] = value
    
    def __getitem__(self, key):
        """Retrieve an item using bracket notation."""
        if key in self._data:
            return self._data[key]
        raise KeyError(f"{key} not found in map {self._data}")

    def __iter__(self):
        """Iterate over keys in the map."""
        return iter(self._data)

    def keys(self):
        """Return a view of keys in the map."""
        return self._data.keys()

    def values(self):
        """Return a view of values in the map."""
        return self._data.values()

    def items(self):
        """Return a view of key-value pairs in the map."""
        return self._data.items()

    def __len__(self):
        """Return the number of key-value pairs in the map."""
        return len(self._data)

    def __repr__(self):
        return f"map<{self._data}>"

    def clear(self):
        """Remove all key-value pairs from the map."""
        self._data.clear()


class _Node:
    __slots__ = 'key', 'value', 'priority', 'left', 'right'
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        # A random priority gives us the heap property.
        self.priority = random.random()
        self.left = None
        self.right = None

class multimap:
    def __init__(self):
        self._root = None

    # --- Treap helper routines ---
    def _split(self, root, key):
        """
        Splits the treap rooted at 'root' into two treaps:
         - left: nodes with keys < key,
         - right: nodes with keys >= key.
        Returns (left, right).
        """
        if root is None:
            return (None, None)
        if root.key < key:
            # Current node belongs to left part.
            left_subtree, right_subtree = self._split(root.right, key)
            root.right = left_subtree
            return (root, right_subtree)
        else:
            # root.key >= key: current node goes to right part.
            left_subtree, right_subtree = self._split(root.left, key)
            root.left = right_subtree
            return (left_subtree, root)

    def _merge(self, left, right):
        """
        Merges two treaps 'left' and 'right' (all keys in left are <= all keys in right)
        and returns the new root.
        """
        if left is None:
            return right
        if right is None:
            return left

        if left.priority < right.priority:
            # Left becomes parent.
            left.right = self._merge(left.right, right)
            return left
        else:
            right.left = self._merge(left, right.left)
            return right

    def insert(self, key, value):
        """Insert the pair (key, value) into the multimap."""
        new_node = _Node(key, value)
        # We want duplicates to be stored in order; choose to send equal keys
        # to the right subtree so that lower_bound finds the first occurrence.
        left, right = self._split(self._root, key)
        # Merge left with new node, then merge with right.
        self._root = self._merge(self._merge(left, new_node), right)

    def _erase(self, root, key, value):
        """
        Erase one occurrence of (key, value) from the treap rooted at 'root'.
        Returns the new root and a boolean indicating if an element was removed.
        (If multiple nodes have the same key, value, only one is removed.)
        """
        if root is None:
            return (None, False)
        removed = False
        if key == root.key and value == root.value:
            # Remove this node by merging its children.
            new_root = self._merge(root.left, root.right)
            return (new_root, True)
        elif key < root.key:
            new_left, removed = self._erase(root.left, key, value)
            root.left = new_left
        else:
            # For equal keys, note that our insertion rule sends duplicates to the right.
            new_right, removed = self._erase(root.right, key, value)
            root.right = new_right
        return (root, removed)

    def erase(self, key, value):
        """
        Erase one occurrence of the pair (key, value).
        Returns True if a node was removed, False otherwise.
        """
        self._root, removed = self._erase(self._root, key, value)
        return removed

    # --- Lookup routines ---
    def find_all(self, key):
        """
        Returns a list of all values associated with the given key.
        (The order is the sorted order of insertion in the tree.)
        """
        result = []
        # We can use the lower_bound routine to start.
        node = self.lower_bound(key)
        # Walk the in-order chain while keys are equal.
        while node is not None and node.key == key:
            result.append(node.value)
            node = self._successor(node.key, node.value)
        return result

    def lower_bound(self, key):
        """
        Returns the first node (as an _Node object) whose key is >= the given key.
        If no such node exists, returns None.
        """
        result = None
        cur = self._root
        while cur is not None:
            if cur.key < key:
                cur = cur.right
            else:
                result = cur
                cur = cur.left
        return result

    def upper_bound(self, key):
        """
        Returns the first node (as an _Node object) whose key is > the given key.
        If no such node exists, returns None.
        """
        result = None
        cur = self._root
        while cur is not None:
            if cur.key <= key:
                cur = cur.right
            else:
                result = cur
                cur = cur.left
        return result

    def equal_range(self, key):
        """
        Returns a list of all (key, value) pairs matching the given key.
        """
        node = self.lower_bound(key)
        result = []
        while node is not None and node.key == key:
            result.append((node.key, node.value))
            node = self._successor(node.key, node.value)
        return result

    # --- In-order traversal routines ---
    def _inorder(self, root):
        """Generator to in-order traverse the treap."""
        if root is not None:
            yield from self._inorder(root.left)
            yield root
            yield from self._inorder(root.right)

    def __iter__(self):
        """Iterate over (key, value) pairs in sorted order by key."""
        for node in self._inorder(self._root):
            yield (node.key, node.value)

    def items(self):
        """Return a list of (key, value) pairs in order."""
        return list(iter(self))

    # --- Helper: find the successor of a given node ---
    def _successor(self, key, value):
        """
        Returns the next node in the sorted order after the given (key, value) pair,
        or None if there is no successor.
        Since our treap does not have parent pointers, we do an in-order traversal.
        (For efficiency in real applications, you might want to maintain parent
         pointers or an explicit iterator.)
        """
        # One way is to do an in-order traversal and stop when we pass (key, value).
        # Here we use the treap’s in-order iterator.
        found = False
        for node in self._inorder(self._root):
            if found:
                return node
            if node.key == key and node.value == value:
                found = True
        return None
    
class pair:
    def __init__(self, values):
        """Initialize the Pair with two values."""
        assert (len(values) == 2)
        first, second = values[0], values[1]
        self.first = first
        self.second = second

    def __repr__(self):
        """Return the string representation of the Pair."""
        return f"Pair({self.first}, {self.second})"

    def __eq__(self, other):
        """Check if two Pairs are equal based on their elements."""
        if isinstance(other, pair):
            return self.first == other.first and self.second == other.second
        return NotImplemented

    def __lt__(self, other):
        """
        Define a lexicographical ordering for Pair.
        This allows Pairs to be compared and sorted if their elements are comparable.
        """
        if isinstance(other, pair):
            return (self.first, self.second) < (other.first, other.second)
        return NotImplemented

    def __iter__(self):
        """Allow unpacking the pair, e.g., a, b = pair."""
        yield self.first
        yield self.second

    def __getitem__(self, index):
        """Allow indexing: pair[0] returns first, pair[1] returns second."""
        if index == 0:
            return self.first
        elif index == 1:
            return self.second
        else:
            raise IndexError("Index out of range for Pair. Valid indices are 0 and 1.")

class couple(tuple):
    def empty(self):
        return tuple()
    

