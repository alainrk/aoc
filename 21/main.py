from copy import copy
from utils import *

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    if pt ==2: return

    # pad = [[7, 8, 9], [4, 5, 6], [1, 2, 3], [None, "A", "B"]]
    # rpad = [[None, "^", "A"], ["<", "v", ">"]]

    pad = {
        (0, 0): 7, (0, 1): 8, (0, 2): 9,
        (1, 0): 4, (1, 1): 5, (1, 2): 6,
        (2, 0): 1, (2, 1): 2, (2, 2): 3,
        (3, 1): 0, (3, 2): "A"
    }
    pad_inverse = {
        7: (0, 0), 8: (0, 1), 9: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        1: (2, 0), 2: (2, 1), 3: (2, 2),
        0: (3, 1), "A": (3, 2)
    }

    rpad = {
        (0, 1): "^", (0, 2): "A",
        (1, 0): "<", (1, 1): "v", (1, 2): ">"
    }
    rpad_inverse = {
        "^": (0, 1), "A": (0, 2),
        "<": (1, 0), "v": (1, 1), ">": (1, 2)
    }

    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dirsMap = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1)
    }
    dirsInverseMap = {
        (-1, 0): "^",
        (1, 0): "v",
        (0, -1): "<",
        (0, 1): ">"
    }

    res = 0
    codes = []
    for i, line in enumerate(lines):
        codes.append(line)

    pad_shortest = {}
    rpad_shortest = {}

    def shortest_paths_from_s(g, s, M):
        if s in M:
            return M[s]

        # Instead of distances, store lists of direction sequences
        paths = defaultdict(list)
        paths[s] = [[]]  # Start point has empty path

        # Store distances to ensure we only track shortest paths
        dists = defaultdict(lambda: float('inf'))
        dists[s] = 0

        q = [(0, s, [])]  # (distance, point, path)

        while q:
            d, (cx, cy), current_path = heappop(q)

            if dists[(cx, cy)] < d:
                continue

            for dx, dy in dirs:
                nx, ny = cx + dx, cy + dy
                if (nx, ny) not in g:
                    continue

                nd = d + 1
                if nd < dists[(nx, ny)]:
                    # Found a shorter path, clear existing paths
                    paths[(nx, ny)] = []
                    dists[(nx, ny)] = nd
                    # Add new path
                    new_path = current_path + [(dx, dy)]
                    paths[(nx, ny)].append(new_path)
                    heappush(q, (nd, (nx, ny), new_path))
                elif nd == dists[(nx, ny)]:
                    # Found alternative path of same length
                    new_path = current_path + [(dx, dy)]
                    paths[(nx, ny)].append(new_path)
                    heappush(q, (nd, (nx, ny), new_path))

        return paths

    def get_shortest_paths(inverse_pad_type, start, end, shortest_paths_type):
        return shortest_paths_type[inverse_pad_type[start]][inverse_pad_type[end]]

    # All shortest paths from any start to any end in DOOR PAD
    for start in pad_inverse.values():
        pad_shortest[start] = shortest_paths_from_s(pad, start, pad_shortest)

    # All shortest paths from any start to any end in ROBOT PAD
    for start in rpad_inverse.values():
        rpad_shortest[start] = shortest_paths_from_s(rpad, start, rpad_shortest)

    def create_sequences(code, typePadInverse, inverseMap, shortestPaths):
        def recursive_sequence_builder(index, curr, curr_seq):
            if index >= len(code):
                return [curr_seq]

            next_pos = code[index]
            next_pos = int(next_pos) if next_pos.isnumeric() else next_pos

            all_paths = get_shortest_paths(typePadInverse, curr, next_pos, shortestPaths)

            # All possible sequences
            sequences = []

            # For each possible path to the next position
            for path in all_paths:
                # Convert path directions to sequence moves
                path_sequence = []
                for direction in path:
                    path_sequence.append(inverseMap[direction])
                path_sequence.append("A")

                # Create new sequence with current path
                new_sequence = curr_seq + "".join(path_sequence)

                # Recursively build the rest of the sequences
                next_sequences = recursive_sequence_builder(index + 1, next_pos, new_sequence)
                sequences.extend(next_sequences)

            return sequences

        # Start the recursion from the initial position 'A' with an empty sequence
        return recursive_sequence_builder(0, "A", "")

    # print(create_sequences(codes[0], pad_inverse, dirsInverseMap, pad_shortest))

    # Me(rpad) => R1(rpad) => R2(rpad) => R3(pad) => Door
    for code in codes:
        bestcost, best = float('inf'), None
        for r1seq in create_sequences(code, pad_inverse, dirsInverseMap, pad_shortest):
            for r2seq in create_sequences(r1seq, rpad_inverse, dirsInverseMap, rpad_shortest):
                for r3seq in create_sequences(r2seq, rpad_inverse, dirsInverseMap, rpad_shortest):
                    if len(r3seq) < bestcost:
                        # print(f"----------\n{code = }\n{r1seq = }\n{r2seq = }\n{r3seq = }")
                        bestcost = len(r3seq)
                        best = r3seq
        print(f"{code = }\n{bestcost = }\n{best = }\n")
        res += ints(code)[0] * bestcost

    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")


'''
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
'''
