import random
import hashlib
def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()
def generate_shifts(user_shifts, total_length):
    auto_shifts = [random.randint(-25,25)for _ in range(total_length - len(user_shifts))]
    return user_shifts + auto_shifts
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
                shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
                result += chr(shifted)
            shift_index += 1
        else:
            result += char
    return result

print("=== Secure Multi-Shift Cipher (Level 3B) ===")
print("1. Encrypt a message")
print("2. Decrypt a message")
choice = input("\nEnter choice (1 or 2): ")

if choice == "1":
    message = input("Enter your message: ")
    shifts_input = input("Enter 5 shifts separated by commas (e.g., 3,-2,5,-4,8): ")
    user_shifts = [int(x) for x in shifts_input.split(",")]
    full_shifts = generate_shifts(user_shifts, len(message))
    pin = input("Set a PIN (4, 6, or 8 digits): ")
    hashed_pin = hash_pin(pin)
    encrypted = multi_shift_cipher(message, full_shifts, "encrypt")
    print(f"\nEncrypted message: {encrypted}")
    print(f"Full shift key: {full_shifts}")
    print(f"Hashed PIN: {hashed_pin}")
    print(" Share the encrypted message and shift key with receiver secretly!")
    print(" Share the PIN separately through a different channel!")
    
elif choice == "2":
    encrypted = input("Enter encrypted message: ")
    shifts_input = input("Enter full shift key (comma separated): ")
    full_shifts = [int(x) for x in shifts_input.split(",")]
    hashed_pin = input("Enter hashed PIN: ")
    pin_attempt = input("Enter PIN to decrypt: ")
    if hash_pin(pin_attempt) == hashed_pin:
        decrypted = multi_shift_cipher(encrypted, full_shifts, "decrypt")
        print(f"\nAccess granted!")
        print(f"Decrypted message: {decrypted}")
    else:
        print("Wrong PIN! Access denied!")
else:
    print("Invalid choice! Please enter 1 or 2.")