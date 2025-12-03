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
def solve(__file, pt):
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
            if pt == 1:
                l = len(s) // 2
                if s[l:] == s[:l]:
                    res += n
            if pt == 2:
                for l in reversed(range(1, len(s) // 2 + 1)):
                    if all_equal(split_in_chunks(s, l)):
                        res += n
                        break

    return res


#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")
