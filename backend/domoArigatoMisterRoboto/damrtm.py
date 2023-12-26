# domoArigatoMisterRoboto/damrtm.py

class DAMRTM:
    def __init__(self):
        self.memory = [0] * 10
        self.pointer = 0

    def process_instruction(self, instruction):
        if instruction == 'U':
            self.memory[self.pointer] = (self.memory[self.pointer] + 1) % 10
        elif instruction == 'D':
            self.memory[self.pointer] = (self.memory[self.pointer] - 1) % 10
        elif instruction == 'N':
            self.pointer = (self.pointer + 1) % 10
        elif instruction == 'S':
            decoded_message = self.decode_message()
            self.reset_memory()
            return decoded_message

    def decode_message(self):
        message = ""
        for value in self.memory:
            if value != 0:
                # Map values to corresponding alphabet letters (A=1, B=2, ..., Z=26)
                letter = chr(ord('A') + value - 1)
                message += letter
            else:
                # Separation between letters
                message += ''
        return message

    def reset_memory(self):
        self.memory = [0] * 10
        self.pointer = 0
