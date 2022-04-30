from instruction import Instruction
from state import State
from utils import log


class Program:
    def __init__(self, state: State, instructions: list[Instruction]) -> None:
        self.state = state
        self.instructions = instructions
        self.firstRun = True

    # Returns true if it halts
    def executeOnce(self) -> bool:
        if not self.state.halted:
            self.instructions[self.state.PC].execute(self.state)

            if self.state.PC >= len(self.instructions):
                self.halt()

        return self.state.halted

    # execute n times or halts, 0 for a lot of times(1 million times)
    # Return true if it halts
    def execute(self, n: int) -> bool:
        limit = 10 ** 6
        if n > 0:
            limit = n

        # Make header
        # Cycle number, PC, Halted, registers
        log(f"""|{'i':^5}|{'PC':^6}|{'H':^3}|{'|'.join(f'{x:^7}' for x in range(len(self.state.registers)))}|""")
        log(f"""|{'-'*5}+{'-'*6}+{'-'*3}+{'+'.join(f'{"-"*7}' for _ in range(len(self.state.registers)))}|""")
        log(f"""|{'Pre':^5}|{self.state.PC:^6}|{'T' if self.state.halted else'F':^3}|{'|'.join(f'{x:^7}' for x in self.state.registers)}|""")

        for i in range(0, limit):
            halted = self.executeOnce()
            log(f"""|{i:^5}|{self.state.PC:^6}|{'T' if self.state.halted else'F':^3}|{'|'.join(f'{x:^7}' for x in self.state.registers)}|""")
            if halted:
                break

        return self.state.halted

    # def __str__(self) -> str:
    #     return f"{'H' if self.halted else self.PC} {' '.join(str(x) for x in self.registers)}"

    def halt(self) -> None:
        self.state.halt()
