# Caesar Cipher - Multi-Level Encryption Tool 

A Python-based cryptography project implementing the Caesar Cipher encryption technique across 5 levels of increasing difficulty. Built as part of a cybersecurity portfolio to demonstrate understanding of encryption, decryption, and cryptanalysis concepts.

##  Project Overview

The Caesar Cipher is one of the oldest and most well-known encryption techniques, named after Julius Caesar who used it to protect military messages. This project builds on that foundation progressively, from basic encryption to advanced cryptanalysis.

##  Project Structure
caesar-cipher/

├── level1_caesar.py          # Basic encryption only

├── level2_encrypt_decrypt.py # Encrypt + Decrypt modes

├── level3_multi_shift.py     # Custom shift per letter

├── level4_vigenere.py        # Keyword-based cipher

├── level5_brute_force.py     # Cipher cracker

└── README.md
## 🎯 Levels Explained

### Level 1 — Classic Caesar Cipher (Beginner)
- Encrypts a message using a single fixed shift value
- Handles uppercase, lowercase, and special characters
- **Example:** `HELLO` with shift 3 → `KHOOR`

### Level 2 — Encrypt & Decrypt (Easy-Intermediate)
- Adds decryption mode to Level 1
- User chooses to encrypt or decrypt
- Uses negative shift for decryption
- **Example:** `KHOOR` with shift 3, decrypt → `HELLO`

### Level 3 — Multi-Shift Cipher (Intermediate)
- Each letter gets its own unique shift value
- Shift list cycles if message is longer than shift list
- Much harder to crack than classic Caesar
- **Example:** `HELLO` with shifts `[3, -2, 5, -4, 8]` → unique encrypted output

### Level 4 — Vigenère Keyword Cipher (Advanced)
- Uses a keyword instead of numbers for shifting
- Each letter of keyword determines shift (A=0, B=1...Z=25)
- Industry-standard upgrade to Caesar Cipher
- **Example:** `HELLO` with keyword `KEY` → encrypted output

### Level 5 — Brute Force Cipher Cracker (Expert)
- Takes an encrypted message and tries all 26 possible shifts
- Displays all possible decryptions for the user to identify the correct one
- Demonstrates real cryptanalysis techniques used in cybersecurity
- **Example:** Given `KHOOR`, tries shifts 0-25 and shows `HELLO` at shift 3

## 🚀 How to Run

Make sure Python is installed:
```bash
python --version
```

Run any level:
```bash
python level1_caesar.py
python level2_encrypt_decrypt.py
python level3_multi_shift.py
python level4_vigenere.py
python level5_brute_force.py
```

## 💡 Concepts Learned

- **ASCII values** — `ord()` and `chr()` functions
- **Modulo operator** (`%`) for alphabet wrap-around
- **String manipulation** and loops
- **Negative shifts** for decryption
- **List indexing** and cycling
- **Cryptanalysis** — brute force attack techniques
- **Vigenère Cipher** — keyword-based encryption

## 🔧 Requirements

- Python 3.x
- No external libraries required

## 📊 Encryption Strength Comparison

| Level | Type | Difficulty to Crack |
|-------|------|-------------------|
| 1 | Classic Caesar | Very Easy (26 possibilities) |
| 2 | Caesar + Decrypt | Very Easy |
| 3 | Multi-Shift | Medium |
| 4 | Vigenère Keyword | Hard |
| 5 | Brute Force Cracker | Tool for cracking Level 1 |

## 🛡️ Cybersecurity Relevance

Understanding cipher mechanics is fundamental to cybersecurity:
- Modern encryption (AES, RSA) builds on these same mathematical principles
- Brute force attacks (Level 5) are a real attack vector in cybersecurity
- Vigenère cipher demonstrates the importance of key complexity

## 👤 Author

**Sabareesh Valiveti**
- MS Cybersecurity @ Indiana Institute of Technology
- MTech VLSI Design @ IIIT Sri City
- GitHub: [SabareeshValiveti](https://github.com/SabareeshValiveti)
- LinkedIn: [sabareesh-valiveti](https://linkedin.com/in/sabareesh-valiveti)