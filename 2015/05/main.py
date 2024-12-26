from utils import *

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    """
    A nice string is one with all of the following properties:

    It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
    """
    def nice1(word):
        c = Counter(word)

        # At least 3 vowels
        if c["a"] + c["e"] + c["i"] + c["o"] + c["u"] < 3:
            return False

        ok = False
        prev = word[0]
        for j in range(1, len(word)):
            if f"{prev}{word[j]}" in ["ab", "cd", "pq", "xy"]:
                ok = False
                break
            # 2 eq in a row
            if word[j] == prev:
                ok = True
            prev = word[j]

        return ok

    """
    Now, a nice string is one with all of the following properties:

    It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
    It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
    """
    def nice2(word):
        pairs = {}

        hasPair = False
        hasXYX = False
        prev = word[0]
        for i in range(1, len(word)):
            p = f"{prev}{word[i]}"
            prev = word[i]

            # xyx case
            if i < len(word) - 1:
                xyx = f"{p}{word[i+1]}"
                if xyx == xyx[::-1]:
                    hasXYX = True

            if p not in pairs:
                pairs[p] = (0, -1) # count, last_pos

            # overlaps
            if pairs[p][1] != i - 1:
                # otherwise update
                pairs[p] = (pairs[p][0] + 1, i)
                if pairs[p][0] > 1:
                    hasPair = True
            if hasPair and hasXYX:
                return True
        return False

    ## main
    res = 0
    for _, word in enumerate(lines):
        if pt == 1:
            if nice1(word):
                res += 1
        else:
            if nice2(word):
                res += 1

    return res
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")

