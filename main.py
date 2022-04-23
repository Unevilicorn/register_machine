from typing import List
from instruction import Instruction, AddI, SubI, HaltI
from utils import log, encodeNatrual, getIntSubScript, getIntSuperScript
from encode import encodeInstructionMap, encodeList, encodeListPowerForm

encodeInput = [SubI(1, 1, 2),
               AddI(0, 0),
               SubI(2, 3, 4),
               AddI(0, 2),
               HaltI()]

decodeInput = 2**216*833  # 786432


def encode():

    arr = encodeInstructionMap(encodeInput)
    print(arr)
    # print(encodeList(arr))
    print(encodeListPowerForm(arr))


encode()

# decode()
