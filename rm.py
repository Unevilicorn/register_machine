import math


def encode1(i, j):
    return 2**i * (2 * j + 1) - 1


def encode2(i, j):
    return 2**i * (2 * j + 1)


def encodel(arr):
    if len(arr) == 0:
        return None

    prev = arr.pop()
    if len(arr) == 0:
        return encode2(prev, 0)

    while len(arr) > 0:
        prev = encode2(arr.pop(), prev)

    return prev


def calc_instr(arr):
    s = 0
    while len(arr) > 0:
        val = arr.pop()
        if val == "HALT":
            s += 0
            continue

        prev = arr.pop()
        if len(arr) == 0:
            s += encode2(2*prev, val)
            continue

        pprev = arr.pop()
        if len(arr) == 0:
            s += encode2(2 * abs(pprev) + 1, encode1(prev, val))
            continue
    return s


def calc_all_instr(arr):
    return list(map(calc_instr, arr))


def combine_nums(arr):
    size = len(arr)

    cur = 0

    for i in range(0, size):
        cur = encode2(arr[size - i - 1], cur)

    return cur

# Encode a list
def calc_combine_all(arr):
    return combine_nums(calc_all_instr(arr))


def decodep(n):
    return decodel(n + 1)


def decodel(n):
    pn = n & ~(n - 1)
    p = math.log2(pn)
    c = ((n / pn) - 1) / 2
    return [int(p), int(c)]


def decode_all(n):
    arr = []
    while n != 0:
        [c, n] = decodel(n)
        arr.append(c)

    return arr


def translate(n):
    if n == 0:
        return ["HALT"]

    [c, n] = decodel(n)

    if c % 2 == 0:
        r = int(c / 2)
        return [r, n]
    else:
        [j, k] = decodep(n)
        r = int((c - 1) / 2)
        return [-r, j, k]


def translate_all(arr):
    return list(map(translate, arr))

def calc_translate_all(n):
    return translate_all(decode_all(n))


print(decode_all(2**216*833))
print(calc_translate_all(2**216*833))
