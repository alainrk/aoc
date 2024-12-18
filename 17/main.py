from utils import *

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    global A
    global B
    global C

    A = ints(lines[0])[0]
    B = ints(lines[1])[0]
    C = ints(lines[2])[0]
    Program = ints(lines[4])

    def combo(n):
        if n < 4:
            return n
        if n == 4:
            return A
        if n == 5:
            return B
        if n == 6:
            return C
        if n == 7:
            return 0
        assert False

    def exec(program):
        global A
        global B
        global C
        ip = 0

        out = []
        while ip < len(program):
            opcode = program[ip]
            operand = program[ip + 1] if ip + 1 < len(program) else 0

            if opcode== 0:  # adv
                power = combo(operand)
                A //= (2 ** power)
            elif opcode== 1:  # bxl
                B ^= operand
            elif opcode== 2:  # bst
                B = combo(operand) % 8
            elif opcode== 3:  # jnz
                if A != 0:
                    ip = operand
                    continue
            elif opcode== 4:  # bxc
                B ^= C
            elif opcode== 5:  # out
                val = combo(operand) % 8
                out.append(val)
            elif opcode== 6:  # bdv
                power = combo(operand)
                B = A // (2 ** power)
            elif opcode== 7:  # cdv
                power = combo(operand)
                C = A // (2 ** power)

            ip += 2

        return out

    if pt==1:
        return exec(Program)
    else:
        q = deque([(len(Program), 0)])
        while q:
            pos, a = q.popleft()
            for i in range(8):
                A = a*8 + i
                B = 0
                C = 0
                o = list(map(int, exec(Program)))
                if o == Program[pos-1:]:
                    q.append((pos - 1, A))
                    if len(o) == len(Program):
                        return A

#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")

