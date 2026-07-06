class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nextn = None
        self.prevn = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cmap = {}
        
        # Dummy boundaries to handle edge cases cleanly
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.nextn = self.tail
        self.tail.prevn = self.head

    def _remove(self, node: Node):
        """Helper to splice a node out of its current position."""
        prev_node = node.prevn
        next_node = node.nextn
        prev_node.nextn = next_node
        next_node.prevn = prev_node

    def _add_to_head(self, node: Node):
        """Helper to insert a node right after the dummy head (MRU)."""
        node.nextn = self.head.nextn
        node.prevn = self.head
        self.head.nextn.prevn = node
        self.head.nextn = node

    def get(self, key: int) -> int:
        if key not in self.cmap:
            return -1
        
        # Move accessed node to head (MRU)
        node = self.cmap[key]
        self._remove(node)
        self._add_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cmap:
            # Key exists: update val and refresh positioning
            node = self.cmap[key]
            node.val = value
            self._remove(node)
            self._add_to_head(node)
        else:
            # Cache is full: evict the tail node (LRU)
            if len(self.cmap) == self.capacity:
                lru_node = self.tail.prevn
                self._remove(lru_node)
                del self.cmap[lru_node.key]
            
            # Insert new element
            new_node = Node(key, value)
            self.cmap[key] = new_node
            self._add_to_head(new_node)
