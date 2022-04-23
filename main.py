from typing import List
from decode import decodeAll
from instruction import Instruction, AddI, SubI, HaltI
from encode import encodeInstructionMap, encodeList, encodeListPowerForm
from decode import decodeToIntList, decodeAll

encodeInput = [SubI(1, 1, 2),
               AddI(0, 0),
               SubI(2, 3, 4),
               AddI(0, 2),
               HaltI()]

decodeInput = 2**216*833  # 786432


def encode(arr):
    earr = encodeInstructionMap(arr)
    print(earr)
    efarr = encodeList(earr)
    print(encodeListPowerForm(earr))
    return efarr


def decode(n):
    darr = decodeToIntList(n)
    print(darr)

    dfarr = decodeAll(darr)
    print(list(map(str, dfarr)))
    return dfarr


# encode(encodeInput)
decode(decodeInput)

# decode(encode(encodeInput))

print(encodeListPowerForm([1, 2, 3, 4]))
