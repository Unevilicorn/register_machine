from tokenize import String
import configs


_SUBSCRIPTS = dict(zip(u"0123456789", u"₀₁₂₃₄₅₆₇₈₉"))
_SUPERSCRIPTS = dict(zip(u"0123456789", u"⁰¹²³⁴⁵⁶⁷⁸⁹"))


# Encodes N x N -> N
def encodeWhole(i: int, j: int) -> int:
    return 2**i * (2 * j + 1) - 1


# Encodes N x N -> N
def encodeNatrual(i: int, j: int) -> int:
    return 2**i * (2 * j + 1)


# Special log function that uses the log varaible
def log(string: str) -> None:
    if configs.LOG:
        print(string)


# Get superscript for a number
def getIntSuperScript(num: int) -> str:
    return "".join(map(lambda x: _SUPERSCRIPTS[str(x)], str(num)))


# Get subscript for a number
def getIntSubScript(num: int) -> str:
    return "".join(map(lambda x: _SUBSCRIPTS[str(x)], str(num)))
