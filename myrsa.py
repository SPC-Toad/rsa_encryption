from math import gcd
import math
import random

# Generates array of prime numbers between lo value to hi value
def prime_gen(lo, hi):
    prime = []
    for p in range(lo, hi):
        if (p < 2 or p % 2 == 0):
            continue
        j = 2
        while j <= p / j:
            if p % j == 0:
                break
            j += 1
        if j > p / j:
            prime.append(p)
    return prime

def get_n(p, q):
    return p * q

# Compute φ(n)
def phi(p, q):
    return (p - 1) * (q - 1)

def public_key_gen(phi_n, prime_arr):
    for e in prime_arr:
        if (1 < e < phi_n) and gcd(e, phi_n) == 1:
            return e

def private_key_gen(phi_n, e):
    for i in range(1, phi_n):
        if (e * i) % phi_n == 1:
            return i

def encrypt_chunk(chunk, e, n):
    message_int = int.from_bytes(chunk.encode(), byteorder='big')
    return pow(message_int, e, n)

def decrypt_chunk(ciphertext, d, n):
    decrypted = pow(ciphertext, d, n)
    return decrypted.to_bytes((math.ceil(decrypted.bit_length() / 8)), 'big').decode()

# Encrypts each chunk in message into byte to int
def encrypt_message(message, e, n):
    chunk_size = (n.bit_length() - 1) // 8
    chunks = [message[i:i + chunk_size] for i in range(0, len(message), chunk_size)]
    encrypted_chunks = [encrypt_chunk(chunk, e, n) for chunk in chunks]
    return encrypted_chunks

# Decrypts encryped message
def decrypt_message(encrypted_message_arr, d, n):
    decrypted_chunks = [decrypt_chunk(chunk, d, n) for chunk in encrypted_message_arr]
    return ''.join(decrypted_chunks)

print("What is your message?:")
message = input()
print("What is the lowest prime number? (higher the number it is more secure it is):")
low = int(input())
print("What is the highest prime number? (higher the number it is more secure it is):")
high = int(input())

# Generate prime number array
prime_arr = prime_gen(low, high)

# Get p and q prime numbers
p = random.choice(prime_arr)
q = random.choice([x for x in prime_arr if x != p])

# Compute n and φ(n)
n = get_n(p, q)
phi_n = phi(p, q)

# Generate public and private keys
e = public_key_gen(phi_n, prime_arr)
d = private_key_gen(phi_n, e)

print(f"Your message before encryption: {message}")

ciphertext = encrypt_message(message, e, n)
print(f"Your message after encryption: {ciphertext}")

decrypted_message = decrypt_message(ciphertext, d, n)
print(f"Your message after decryption: {decrypted_message}")
