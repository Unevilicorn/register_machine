import math
from typing import List, Tuple

from instruction import Instruction, AddI, SubI, HaltI
from utils import decodeNatrual, decodeWhole, log, encodeNatrual, getIntSubScript, getIntSuperScript, powString
from configs import MULT_SYMBOL


# Decode instruction to a list of instructions
def decodeToIntList(encoded: int) -> List[int]:
    c = encoded
    out = []
    while c != 0:
        log(f"Decoding list {c}")  #
        (p, c) = decodeNatrual(c)
        log(f"= <<{p}, {c}>>")
        out.append(p)
    return out


# Decode a single instruction
def decodeInstruction(encoded: int) -> Instruction:
    log(f"Decoding Instruction {encoded}")

    # Is halt
    if encoded == 0:
        res = HaltI()
    else:
        (p, c) = decodeNatrual(encoded)

        if p % 2 == 0:
            # Is add instruction
            res = AddI(p // 2, c)
        else:
            # Is Sub instruction
            (t, f) = decodeWhole(c)
            res = SubI((p - 1) // 2, t, f)

    log(f"= {res}")
    return res

# Decode everything


def decodeAll(encodedList: List[int]) -> List[Instruction]:
    return list(map(lambda x: decodeInstruction(x), encodedList))
