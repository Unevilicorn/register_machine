class State:
    def __init__(self,  PCValue: int, registers: list[int]) -> None:
        self.PC = PCValue
        self.registers = registers
        self.halted = False

    def jumpTo(self, newPC: int) -> None:
        self.PC = newPC

    def halt(self) -> None:
        self.halted = True
