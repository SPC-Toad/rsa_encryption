# RSA Encryption and Decryption

This project demonstrates the implementation of RSA encryption and decryption in Python. It includes generating prime numbers, creating public and private keys, and handling message chunking for encryption and decryption.

## Features

- Generate an array of prime numbers within a specified range.
- Select two random prime numbers to compute \( n \) and \( \phi(n) \).
- Generate public and private keys.
- Encrypt and decrypt messages using RSA, with support for chunking to handle larger messages.

## Usage

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/rsa_encryption.git
   cd rsa_encryption
   ```

2. **Run the script**:
   ```bash
   python myrsa.py
   ```

3. **Follow the prompts**:
   - Enter your message.
   - Specify the lowest and highest prime numbers to define the range for prime number generation.

## Example

### Input

```plaintext
What is your message?:
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
What is the lowest prime number? (higher the number it is more secure it is):
2
What is the highest prime number? (higher the number it is more secure it is):
600
```

### Output

```plaintext
Your message before encryption: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

Your message after encryption: [1179, 841, 779, 3306, 232, 2263, 1388, 1637, 2815, 1170, 232, 2263, 1277, 2815, 2263, 2815, 1277, 232, 1637, 2275, 1374, 2263, 3119, 1170, 232, 232, 1374, 2263, 3366, 3306, 1753, 3366, 2263, 841, 924, 2263, 3366, 277, 3306, 2263, 1637, 779, 1277, 1131, 3366, 1277, 1131, 2663, 2263, 2811, 1131, 3119, 2263, 3366, 1374, 1637, 3306, 2815, 3306, 3366, 3366, 1277, 1131, 2663, 2263, 1277, 1131, 3119, 1170, 2815, 3366, 779, 1374, 2866, 2263, 1179, 841, 779, 3306, 232, 2263, 1388, 1637, 2815, 1170, 232, 2263, 277, 2811, 2815, 2263, 1582, 3306, 3306, 1131, 2263, 3366, 277, 3306, 2263, 1277, 1131, 3119, 1170, 2815, 3366, 779, 1374, 3276, 2815, 2263, 2815, 3366, 2811, 1131, 3119, 2811, 779, 3119, 2263, 3119, 1170, 232, 232, 1374, 2263, 3366, 3306, 1753, 3366, 2263, 3306, 2091, 3306, 779, 2263, 2815, 1277, 1131, 2396, 3306, 2263, 3366, 277, 3306, 2263, 1111, 1014, 1792, 1792, 2815, 2065, 2263, 2254, 277, 3306, 1131, 2263, 2811, 1131, 2263, 1170, 1131, 692, 1131, 841, 2254, 1131, 2263, 1637, 779, 1277, 1131, 3366, 3306, 779, 2263, 3366, 841, 841, 692, 2263, 2811, 2263, 2663, 2811, 2275, 2275, 3306, 1374, 2263, 841, 924, 2263, 3366, 1374, 1637, 3306, 2263, 2811, 1131, 3119, 2263, 2815, 2396, 779, 2811, 232, 1582, 2275, 3306, 3119, 2263, 1277, 3366, 2263, 3366, 841, 2263, 232, 2811, 692, 3306, 2263, 2811, 2263, 3366, 1374, 1637, 3306, 2263, 2815, 1637, 3306, 2396, 1277, 232, 3306, 1131, 2263, 1582, 841, 841, 692, 2866, 2263, 1388, 3366, 2263, 277, 2811, 2815, 2263, 2815, 1170, 779, 2091, 1277, 2091, 3306, 3119, 2263, 1131, 841, 3366, 2263, 841, 1131, 2275, 1374, 2263, 924, 1277, 2091, 3306, 2263, 2396, 3306, 1131, 3366, 1170, 779, 1277, 3306, 2815, 2065, 2263, 1582, 1170, 3366, 2263, 2811, 2275, 2815, 841, 2263, 3366, 277, 3306, 2263, 2275, 3306, 2811, 1637, 2263, 1277, 1131, 3366, 841, 2263, 3306, 2275, 3306, 2396, 3366, 779, 841, 1131, 1277, 2396, 2263, 3366, 1374, 1637, 3306, 2815, 3306, 3366, 3366, 1277, 1131, 2663, 2065, 2263, 779, 3306, 232, 2811, 1277, 1131, 1277, 1131, 2663, 2263, 3306, 2815, 2815, 3306, 1131, 3366, 1277, 2811, 2275, 2275, 1374, 2263, 1170, 1131, 2396, 277, 2811, 1131, 2663, 3306, 3119, 2866, 2263, 1388, 3366, 2263, 2254, 2811, 2815, 2263, 1637, 841, 1637, 1170, 2275, 2811, 779, 1277, 2815, 3306, 3119, 2263, 1277, 1131, 2263, 3366, 277, 3306, 2263, 1111, 1829, 2725, 1792, 2815, 2263, 2254, 1277, 3366, 277, 2263, 3366, 277, 3306, 2263, 779, 3306, 2275, 3306, 2811, 2815, 3306, 2263, 841, 924, 2263, 1179, 3306, 3366, 779, 2811, 2815, 3306, 3366, 2263, 2815, 277, 3306, 3306, 3366, 2815, 2263, 2396, 841, 1131, 3366, 2811, 1277, 1131, 1277, 1131, 2663, 2263, 1179, 841, 779, 3306, 232, 2263, 1388, 1637, 2815, 1170, 232, 2263, 1637, 2811, 2815, 2815, 2811, 2663, 3306, 2815, 2065, 2263, 2811, 1131, 3119, 2263, 232, 841, 779, 3306, 2263, 779, 3306, 2396, 3306, 1131, 3366, 2275, 1374, 2263, 2254, 1277, 3366, 277, 2263, 3119, 3306, 2815, 692, 3366, 841, 1637, 2263, 1637, 1170, 1582, 2275, 1277, 2815, 277, 1277, 1131, 2663, 2263, 2815, 841, 924, 3366, 2254, 2811, 779, 3306, 2263, 2275, 1277, 692, 3306, 2263, 1114, 2275, 3119, 1170, 2815, 2263, 2845, 2811, 2663, 3306, 205, 2811, 692, 3306, 779, 2263, 1277, 1131, 2396, 2275, 1170, 3119, 1277, 1131, 2663, 2263, 2091, 3306, 779, 2815, 1277, 841, 1131, 2815, 2263, 841, 924, 2263, 1179, 841, 779, 3306, 232, 2263, 1388, 1637, 2815, 1170, 232, 2866]

Your message after decryption: Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
```

## Functions

- `prime_gen(lo, hi)`: Generates an array of prime numbers between `lo` and `hi`.
- `get_n(p, q)`: Computes \( n \) as the product of `p` and `q`.
- `phi(p, q)`: Computes \( \phi(n) \) as \((p-1) \times (q-1)\).
- `public_key_gen(phi_n, prime_arr)`: Generates the public key `e`.
- `private_key_gen(phi_n, e)`: Generates the private key `d`.
- `encrypt_chunk(chunk, e, n)`: Encrypts a single chunk of the message.
- `decrypt_chunk(ciphertext, d, n)`: Decrypts a single chunk of the ciphertext.
- `encrypt_message(message, e, n)`: Encrypts the entire message by splitting it into chunks.
- `decrypt_message(encrypted_chunks, d, n)`: Decrypts the entire message by decrypting each chunk and reassembling them.

## Notes

- Ensure the range for prime number generation is appropriately large to enhance security.
- The chunk size is determined based on the bit length of \( n \).

## Acknowledgments

Inspired by the need for understanding RSA encryption and decryption in Python.