class TuringMachine:
    def __init__(self, transitions, initial_state, accept_state, reject_state):
        self.transitions = transitions
        self.state = initial_state
        self.accept_state = accept_state
        self.reject_state = reject_state
        self.tape = ['B']  # Initialize the tape with a blank symbol

    def step(self):
        current_symbol = self.tape[0]
        if (self.state, current_symbol) in self.transitions:
            new_state, write_symbol, move_direction = self.transitions[(self.state, current_symbol)]

            # Update tape
            self.tape[0] = write_symbol

            # Move tape head
            if move_direction == 'R':
                self.tape.insert(0, 'B')  # Move right by adding a blank symbol on the left
            elif move_direction == 'L':
                if len(self.tape) > 1:
                    self.tape.pop(0)  # Move left by removing the leftmost symbol
                else:
                    self.tape[0] = 'B'  # Move left from the leftmost position by replacing the symbol with blank

            # Update state
            self.state = new_state
        else:
            self.state = self.reject_state

    def run(self, input_str):
        # Initialize tape with input string
        self.tape += list(input_str)

        # Run the machine until it reaches an accepting or rejecting state
        while self.state not in [self.accept_state, self.reject_state]:
            self.step()

        # Check the final state
        return self.state == self.accept_state


# Define the Turing machine transitions
transitions = {
    ('q0', '0'): ('q0', '0', 'R'),
    ('q0', '1'): ('q0', '1', 'R'),
    ('q0', 'B'): ('q1', 'B', 'L'),
    ('q1', '0'): ('q2', 'B', 'L'),  # Move to the second-to-last symbol
    ('q1', '1'): ('q2', 'B', 'L'),  # Move to the second-to-last symbol
    ('q1', 'B'): ('q_accept', 'B', '-'),  # Accept if the entire string has been processed and is a palindrome
    ('q2', '0'): ('q2', '0', 'L'),  # Move left until a blank symbol is found
    ('q2', '1'): ('q2', '1', 'L'),  # Move left until a blank symbol is found
    ('q2', 'B'): ('q3', 'B', 'R'),  # Move to the rightmost symbol
    ('q3', '0'): ('q_reject', '0', '-'),  # Reject if symbols at ends do not match
    ('q3', '1'): ('q_reject', '1', '-'),  # Reject if symbols at ends do not match
    ('q3', 'B'): ('q_reject', 'B', '-'),  # Reject if symbols at ends do not match
}

# Create a Turing machine
tm = TuringMachine(transitions, 'q0', 'q_accept', 'q_reject')

# Test the Turing machine with an input string
input_str = "101"
result = tm.run(input_str)

# Display the result
if result:
    print(f"The input '{input_str}' is a palindrome.")
else:
    print(f"The input '{input_str}' is not a palindrome.")