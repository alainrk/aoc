import collections
import heapq
from utils import *


class UF:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def union(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)

        # Same set already
        if roota == rootb:
            return False

        # Merge by rank
        if self.rank[roota] < self.rank[rootb]:
            self.parent[roota] = rootb
        elif self.rank[roota] > self.rank[rootb]:
            self.parent[rootb] = roota
        else:
            self.parent[rootb] = roota
            self.rank[roota] += 1

        return True

    def find(self, a):
        if a not in self.parent:
            self.parent[a] = a
            self.rank[a] = 0
            return a

        root = a
        while root != self.parent[root]:
            root = self.parent[root]

        curr = a
        while curr != root:
            next = self.parent[curr]
            self.parent[curr] = root
            curr = next

        return root


def dist(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2) + math.pow(z1 - z2, 2))


#########################################################
#########################################################
@performance
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    boxes = []
    for i, line in enumerate(lines):
        boxes.append(tuple(map(int, line.split(","))))

    # print(boxes)
    # return

    B = len(boxes)
    mind = float("inf")
    conns = []  # (dist, idxA, idxB)

    uf = UF()

    for i in range(B):
        for j in range(i + 1, B):
            d = dist(boxes[i], boxes[j])
            conns.append((d, i, j))

    conns.sort()

    LIMIT = 1000
    if pt == 1 and "test" in __file:
        LIMIT = 10
    if pt == 2:
        LIMIT = float("inf")

    clusters = len(lines)

    # Use min in case there are fewer than 1000 total pairs (small inputs)
    if pt == 1:
        for i in range(min(len(conns), LIMIT)):
            d, a, b = conns[i]
            merged = uf.union(a, b)
    else:
        for d, a, b in conns:
            if uf.union(a, b):
                clusters -= 1
                if clusters == 1:
                    x1 = boxes[a][0]
                    x2 = boxes[b][0]
                    return x1 * x2

    c = collections.defaultdict(int)
    for b in range(B):
        root = uf.find(b)
        c[root] += 1

    q = []
    for i in c:
        heapq.heappush(q, -c[i])

    if len(q) < 3:
        print("Error: Fewer than 3 circuits found.")
        return 0

    res = 1
    res *= -(heapq.heappop(q))
    res *= -(heapq.heappop(q))
    res *= -(heapq.heappop(q))

    return res


#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")
