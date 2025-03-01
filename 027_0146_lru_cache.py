# watch solution, need revisit
class LRUCache:
    def __init__(self, capacity: int):
        self.hmap = {}
        self.capacity = capacity
        self.left, self.right = ListNode(0, 0), ListNode(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key not in self.hmap:
            return -1
        self.remove(self.hmap[key])
        self.ins_right(self.hmap[key])
        return self.hmap[key].val


    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            self.remove(self.hmap[key])
        self.hmap[key] = ListNode(value, key)
        self.ins_right(self.hmap[key])
        if len(self.hmap) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.hmap[lru.key]

    def remove(self, node: ListNode) -> None:
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    def ins_right(self, node: ListNode) -> None:
        prev, next = self.right.prev, self.right
        prev.next = node
        next.prev = node
        node.next, node.prev = next, prev



class ListNode:
    def __init__(self, val=0, key=0):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)