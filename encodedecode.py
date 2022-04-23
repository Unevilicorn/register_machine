from typing import List
from instruction import Instruction, AddI, SubI, HaltI
from utils import encodeNatrual, getIntSubScript, getIntSuperScript
from utils import log


# Encodes a list of instructions into int
def encodeInstructionMap(instructions: List[Instruction]) -> List[int]:
    return list(map(lambda x: x.encode(), instructions))


# Encoding a list
def encodeList(encodedInstructions: List[int]) -> int:
    curr = 0
    for n in reversed(encodedInstructions):
        total = encodeNatrual(n, curr)
        log(f"encoding <<{n}, {curr}>> = {total}")
        curr = total
    return total


# Encoding a list but leave in the power form
def encodeListPowerForm(encodedInstructions: List[int]) -> str:
    curr = "1"
    for n in reversed(encodedInstructions):
        curr = f"2{getIntSuperScript(n)} x ({curr})"
    return curr


encodeInput = [SubI(1, 1, 2),
               AddI(0, 0),
               SubI(2, 3, 4),
               AddI(0, 2),
               HaltI()]


def encode():

    arr = encodeInstructionMap(encodeInput)
    print(arr)
    # print(encodeList(arr))
    print(encodeListPowerForm(arr))


# encode()
