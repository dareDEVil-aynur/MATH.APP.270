# A template for Ford Fulkerson algorithm and min cut

from graph import Graph
from copy import deepcopy as copy
from queue import Queue
import sys

# from icecream import ic


## This code assumes flow is dictionary with keys (u,v) and values flow(u,v)
## Define the sum of two flows
def SumFlow(f1, f2):
    f = {}
    for u, v in set(f1.keys()) | set(f2.keys()):
        if not (u, v) in f1:
            f[(u, v)] = f2[(u, v)]
        elif not (u, v) in f2:
            f[(u, v)] = f1[(u, v)]
        else:
            f[(u, v)] = f1[(u, v)] + f2[(u, v)]
    return f


## This is an EXAMPLE of how the flow network class can be implemented, some implementation is missing
class FlowNetwork:
    def __init__(self, G) -> None:
        self.G = G
        # print(self.G.w)
        self.FindSource()
        self.FindSink()

    ## Find the source, it is the first vertex with a non-empty adjacency list:
    def FindSource(self):
        for u in range(self.G.n):
            if len(self.G.adj[u]) > 0:
                self.s = u
                return

    ## Find the sink. It is the last vertex.
    def FindSink(self):
        self.t = self.G.n - 1

    # Define the value of a flow
    def FlowValue(self, f):
        return sum(f[(self.s, u)] for u in self.G.adj[self.s] if (self.s, u) in f)

    ## Create a residual graph
    def MakeResidual(self, f):
        ## Copy the graph:
        G = copy(self.G)
        for u, v in f:
            c = 0
            ## Copy the weight
            if (u, v) in G.w:
                c = G.w[(u, v)]
            # calculate residual capasity
            cf = c - f[(u, v)]
            ## It is an error if the residual capacity is negative
            if cf < 0:
                raise Exception("capacity violation in f")
            ## Add the edge if the residual capacity is positive
            if not v in G.adj[u]:
                G.addEdge(u, v)
            G.w[(u, v)] = cf
        return G

    def FindAugPath(self, Gr, s=None, t=None):
        """
        Identifies an augmenting path from source to sink using DFS.
        """
        s = s or self.s
        t = t or self.t
        visited, stack = set(), [(s, [s])]

        while stack:
            current, path = stack.pop()
            if current == t:
                return path

            visited.add(current)
            for next_node in Gr.adj[current]:
                if next_node not in visited and Gr.w.get((current, next_node), 0) > 0:
                    stack.append((next_node, path + [next_node]))

        return []

    ## Make an augmenting flow from a path
    def MakeAugFlow(self, path, Gr=None):
        if Gr is None:
            Gr = self.G
        f = {}
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]
            if (u, v) not in Gr.w or Gr.w[(u, v)] == 0:
                raise Exception("Edge not in Gr or saturated")
            f[(u, v)] = 0
        cf = min([Gr.w[(u, v)] for (u, v) in f])
        for u, v in f:
            f[(u, v)] = cf
        return f

    def FordFulkerson(self):
        f = {}
        G = self.G
        Gr = self.MakeResidual(f)
        ap = self.FindAugPath(G)
        while ap != []:
            fp = self.MakeAugFlow(ap, Gr)
            f = SumFlow(f, fp)
            Gr = self.MakeResidual(f)
            ap = self.FindAugPath(Gr)
        return f

    def MinCutEdges(self):
        f = self.FordFulkerson()
        S = set()
        visited = set([self.s])
        self.dfs_visit(self.s, visited, f)

        cut_edges = [
            (u, v)
            for u in visited
            for v in self.G.adj[u]
            if v not in visited and (u, v) in self.G.w
        ]
        cut_weight_sum = sum(self.G.w[(u, v)] for u, v in cut_edges)

        if cut_edges:
            edges_str = ", ".join(f"({u},{v})" for u, v in cut_edges)
            print(
                f"The 'correct answer' consists of {len(cut_edges)} edges. \n"
                f"The edges are: [{edges_str}]."
            )
        else:
            print("No edges are crossing the minimum cut,")

        print(f"Total flow through the minimum cut: {cut_weight_sum}.")
        return cut_edges

    def dfs_visit(self, node, visited, f):
        """
        Helper method for DFS to mark nodes reachable from 'node' considering the residual capacities.
        """
        for next_node in self.G.adj[node]:
            if (
                next_node not in visited
                and (node, next_node) in self.G.w
                and self.G.w[(node, next_node)] - f.get((node, next_node), 0) > 0
            ):
                visited.add(next_node)
                self.dfs_visit(next_node, visited, f)


if __name__ == "__main__":
    graph = Graph()
    graph.readgraph(sys.argv[1])
    flow_network = FlowNetwork(graph)
    min_cut_edges = flow_network.MinCutEdges()
