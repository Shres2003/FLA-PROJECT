class BinaryAdditionFSM:
    def _init_(self):
        self.states = {'q0', 'q1', 'q2'}
        self.input_symbols = {'0', '1'}
        self.transitions = {
            'q0': {'0': ('q0', '0', 'R'), '1': ('q0', '1', 'R'), 'B': ('q1', 'B', 'L')},
            'q1': {'0': ('q1', '0', 'L'), '1': ('q1', '1', 'L'), 'B': ('q2', 'B', 'R')},
            'q2': {'0': ('q2', '0', 'R'), '1': ('q2', '1', 'R'), 'B': ('q2', 'B', 'S')},
        }
        self.initial_state = 'q0'
        self.accept_state = 'q2'

    def run(self, input_str1, input_str2):
        tape = list(input_str1 + 'B' + input_str2 + 'B')
        head = 0
        state = self.initial_state

        while state != self.accept_state:
            symbol = tape[head]
            new_state, new_symbol, move = self.transitions[state][symbol]
            tape[head] = new_symbol
            if move == 'L':
                head -= 1
            elif move == 'R':
                head += 1
            state = new_state

        result = ''.join(tape).strip('B')
        return result


# Example usage:
binary_addition_fsm = BinaryAdditionFSM()
result = binary_addition_fsm.run('1101', '1011')
print(f"Binary Addition Result: {result}")