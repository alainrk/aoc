from utils import *

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    E = []
    G = defaultdict(set)
    for i, line in enumerate(lines):
        e = words(line)
        G[e[0]].add(e[1])
        G[e[1]].add(e[0])
        E.append(e)

    if pt == 1:
        comb = combinations(G.keys(), 3)
        CC3 = set()
        for a, b, c in comb:
            if b in G[a] and c in G[a] and c in G[b]:
                CC3.add((a, b, c))

        for cc in CC3:
            # check if any c in cc startswith t
            if any(c.startswith("t") for c in cc):
                res += 1
        return res

    # pt2

    def find_max_clique(g):
        def bron_kerbosch(r, p, x, max_clique) -> None:
            if len(p) == 0 and len(x) == 0:
                if len(r) > len(max_clique[0]):
                    max_clique[0] = r.copy()
                return

            pivot = max((p | x), key=lambda u: len(p & g[u]), default=None)

            if pivot is None and p:
                pivot = next(iter(p))

            explore = p - g[pivot] if pivot else p.copy()

            for v in explore:
                neighbors = g[v]
                bron_kerbosch(
                    r | {v},
                    p & neighbors,
                    x & neighbors,
                    max_clique
                )
                p.remove(v)
                x.add(v)

        # init stuff
        r = set()
        p = set(g.keys())
        x = set()
        max_clique = [set()]

        bron_kerbosch(r, p, x, max_clique)

        return max_clique[0]

    clique = find_max_clique(G)
    print(",".join(sorted(clique)))

    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")

