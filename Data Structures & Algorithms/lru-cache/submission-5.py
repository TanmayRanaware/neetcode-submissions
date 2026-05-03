class Node:
  def __init__(self, val=0, key=0):
    self.key=key
    self.val=val
    self.prev=None
    self.nex=None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={}
        self.left = Node()
        self.right = Node()
        self.left.nex=self.right
        self.right.prev=self.left

    def remove(self, node):
        prev=node.prev
        nex=node.nex
        prev.nex=nex
        nex.prev=prev

    def insert(self, new_node):
        prev_mru=self.right.prev
        prev_mru.nex=new_node
        new_node.prev=prev_mru
        new_node.nex=self.right
        self.right.prev=new_node

    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.remove(node)    
        self.insert(node)
        return node.val

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node_to_remove = self.cache[key]
            self.remove(node_to_remove)
        new_node=Node(value, key)
        self.insert(new_node)
        self.cache[key]=new_node
        if self.cap<len(self.cache):
            lru=self.left.nex
            self.remove(lru)
            del self.cache[lru.key]
        

        
