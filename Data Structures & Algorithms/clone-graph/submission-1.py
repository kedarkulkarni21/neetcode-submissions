"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        start = node
        visited = set()
        visited.add(start)
        stack = [start]
        old_to_new = {}

        while stack:
            element = stack.pop()
            new_element = Node(val=element.val)
            old_to_new[element] = new_element

            for nei in element.neighbors:
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)

        for old, new in old_to_new.items():
            for nei in old.neighbors:
                new.neighbors.append(old_to_new[nei])


        return old_to_new[start]