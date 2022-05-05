
import string
from abc import abstractmethod
from configs import MULT_SYMBOL
from utils import encodeNatrual, encodeWhole, log, getIntSubScript, powString
from state import State


class Instruction:
    @abstractmethod
    def encode(self) -> int:
        raise NotImplementedError

    @abstractmethod
    def execute(self, state: State) -> None:
        raise NotImplementedError


class AddI(Instruction):
    def __init__(self, register: int, label: int) -> None:
        self.register = register
        self.label = label

    # Encode using <<2i, j>>
    def encode(self) -> int:
        result = encodeNatrual(2 * self.register, self.label)
        log(f"Encoding {self}:")
        log(f"    Encoding <<2 {MULT_SYMBOL} {self.register}, {self.label}>>:")
        log(f"    = <<{2 * self.register}, {self.label}>>:")
        log(f"    = {powString(2, 2 * self.register)} {MULT_SYMBOL} (2 {MULT_SYMBOL} {self.label} + 1)")
        log(f"    = {result}")
        log(f"= {result}")
        return result

    def execute(self, state: State) -> None:
        state.registers[self.register] += 1
        state.jumpTo(self.label)

    def __str__(self) -> string:
        return f"R{getIntSubScript(self.register)}+ -> L{getIntSubScript(self.label)}"


class SubI(Instruction):
    def __init__(self, register: int, trueLabel: int, falseLabel: int) -> None:
        self.register = register
        self.trueLabel = trueLabel
        self.falseLabel = falseLabel

    # Encode using <<2i + 1, <j, k>>>
    def encode(self) -> int:
        elpair = encodeWhole(self.trueLabel, self.falseLabel)
        encoded = encodeNatrual(2 * self.register + 1, elpair)

        log(f"Encoding {self}:")
        log(f"    Encoding <{self.trueLabel}, {self.falseLabel}>:")
        log(f"    = {powString(2, self.trueLabel)} {MULT_SYMBOL} (2 {MULT_SYMBOL} {self.falseLabel} + 1) - 1")
        log(f"    = {elpair}")
        log(f"    Encoding <<2 {MULT_SYMBOL} {self.register} + 1, {elpair}>>")
        log(f"    = <<{2 * self.register + 1}, {elpair}>>:")
        log(f"    = {powString(2, 2 * self.register + 1)} {MULT_SYMBOL} (2 {MULT_SYMBOL} {elpair} + 1)")
        log(f"    = {encoded}")
        log(f"= {encoded}")
        return encoded

    def execute(self, state: State) -> None:
        if state.registers[self.register] > 0:
            state.registers[self.register] -= 1
            state.jumpTo(self.trueLabel)
        else:
            state.jumpTo(self.falseLabel)

    def __str__(self) -> str:
        return f"R{getIntSubScript(self.register)}- -> L{getIntSubScript(self.trueLabel)}, L{getIntSubScript(self.falseLabel)}"


class HaltI(Instruction):
    # Encode using 0
    def encode(self) -> int:
        log(f"Encoding {self}:")
        log(f"= 0")
        return 0

    def execute(self, state: State) -> None:
        return state.halt()

    def __str__(self) -> str:
        return f"HALT"
