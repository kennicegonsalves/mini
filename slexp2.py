def generate_key_table(key):
    """
    Generates a 5x5 key table based on the given key.
    - Replaces 'J' with 'I'
    - Includes letters from the key and fills the rest with remaining letters of the alphabet
    """
    key = key.upper().replace('J', 'I')  # Convert key to uppercase and replace 'J' with 'I'
    key_table = []
    used = set()
    # Add characters from the key to the key table
    for char in key:
        if char not in used and char.isalpha():
            used.add(char)
            key_table.append(char)
    # Add remaining characters from the alphabet to the key table
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' is excluded
    for char in alphabet:
        if char not in used:
            key_table.append(char)
    # Return the key table as a list of lists (5x5 matrix)
    return [key_table[i*5:(i+1)*5] for i in range(5)]
def find_position(table, char):
    """
    Finds the position (row, column) of a character in the key table.
    """
    for i, row in enumerate(table):
        for j, val in enumerate(row):
            if val == char:
                return i, j
    return None
def prepare_text(text):
    """
    Prepares the text for encryption or decryption:
    - Converts to uppercase
    - Replaces 'J' with 'I'
    - Removes non-alphabetic characters
    - Pads double letters with 'X' and ensures even length by padding last character if needed
    """
    text = ''.join([char for char in text.upper() if char.isalpha()]).replace('J', 'I')
    prepared = []
    i = 0
    while i < len(text):
        if i == len(text) - 1:
            prepared.append(text[i] + 'X')  # Pad last character with 'X' if needed
            i += 1
        elif text[i] == text[i + 1]:
            prepared.append(text[i] + 'X')  # Pad double letters with 'X'
            i += 1
        else:
            prepared.append(text[i] + text[i + 1])
            i += 2
    return prepared
def encrypt_pair(pair, table):
    """
    Encrypts a pair of characters using the Playfair cipher rules:
    - If both characters are in the same row, replace them with characters to their right.
    - If both characters are in the same column, replace them with characters below.
    - Otherwise, form a rectangle and replace characters with those on the opposite corners.
    """
    row1, col1 = find_position(table, pair[0])
    row2, col2 = find_position(table, pair[1])
    if row1 == row2:
        return table[row1][(col1 + 1) % 5] + table[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return table[(row1 + 1) % 5][col1] + table[(row2 + 1) % 5][col2]
    else:
        return table[row1][col2] + table[row2][col1]
def decrypt_pair(pair, table):
    """
    Decrypts a pair of characters using the Playfair cipher rules:
    - If both characters are in the same row, replace them with characters to their left.
    - If both characters are in the same column, replace them with characters above.
    - Otherwise, form a rectangle and replace characters with those on the opposite corners.
    """
    row1, col1 = find_position(table, pair[0])
    row2, col2 = find_position(table, pair[1])
    if row1 == row2:
        return table[row1][(col1 - 1) % 5] + table[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return table[(row1 - 1) % 5][col1] + table[(row2 - 1) % 5][col2]
    else:
        return table[row1][col2] + table[row2][col1]
def playfair_encrypt(plaintext, table):
    """
    Encrypts the given plaintext using the provided key table.
    """
    plaintext_pairs = prepare_text(plaintext)
    ciphertext = ''
    for pair in plaintext_pairs:
        ciphertext += encrypt_pair(pair, table)
    return ciphertext
def playfair_decrypt(ciphertext, table):
    """
    Decrypts the given ciphertext using the provided key table.
    """
    ciphertext_pairs = prepare_text(ciphertext)
    plaintext = ''
    for pair in ciphertext_pairs:
        plaintext += decrypt_pair(pair, table)
    return plaintext
def display_key_table(table):
    #Displays the key table in a readable 5x5 matrix format.
    for row in table:
        print(' '.join(row))
def main():
    """
    Main function to run the Playfair Cipher program.
    - Provides options to generate key table, encrypt, decrypt, and exit.
    - Repeats until the user chooses to exit."""
    key_table = None
    while True:
        print("\nPlayfair Cipher")
        choice = input("Choose an option:\n1. Generate Key Table\n2. Encrypt\n3. Decrypt\n4. Exit\nChoice: ")
        if choice == '1':
            key = input("Enter the key: ")
            key_table = generate_key_table(key)
            print("Generated Key Table:")
            display_key_table(key_table)
        elif choice == '2':
            if key_table is None:
                print("Please generate a key table first.")
            else:
                plaintext = input("Enter the plaintext: ")
                ciphertext = playfair_encrypt(plaintext, key_table)
                print("Ciphertext: ", ciphertext)
        elif choice == '3':
            if key_table is None:
                print("Please generate a key table first.")
            else:
                ciphertext = input("Enter the ciphertext: ")
                decrypted_text = playfair_decrypt(ciphertext, key_table)
                print("Decrypted Text: ", decrypted_text)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
if __name__ == "__main__":
    main()
