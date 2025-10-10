class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        # Dummy head and tail nodes to simplify insert/remove
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        """Remove node from the linked list."""
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def _add_to_front(self, node):
        """Add node right after head (most recently used)."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            # Move the accessed node to the front
            self._remove(node)
            self._add_to_front(node)
            return node.value
        return -1

    def set(self, key, value):
        if key in self.cache:
            # Update value and move to front
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                # Remove least recently used node
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]
            # Add new node
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_front(new_node)


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


head, tail = None, None
N, MAX = 0, 0
mMap = {}


class LRUCache2:

    # @param capacity, an integer
    def __init__(self, capacity):
        global head, tail, MAX, N, mMap
        head = None
        tail = None
        MAX = capacity
        N = 0
        mMap = {}

    def updateAccessList(self, node):
        global head
        temp = node.prev
        temp.next = node.next
        temp = node.next
        if (temp != None):
            temp.prev = node.prev

        node.next = head
        head.prev = node
        node.prev = None
        head = node

    # @return an integer
    def get(self, key):
        global head, tail, MAX, N, mMap
        if (N == 0):
            return -1

        if (key in mMap):
            node = mMap[key]
            if (key == head.key):
                return node.val
            if (tail.key == key):
                tail = tail.prev

            self.updateAccessList(node)
            return node.val

        return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        global head, tail, MAX, N, mMap
        if (key in mMap):
            node = mMap[key]
            if (node.key == head.key):
                node.val = value
                return
            if (tail.key == key):
                tail = tail.prev
            self.updateAccessList(node)
            node.val = value
            return

        if (N == MAX):
            if (tail != None):
                del mMap[tail.key]
                tail = tail.prev
                if (tail != None):
                    tail.next.prev = None
                    tail.next = None
                N -= 1

        node = Node(key, value)
        node.next = head
        if (head != None):
            head.prev = node

        head = node
        N += 1

        if (N == 1):
            tail = head

        mMap[key] = node