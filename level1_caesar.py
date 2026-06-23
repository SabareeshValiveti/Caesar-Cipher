def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            shifted = (ord(char) - ord('A') + shift) % 26 + ord ('A')
            result += chr(shifted)
        elif char.islower():
            shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
            result += chr(shifted)
        else:
            result += char
    return result

print("=== Caesar Cipher - Level 1 ===")
message = input ("Enter your message: ")
shift = int(input("Enter shift number (e.g., 3): "))

encrypted = caesar_encrypt(message, shift)
print(f"Encrypted message: {encrypted}") 