class CPU:
    ops_cycles = {
        'noop': 1,
        'addx': 2,
        'stop': 1,
    }

    def __init__(self, memory, pc=0):
        self.memory = memory
        self.pc = pc
        self.X = 1
        self.instruction = None
        self.op = None
        self.args = None
        self.required_cycles = 0
        self.elapsed_cycles = 0

    def cycle(self):
        if self.required_cycles == 0:
            self.fetch_instruction()
            self.decode_instruction()

        if self.elapsed_cycles == self.required_cycles:
            self.execute_instruction()
            self.fetch_instruction()
            self.decode_instruction()

        self.elapsed_cycles += 1

    def fetch_instruction(self):
        self.instruction = self.memory[self.pc]

    def decode_instruction(self):
        op, *args = self.instruction.split(' ')
        required_cycles = CPU.ops_cycles[op]

        self.elapsed_cycles = 0
        self.required_cycles = required_cycles
        self.op = op
        self.args = args

    def execute_instruction(self):
        if self.op == 'addx':
            self.X += int(self.args[0])
            self.pc += 1
        elif self.op == 'noop':
            self.pc += 1
        elif self.op == 'stop':
            self.pc += 0


class CRT:
    def __init__(self):
        self.screen = [['.']*40 for _ in range(6)]
        self.vertical_pos = 0
        self.horizontal_pos = 0

    def connect(self, cpu: CPU):
        self.cpu = cpu

    def cycle(self):
        is_drawing_sprite = self.horizontal_pos <= self.cpu.X + \
            1 and self.horizontal_pos >= self.cpu.X - 1
        if is_drawing_sprite:
            self.screen[self.vertical_pos][self.horizontal_pos] = '#'
        else:
            self.screen[self.vertical_pos][self.horizontal_pos] = '.'

        self.vertical_pos += (self.horizontal_pos + 1) // 40
        self.vertical_pos %= 6
        self.horizontal_pos = (self.horizontal_pos + 1) % 40

    def show_screen(self):
        for row in self.screen:
            for pixel in row:
                print(pixel, end='')
            print()


def load_memory(filepath):
    with open(filepath) as file:
        file_content = file.read().strip()
        return file_content.split('\n')


memory = load_memory('./10/input.txt')
memory.append('stop')
cpu = CPU(memory)
crt = CRT()
crt.connect(cpu)

for cycle in range(1, 240):
    cpu.cycle()
    crt.cycle()

crt.show_screen()
