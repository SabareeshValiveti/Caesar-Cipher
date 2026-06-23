def caesar_cipher(text, shift, mode):
    if mode == "decrypt":
        shift = -shift
    result = ""
    for char in text:
        if char.isupper():
            shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
            result += chr(shifted)
        elif char.islower ():
            shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
            result += chr(shifted)
        else:
            result += char
    return result

print("=== Caesar Cipher - Level 2 (Encrypt/Decrypt) ===")
message = input("Enter your message: ")
shift = int(input("Enter shift number (e.g., 3): "))
mode = input("Type 'encrypt' or 'decrypt': ")

result = caesar_cipher(message, shift, mode)
print(f"Result: {result}")