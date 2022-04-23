import math
from typing import Tuple
import configs


_SUBSCRIPTS = dict(zip(u"0123456789", u"₀₁₂₃₄₅₆₇₈₉"))
_SUPERSCRIPTS = dict(zip(u"0123456789", u"⁰¹²³⁴⁵⁶⁷⁸⁹"))


# Encodes N x N -> N+
def encodeNatrual(i: int, j: int) -> int:
    return 2**i * (2 * j + 1)


# Encodes N x N -> N
def encodeWhole(i: int, j: int) -> int:
    return encodeNatrual(i, j) - 1


# Deocode current int to two ints
def decodeNatrual(encoded: int) -> Tuple[int, int]:
    pn = encoded & ~(encoded - 1)
    p = math.log2(pn)
    c = ((encoded // pn) - 1) // 2

    return (int(p), int(c))


# Decodes whole numbers into two
def decodeWhole(encoded: int) -> Tuple[int, int]:
    return decodeNatrual(encoded + 1)


# Special log function that uses the log varaible
def log(string: str) -> None:
    if configs.LOG:
        print(string)


def powString(base: int, exponent: int) -> str:
    if configs.USE_SUPERSCRIPTS:
        return f"{base}{getIntSuperScript(exponent)}"

    return f"{base}**{exponent}"


# Get superscript for a number
def getIntSuperScript(num: int) -> str:
    return "".join(map(lambda x: _SUPERSCRIPTS[str(x)], str(num)))


# Get subscript for a number
def getIntSubScript(num: int) -> str:
    return "".join(map(lambda x: _SUBSCRIPTS[str(x)], str(num)))
