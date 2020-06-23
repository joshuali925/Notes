```python
from collections import defaultdict, deque
def topological(numNodes, prereqs):
    # prereqs: [[nodeA, prereqA], [nodeB, prereqB], ...]
    # for each node, we visit all neighbors depending on it recursively
    # when finished, we can add this node to the beginning of the answers list
    # we add it to the beginning to skip nodes added in the recursion
    
    ans = deque()
    visited = [0] * numNodes
    graph = defaultdict(list)
    for node, prereq in prereqs:
        graph[prereq].append(node)
    
    def dfs(node):
        # already visited and added to answers, skip
        if visited[node] == 1: return True
        # we came from this node and encountered it again (cycle, no solution)
        if visited[node] == -1: return False
        
        # visiting this node
        visited[node] = -1
        for prereq in graph[node]:
            if not dfs(prereq):
                return False
        
        # all nodes depending on it had been visited and added to the answers list
        # mark it as visited and add it to the beginning of the answers list
        visited[node] = 1
        ans.appendleft(node)
        return True
    
    for node in range(numNodes):
        if not dfs(node):
            return False
    
    return ans
```
