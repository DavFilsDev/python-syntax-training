# riot_threshold.py
# ----------------------------------------
# 🔥 Problem: Riot Threshold Model with Dunbar Limit
#
# Given a social graph (undirected) where each node represents a person
# and edges represent relationships (friends),
# each person has a threshold f(v) ∈ [0,1] (as a Fraction),
# which is the **minimum fraction of their neighbors** who must be rioting
# before they join the riot.
#
# Persons with f(v) = 0 riot immediately.
# Persons with f(v) > 1 never riot.
#
# The simulation runs until it reaches a stable point (no more new rioters).
#
# ➤ Goal: return the total number of people who will end up rioting.
# ➤ Constraints: Up to 25,000 people (N), but each person has few neighbors.
# ➤ Complexity: O(N) or O(N log N)

from collections import deque
from fractions import Fraction

def n_rioters(N, E, f):
    """
    :param N: int - number of nodes/people
    :param E: dict - adjacency list representing graph edges
    :param f: list[Fraction] - threshold for each node
    :return: int - final count of rioting people
    """
    # Status of each person: True if rioting
    rioting = [False] * N

    # Current number of rioting neighbors per person
    riot_neighbors = [0] * N

    # Initialize queue with people who have threshold = 0 (they riot immediately)
    queue = deque()
    for v in range(N):
        if f[v] == 0:
            rioting[v] = True
            queue.append(v)

    while queue:
        current = queue.popleft()
        for neighbor in E[current]:
            if rioting[neighbor]:
                continue  # already rioting
            riot_neighbors[neighbor] += 1
            total_neighbors = len(E[neighbor])
            # Check if the neighbor now has enough rioting friends to join
            if Fraction(riot_neighbors[neighbor], total_neighbors) >= f[neighbor]:
                rioting[neighbor] = True
                queue.append(neighbor)

    return sum(rioting)  # total number of people who ended up rioting

# Example usage (basic test)
if __name__ == "__main__":
    from fractions import Fraction

    N = 5
    E = {
        0: {1, 2},
        1: {0, 2, 3},
        2: {0, 1},
        3: {1, 4},
        4: {3}
    }
    f = [Fraction(0), Fraction(1, 2), Fraction(1), Fraction(1, 2), Fraction(1)]
    
    print("Number of rioters:", n_rioters(N, E, f))
