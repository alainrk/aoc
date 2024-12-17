from utils import *

#########################################################
#########################################################
def solve(__file, pt):
    lines = [line.strip() for line in open(__file)]
    if len(lines) == 0:
        return -1

    res = 0
    A = ints(lines[0])[0]
    B = ints(lines[1])[0]
    C = ints(lines[2])[0]
    Program = ints(lines[4])
    ip = 0
   
    # Combo_Ops:
    # 0-3 literal 0-3
    # 4: Reg A
    # 5: Reg B
    # 6: Reg C
    # 7: Reserved
    #
    # Instructions:
    # 0 (adv) -> Division A/2**Combo_Op e.g. Op=3 A/2**3 = 2**8 -> Write A=Trunc_int(A/8)
    # 1 (bxl) -> Bitwise XOR of B. B=XOR(B)
    # 2 (bst) -> B=Op % 8
    # 3 (jnz) -> Nop if A!=0, else ip=literal_op (NO increase ip+=2 after)
    # 4 (bxc) -> Bitwise XOR of B and C. C=bXOR(B, C) -> Ignore the Op
    # 5 (out) -> Output Combo_Op % 8 (CSV if many)
    # 6 (bdv) -> B=Trunc_int(A/2**Combo_Op)
    # 7 (cdv) -> C=Trunc_int(A/2**Combo_Op)

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

    out = []
    while ip < len(Program):
        opcode = Program[ip]
        operand = Program[ip + 1] if ip + 1 < len(Program) else 0

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
#########################################################
#########################################################

if __name__ == "__main__":
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    i_sol1 = solve(input_file, 1)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol1 = }\033[0m")
    i_sol2 = solve(input_file, 2)
    print(f"\033[1m\033[92m[SOLUTION] {i_sol2 = }\033[0m")

