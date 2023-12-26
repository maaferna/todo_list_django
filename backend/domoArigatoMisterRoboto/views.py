from django.http import JsonResponse
from django.views import View

class DecodeMessageView(View):
    def get(self, request, *args, **kwargs):
        encoded_instructions = "DDNNUNUUUUUNNUNUUNNUS"
        encoded_instructions = "UNDDNNUUNNNUNUUUUUNNUNUUUUNNUUNUUUUUNNUUNNNSDDNNUUNNNUNDNNSUNUUUNNUNUUUUNNUNNNUUNUUUNNDDDNNUUUUUUNNDDDNNUUNUUUUUUNNUNNNUNDNNUUUUUUNNS"
        decoded_message = decode_robot_message(encoded_instructions)

        return JsonResponse({"decoded_message": decoded_message})

def decode_robot_message(encoded_instructions):
    memory = [0] * 10
    pointer = 0
    decoded_message = ""
    for instruction in encoded_instructions:
        if instruction == 'U':
            memory[pointer] = (memory[pointer] + 1) % 10
        elif instruction == 'D':
            memory[pointer] = (memory[pointer] - 1) % 10
        elif instruction == 'N':
            pointer = (pointer + 1) % 10
        elif instruction == 'S':
            # Decode and append the current message segment
            decoded_message += decode_memory(memory)
            print(memory)
            # Reset memory after appending
            memory = [0] * 10
    
    return decoded_message.strip()  # Remove any trailing spaces

def decode_memory(memory):
    message = ""
    current_value = 0
    
    for value in memory:
        if value != 0:
            current_value = current_value * 10 + value
        else:
            if current_value > 0:
                # Ensure the generated value is within the range 1-56
                current_value = (current_value - 1) % 56 + 1
                try:
                    letter = chr(ord('A') + current_value - 1)
                    message += letter
                    current_value = 0  # Reset for the next potential combination
                except ValueError:
                    # Handle larger values
                    message += f"{current_value} "
                current_value = 0
    
    # Append the last letter if any
    if current_value > 0:
        # Ensure the generated value is within the range 1-56
        current_value = (current_value - 1) % 56 + 1
        try:
            letter = chr(ord('A') + current_value - 1)
            message += letter
        except ValueError:
            # Handle larger values
            message += f"{current_value} "
    
    return message.strip()

