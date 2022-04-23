from typing import List
from instruction import Instruction
from utils import encodeNatrual, powString
from configs import MULT_SYMBOL


# Encodes a list of instructions into int
def encodeInstructionMap(instructions: List[Instruction]) -> List[int]:
    return list(map(lambda x: x.encode(), instructions))


# Encoding a list
def encodeList(encodedInstructions: List[int]) -> int:
    curr = 0
    for n in reversed(encodedInstructions):
        total = encodeNatrual(n, curr)
        # log(f"encoding <<{n}, {curr}>> = {total}")
        curr = total
    return total


# Encoding a list but leave in the power form
def encodeListPowerForm(encodedInstructions: List[int]) -> str:
    curr = "1"
    for n in reversed(encodedInstructions):
        curr = f"{powString(2, n)} {MULT_SYMBOL} (2 {MULT_SYMBOL} {curr} + 1)"
    return curr
