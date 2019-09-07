# Union Find
```python
class UnionFind():
    def __init__(self):
        self.parents = {}

    def union(self, x, y):
        if x not in self.parents: self.parents[x] = x
        if y not in self.parents: self.parents[y] = y

        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parents[root_y] = root_x

    def find(self, x):
        if x not in self.parents: self.parents[x] = x

        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def is_connected(self, x, y):
        if x not in self.parents or y not in self.parents:
            return False
        return self.find(x) == self.find(y)
```

## `union()` With Ranks
```python
class UnionFind():
    def __init__(self):
        self.parents = {}
        self.ranks = {}
    
    def make_set(self, x):
        self.parents[x] = x
        self.ranks[x] = 0

    def union(self, x, y):
        if x not in self.parents: self.make_set(x)
        if y not in self.parents: self.make_set(y)

        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.ranks[root_x] < self.ranks[root_y]:
                self.parents[root_x] = root_y
            elif self.ranks[root_x] > self.ranks[root_y]:
                self.parents[root_y] = root_x
            else:
                self.parents[root_x] = root_y
                self.ranks[root_y] += 1

    def find(self, x):
        if x not in self.parents: self.make_set(x)
        
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def is_connected(self, x, y):
        if x not in self.parents or y not in self.parents:
            return False
        return self.find(x) == self.find(y)
```

## Usage
```python
uf = UnionFind()
uf.union('hello', 'world')
uf.union('world', '!')
uf.union('not', 'related')
print(uf.is_connected('hello', '!'))  # True
print(uf.is_connected('hello', 'not'))  # False
```

# Minimum Spanning Tree (Kruskal's algorithm)
```python
# edges = [(vertex, vertex, weight), ...]
def MST(edges):
    edges.sort(key=lambda x: x[2])  # sort by weight ascending
    results = []
    uf = UnionFind()

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            results.append((u, v, weight))
            uf.union(u, v)

    return results

edges = [(0, 1, 10), (0, 2, 6), (0, 3, 5), (1, 3, 15), (2, 3, 4)]
print(MST(edges))  # [(2, 3, 4), (0, 3, 5), (0, 1, 10)]
```
