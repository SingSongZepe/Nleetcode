
from typing import List, Dict
from collections import deque
import heapq

# my original solution
# but has a testcase that can't pass
class Graph:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        # d -> 0 -> 2: 5
        #        -> 1: 2
        #   -> 3 -> 0: 3
        #   -> 1 -> 2: 1
        self.d: Dict[int, Dict[int, int]] = {}
        for f, t, w in edges:
            if f not in self.d:
                self.d[f] = {}
            self.d[f][t] = w

    def addEdge(self, edge: List[int]) -> None:
        f, t, w = edge
        if f not in self.d:
            self.d[f] = {}

        # if edge f-t exists, then just update new weight to it
        self.d[f][t] = w

    def shortestPath(self, node1: int, node2: int) -> int:

        mark = {node1}
        dq = deque([node1])
        sd: List[int] = [-1] * self.n
        sd[node1] = 0  # node1 to node1, the shortest distance is 0

        while dq:

            for _ in range(len(dq)):
                f = dq.popleft()

                if f not in self.d:
                    break

                for t, w in self.d[f].items():
                    if sd[t] == -1:
                        sd[t] = sd[f] + w
                    else:
                        sd[t] = min(sd[f] + w, sd[t])

                mi = float('inf')
                miidx = -1
                for i, d in enumerate(sd):
                    if i in mark:
                        continue
                    if d != -1 and mi > d:
                        mi = d
                        miidx = i
                mark.add(miidx)
                dq.append(miidx)

                if node2 in mark:
                    return sd[node2]

        return sd[node2]


# my solution after modifying of AI
class Graph1:
    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.d: Dict[int, Dict[int, int]] = {}
        for f, t, w in edges:
            if f not in self.d:
                self.d[f] = {}
            self.d[f][t] = min(self.d[f].get(t, float('inf')), w)

    def addEdge(self, edge: List[int]) -> None:
        f, t, w = edge
        if f not in self.d:
            self.d[f] = {}
        self.d[f][t] = min(self.d[f].get(t, float('inf')), w)

    def shortestPath(self, node1: int, node2: int) -> int:
        pq = [(0, node1)]
        sd = {node: float('inf') for node in range(self.n)}
        sd[node1] = 0

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_distance > sd[current_node]:
                continue

            if current_node in self.d:
                for neighbor, weight in self.d[current_node].items():
                    distance = current_distance + weight

                    if distance < sd[neighbor]:
                        sd[neighbor] = distance
                        heapq.heappush(pq, (distance, neighbor))

        return sd[node2] if sd[node2] != float('inf') else -1

# The best practice
# mention me that you needn't use dict to describe edges
# because you can find the node's edges directly by its idx(node)
# you can say that hashed yet
class Graph2:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.graph = [[] for _ in range(n)]
        for from_node, to_node, cost in edges:
            self.graph[from_node].append((to_node, cost))

    def addEdge(self, edge: List[int]) -> None:
        from_node, to_node, cost = edge
        self.graph[from_node].append((to_node, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        pq = [(0, node1)]
        dist = [float('inf')] * self.n
        dist[node1] = 0

        while pq:
            current_cost, current_node = heapq.heappop(pq)

            if current_node == node2:
                return current_cost

            # ! excellent optimization
            if current_cost > dist[current_node]:
                continue

            for neighbor, edge_cost in self.graph[current_node]:
                new_cost = current_cost + edge_cost
                if new_cost < dist[neighbor]:
                    dist[neighbor] = new_cost
                    heapq.heappush(pq, (new_cost, neighbor))

        return -1 if dist[node2] == float('inf') else dist[node2]


# my best practice
class Graph3:

    def __init__(self, n: int, edges: List[List[int]]):
        self.n = n
        self.edges = [[] for _ in range(n)]
        for f, t, w in edges:
            self.edges[f].append((t, w))

    def addEdge(self, edge: List[int]) -> None:
        f, t, w = edge
        self.edges[f].append((t, w))

    def shortestPath(self, node1: int, node2: int) -> int:

        dq = [(0, node1)]
        sd = [float('inf')] * self.n
        sd[node1] = 0

        while dq:
            curr_w, curr_n = heapq.heappop(dq)

            if curr_n == node2:
                return curr_w

            if curr_w > sd[curr_n]:
                continue

            for t, w in self.edges[curr_n]:
                new_w = curr_w + w
                if new_w < sd[t]:
                    sd[curr_n] = new_w
                    heapq.heappush(dq, (new_w, t))

        return -1 if sd[node2] == float('inf') else sd[node2]



def main():
    print('Hello World')

if __name__ == '__main__':
    main()