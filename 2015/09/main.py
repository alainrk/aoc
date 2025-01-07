from utils import *

#########################################################
#########################################################
@performance
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    G = defaultdict(list)
    for _, line in enumerate(lines):
        w = words(line)
        d = ints(line)
        G[w[0]].append((w[2], int(d[0])))
        G[w[2]].append((w[0], int(d[0])))

    size = float("inf") if pt == 1 else float("-inf")

    cities = list(G.keys())
    n = len(cities)

    # Create a mapping of city names to indices
    city_to_idx = {city: i for i, city in enumerate(cities)}

    # Create distance matrix
    dist = [[size] * n for _ in range(n)]
    for city in G:
        for neighbor, distance in G[city]:
            dist[city_to_idx[city]][city_to_idx[neighbor]] = distance

    # dp[(mask, pos)] represents shortest path visiting all cities in mask, ending at pos
    dp = {}

    def shortest_path(mask, pos):
        if mask == (1 << n) - 1:  # All cities visited
            return 0, [cities[pos]]

        state = (mask, pos)
        if state in dp:
            return dp[state]

        ans = size
        best_path = []

        # Try to visit an unvisited city
        for city in range(n):
            if mask & (1 << city) == 0:  # if city is not visited
                new_mask = mask | (1 << city)
                d, path = shortest_path(new_mask, city)
                if dist[pos][city] + d < ans:
                    ans = dist[pos][city] + d
                    best_path = [cities[pos]] + path

        dp[state] = (ans, best_path)
        return dp[state]

    # Try starting from each city
    min_distance = size
    best_path = []

    for start in range(n):
        # Initialize with only start city visited
        initial_mask = 1 << start
        distance, path = shortest_path(initial_mask, start)
        if distance < min_distance:
            min_distance = distance
            best_path = path

    return min_distance, best_path

#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")

