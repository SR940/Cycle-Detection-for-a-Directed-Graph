from collections import defaultdict

class CycleDetect:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdges(self, s, t):
        self.graph[s].append(t)

    def isCyclicGraph(self, v, visited, recStack):
        visited[v] = True
        recStack[v] = True

        # Recur for all neighbours, if any neighbour is visited and in recStack then graph is cyclic
        for neighbourNode in self.graph[v]:
            if not visited[neighbourNode]:
                if self.isCyclicGraph(neighbourNode, visited, recStack):
                    return True
            elif recStack[neighbourNode]:
                return True

        # The node needs to be popped from recursion stack before function ends
        recStack[v] = False
        return False

    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if not visited[node]:
                if self.isCyclicGraph(node, visited, recStack):
                    return True
        return False

# Driver code
if __name__ == '__main__':
    num_vertices,num_edges = map(int, input().split())


    g = CycleDetect(num_vertices)

    for _ in range(num_edges):
        s, t = map(int, input().split())
        g.addEdges(s, t)

    if g.isCyclic():
        print("1")
    else:
        print("0")
