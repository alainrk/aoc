from utils import *


def split_in_chunks(s, n):
    res = []
    start, end = 0, n
    while start < len(s):
        res.append(s[start:end])
        start += n
        end += n
    return res


def all_equal(arr):
    s = arr[0]
    for p in arr[1:]:
        if p != s:
            return False
        s = p
    return True


#########################################################
#########################################################
@performance
def solve_pt1(__file):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    ranges = []
    for n, line in enumerate(lines):
        chunks = line.split(",")
        ranges = [list(map(int, x.split("-"))) for x in chunks]
        # Only one line
        break

    for r in ranges:
        for n in range(r[0], r[1] + 1):
            s = str(n)
            l = len(s) // 2
            if s[l:] == s[:l]:
                res += n

    return res


@performance
def solve_pt2(__file):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    ranges = []
    maxn = 0
    for n, line in enumerate(lines):
        chunks = line.split(",")
        ranges = [list(map(int, x.split("-"))) for x in chunks]
        # Only one line
        break

    maxn = 0
    for _, m in ranges:
        maxn = max(maxn, m)

    def in_ranges(n):
        for l, r in ranges:
            if l <= n <= r:
                return True, (l, r)
        return False, None

    s = set()

    # e.g. d = [1, 2, 3, ..., 24, 25, ..., 100, 101, ...]
    #      num = [1, 11, 111, ..., 2, 22, 222, ..., 100, 100100, 100100100, ...]
    for d in range(1, floor(sqrt(maxn))):
        i = 2
        num = int(str(d) * i)
        while num < maxn:
            if num not in s:
                found, r = in_ranges(num)
                if found:
                    s.add(num)
                    res += num
            i += 1
            num = int(str(d) * i)
            # time.sleep(0.3)

    return res


#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve_pt1(input_file)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve_pt2(input_file)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")
