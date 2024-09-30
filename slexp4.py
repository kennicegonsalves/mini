import math

# Function to calculate gcd
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to calculate the multiplicative inverse using Extended Euclidean Algorithm
def multiplicative_inverse(e, phi):
    phi_original = phi
    x0, x1 = 0, 1
    while e > 1:
        quotient = e // phi
        e, phi = phi, e % phi
        x0, x1 = x1 - quotient * x0, x0
    if x1 < 0:
        x1 += phi_original
    return x1

# Function to factorize n and find p and q
def factorize_n(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i, n // i
    raise ValueError("Unable to factorize n")

# Function to calculate phi and private key
def calculate_private_key(e, n):
    p, q = factorize_n(n)
    phi = (p - 1) * (q - 1)
    # Ensure e is coprime with phi
    if gcd(e, phi) != 1:
        raise ValueError("e must be coprime with φ(n)")
    # Calculate the private key d
    d = multiplicative_inverse(e, phi)
    # Return private key, p, q, phi
    return (d, n), p, q, phi

# Function to encrypt the message
def encrypt(public_key, message):
    e, n = public_key
    ciphertext = pow(message, e, n)
    return ciphertext

# Function to decrypt the message
def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = pow(ciphertext, d, n)
    return plaintext

def main():
    # Party A
    print("Party A Key Generation")
    e_a = int(input("Enter public key element e for A: "))
    n_a = int(input("Enter modulus n for A: "))
    public_key_a = (e_a, n_a)
    private_key_a, p_a, q_a, phi_a = calculate_private_key(e_a, n_a)
    print(f"A's Public Key (e, n): {public_key_a}")
    print(f"A's Private Key (d, n): {private_key_a}")
    print(f"A's Prime Numbers: p = {p_a}, q = {q_a}")
    print(f"A's ϕ(n): {phi_a}\n")

    # Party B
    print("Party B Key Generation")
    e_b = int(input("Enter public key element e for B: "))
    n_b = int(input("Enter modulus n for B: "))
    public_key_b = (e_b, n_b)
    private_key_b, p_b, q_b, phi_b = calculate_private_key(e_b, n_b)
    print(f"B's Public Key (e, n): {public_key_b}")
    print(f"B's Private Key (d, n): {private_key_b}")
    print(f"B's Prime Numbers: p = {p_b}, q = {q_b}")
    print(f"B's ϕ(n): {phi_b}\n")

    # A sends M to B
    M_a = int(input("Enter message M to send from A to B: "))
    ciphertext_from_a_to_b = encrypt(public_key_b, M_a)
    print(f"Ciphertext sent by A to B: {ciphertext_from_a_to_b}")
    decrypted_message_by_b = decrypt(private_key_b, ciphertext_from_a_to_b)
    print(f"Message decrypted by B: {decrypted_message_by_b}\n")

    # B sends M to A
    M_b = int(input("Enter message M to send from B to A: "))
    ciphertext_from_b_to_a = encrypt(public_key_a, M_b)
    print(f"Ciphertext sent by B to A: {ciphertext_from_b_to_a}")
    decrypted_message_by_a = decrypt(private_key_a, ciphertext_from_b_to_a)
    print(f"Message decrypted by A: {decrypted_message_by_a}\n")

if __name__ == "__main__":
    main()
