from graph_modified import Graph
import sys


def calculate_community_connectivity(community, graph):
    """
    Calculate the connectivity within a community.

    Args:
        community (list): List of nodes representing a community.
        graph (Graph): Graph object containing adjacency information.

    Returns:
        tuple: A tuple containing the number of internal and external edges.
    """
    internal_edges = 0
    external_edges = 0
    for node in community:
        for neighbor in graph.adj[node]:
            if neighbor in community:
                internal_edges += 1
            else:
                external_edges += 1
    internal_edges /= 2
    return internal_edges, external_edges


def balance_communities(communities, graph, max_iterations=100):
    """
    Balance the communities to have roughly equal sizes.

    Args:
        communities (list): List of lists representing communities.
        graph (Graph): Graph object containing adjacency information.
        max_iterations (int): Maximum number of iterations for balancing.

    Returns:
        list: Balanced communities.
    """
    for _ in range(max_iterations):
        improved = False
        for i, community in enumerate(communities):
            for node in list(community):
                communities[i].remove(node)
                best_score = -1
                best_community = i
                for j, target_community in enumerate(communities):
                    target_community.append(node)
                    score = calculate_score(node, j, communities, graph)
                    if score > best_score:
                        best_score = score
                        best_community = j
                    target_community.remove(node)
                communities[best_community].append(node)
                if best_community != i:
                    improved = True
        if not improved:
            break
    return communities


def calculate_score(node, community_index, communities, graph):
    """
    Calculate the score for a node in a community.

    Args:
        node (int): Node index.
        community_index (int): Index of the community.
        communities (list): List of lists representing communities.
        graph (Graph): Graph object containing adjacency information.

    Returns:
        float: Connectivity score of the node within the community.
    """
    connectivity_score = 0
    for neighbor in graph.adj[node]:
        if neighbor in communities[community_index]:
            connectivity_score += 1
    if len(communities[community_index]) > 1:
        connectivity_score /= len(communities[community_index]) - 1
    return connectivity_score


def find_communities(graph, num_communities=4):
    """
    Find communities within the graph.

    Args:
        graph (Graph): Graph object containing adjacency information.
        num_communities (int): Number of communities to find.

    Returns:
        list: List of lists representing communities.
    """
    communities = [[] for _ in range(num_communities)]
    nodes = list(range(graph.n))
    for node in nodes:
        min_size = min([len(c) for c in communities])
        for community in communities:
            if len(community) == min_size:
                community.append(node)
                break
    return balance_communities(communities, graph)


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filepath>")
        return

    filepath = sys.argv[1]
    graph = Graph()
    graph.readgraph(filepath)
    graph.make_undirected()

    communities = find_communities(graph)
    for i, community in enumerate(communities, start=1):
        print(f"Society {i}: {sorted(community)}")


if __name__ == "__main__":
    main()
