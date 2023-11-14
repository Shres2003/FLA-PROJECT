class PalindromeTM:
    def _init_(self):
        self.states = {'q0', 'q1', 'q2', 'q3', 'q4'}
        self.input_symbols = {'0', '1', 'B'}
        self.transitions = {
            'q0': {'0': ('q1', 'B', 'R'), '1': ('q1', 'B', 'R'), 'B': ('q4', 'B', 'S')},
            'q1': {'0': ('q1', '0', 'R'), '1': ('q1', '1', 'R'), 'B': ('q2', 'B', 'L')},
            'q2': {'0': ('q3', 'B', 'L'), '1': ('q3', 'B', 'L'), 'B': ('q4', 'B', 'S')},
            'q3': {'0': ('q3', '0', 'L'), '1': ('q3', '1', 'L'), 'B': ('q0', 'B', 'R')},
            'q4': {},  # Accept state
        }
        self.initial_state = 'q0'
        self.reject_state = 'q4'  # Renamed to reject_state for clarity

    def run(self, input_str):
        tape = list(input_str + 'B')
        head = 0
        state = self.initial_state

        while state != self.reject_state:
            symbol = tape[head]
            if state not in self.transitions or symbol not in self.transitions[state]:
                return f"'{input_str}' is not a palindrome."

            new_state, new_symbol, move = self.transitions[state][symbol]
            tape[head] = new_symbol
            if move == 'L':
                head -= 1
            elif move == 'R':
                head += 1
            state = new_state

        return f"'{input_str}' is a palindrome."


# Example usage with user input:
palindrome_tm = PalindromeTM()
user_input = input("Enter a binary string to check if it's a palindrome: ")
result = palindrome_tm.run(user_input)
print(result)