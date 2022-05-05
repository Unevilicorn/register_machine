from decode import decodeInstruction, decodeToIntList, decodeAll
from encode import encodeInstructionMap, encodeList, encodeListPowerForm
from instruction import AddI, SubI, HaltI
from program import Program

# encodeInput = [SubI(1, 1, 2),
#                AddI(0, 0),
#                SubI(2, 3, 4),
#                AddI(0, 2),
#                HaltI()]

# encodeInput = [SubI(1, 1, 6),
#                SubI(2, 2, 4),
#                AddI(0, 3),
#                AddI(3, 1),
#                SubI(3, 5, 0),
#                AddI(2, 4),
#                HaltI()
#                ]

encodeInput = [SubI(0, 1, 4),
               AddI(1, 2),
               SubI(0, 3, 4),
               AddI(2, 0),
               SubI(1, 4, 5),
               SubI(2, 6, 7),
               AddI(0, 5),
               HaltI()]

# encode(encodeInput)
# decode(decodeInput)

# decode(encode(encodeInput))

# print(encodeList([3]))       # 8
# print(encodeList([1, 3]))    # 34
# print(encodeList([2, 1, 3])) # 276

# print(decodeToIntList(8))   # [3]
# print(decodeToIntList(34))  # [1, 3]
# print(decodeToIntList(276))  # [2, 1 ,3]


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


def runProgram(state, instructions):
    program = Program(state, instructions)
    program.execute(10)


# nl = '\n'
# print(f"{nl.join(str(x) for x in encodeInput)}")
# runProgram(State(0, [0, 1, 2]), encodeInput)

# encode(encodeInput)
# print(encodeInstructionMap(encodeInput))
decodeAll([1144, 448])
