from utils import *


#########################################################
#########################################################
@performance
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    # Parse ingredients
    ingredients = []
    for line in lines:
        if not line:
            continue
        parts = line.split(": ")[1].split(", ")
        props = []
        for part in parts:
            props.append(int(part.split(" ")[1]))
        ingredients.append(props)

    max_score = 0

    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - a - b):
                d = 100 - a - b - c

                capacity = (
                    a * ingredients[0][0]
                    + b * ingredients[1][0]
                    + c * ingredients[2][0]
                    + d * ingredients[3][0]
                )
                durability = (
                    a * ingredients[0][1]
                    + b * ingredients[1][1]
                    + c * ingredients[2][1]
                    + d * ingredients[3][1]
                )
                flavor = (
                    a * ingredients[0][2]
                    + b * ingredients[1][2]
                    + c * ingredients[2][2]
                    + d * ingredients[3][2]
                )
                texture = (
                    a * ingredients[0][3]
                    + b * ingredients[1][3]
                    + c * ingredients[2][3]
                    + d * ingredients[3][3]
                )
                calories = (
                    a * ingredients[0][4]
                    + b * ingredients[1][4]
                    + c * ingredients[2][4]
                    + d * ingredients[3][4]
                )

                if pt == 2 and calories != 500:
                    continue

                if capacity > 0 and durability > 0 and flavor > 0 and texture > 0:
                    score = capacity * durability * flavor * texture
                    max_score = max(max_score, score)

    return max_score


#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")
