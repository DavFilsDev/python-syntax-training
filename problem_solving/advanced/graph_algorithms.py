# graph_algorithms.py
# -----------------------------------------------------
# 🧩 Problem: Shortest Path in Unweighted Graph
#
# Given an unweighted, undirected graph represented as
# an adjacency list and two nodes (src, dest),
# find the length of the shortest path between them.
#
# Approach: Breadth-First Search (BFS)
# Time complexity: O(V + E)
# -----------------------------------------------------

from collections import deque

def shortest_path_length(graph, src, dest):
    """
    :param graph: dict[int, list[int]] – adjacency list
    :param src:   int                – start vertex
    :param dest:  int                – target vertex
    :return:      int                – number of edges in shortest path,
                                         or -1 if no path exists
    """
    visited = set([src])
    queue = deque([(src, 0)])  # (current_node, distance_so_far)

    while queue:
        node, dist = queue.popleft()
        if node == dest:
            return dist
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1  # dest not reachable

# Example usage
if __name__ == "__main__":
    G = {
        0: [1, 2],
        1: [0, 3],
        2: [0, 3],
        3: [1, 2, 4],
        4: [3]
    }
    print("Shortest path 0→4:", shortest_path_length(G, 0, 4))
    # Expected: 3 (0→1→3→4)
