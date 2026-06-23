def multi_shift_cipher(text, shifts, mode):
    result = ""
    shift_index = 0
    for char in text:
        if char.isalpha():
            shift = shifts[shift_index % len(shifts)]
            if mode == "decrypt":
                shift = -shift
            if char.isupper():
                shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
                result += chr(shifted)
            elif char.islower():
                shifted = (ord(char) - ord('a') + shift) % 26 +ord('a')
                result += chr(shifted)
            shift_index += 1
        else:
            result += char
    return result

print("=== Caesar Cipher - Level 3 (Multi-Shift) ===")
message = input("Enter your message: ")
shifts_input = input("Enter shifts seperated by commas (e.g., 3,-2,5,-4,8): ")
shifts = [int(x) for x in shifts_input.split(",")]
mode = input("Type 'encrypt'or 'decrypt': ")
result = multi_shift_cipher(message, shifts, mode)
print(f"Result: {result}")