# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val: int = val
        self.neighbors: list[Node] = neighbors if neighbors is not None else []


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        # This needs to be a dictionary in which I track the instance of the copies. With a set it doesnt work.
        # Suppose I have a square graph with 4 elements. Everything works nice as long as I go DFS from node 1 to 4 (clock wise). Then i go back to the node 1.
        # Now i start traversing counter clock wise, so from 1 then i go to 4. In this case, value 4 is already present in the visited list, so i return
        # node directly. But the node I am returning now IS NOT THE COPY, but the original node number 4!!
        # To solve this issue, i need to return always the copy, thus i need the dictionary.
        # visited = set()

        visited = {}

        def dfs(node: Optional[Node], visited: set):
            if node in visited:
                return visited[node]

            copy_node = Node(node.val)

            visited[node] = copy_node

            for neighbor in node.neighbors:
                copy_node.neighbors.append(dfs(neighbor, visited))

            return copy_node

        return dfs(node, visited) if node else None
