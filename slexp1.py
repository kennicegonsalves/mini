# Shift Cipher Encryption and Decryption Program with User Input

# Function to encrypt the plaintext using a given shift
def encrypt(plaintext, shift):
    encrypted_text = ""
    # Traverse through each character in the plaintext
    for char in plaintext:
        # Encrypt uppercase characters
        if char.isupper():
            # Compute the encrypted character and append to the result
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            # Compute the encrypted character and append to the result
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Append the character as is (non-alphabetic characters)
            encrypted_text += char
    return encrypted_text

# Function to decrypt the ciphertext using a given shift
def decrypt(ciphertext, shift):
    decrypted_text = ""
    # Traverse through each character in the ciphertext
    for char in ciphertext:
        # Decrypt uppercase characters
        if char.isupper():
            # Compute the decrypted character and append to the result
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            # Compute the decrypted character and append to the result
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # Append the character as is (non-alphabetic characters)
            decrypted_text += char
    return decrypted_text

# Function to break the cipher by trying all possible shifts
def break_cipher(ciphertext):
    possible_decryptions = []
    for shift in range(26):
        decrypted_text = decrypt(ciphertext, shift)
        possible_decryptions.append(decrypted_text)
        print(f"Shift {shift}: {decrypted_text}")
    return possible_decryptions

# Function to display the menu and get the user's choice
def display_menu():
    print("")
    print("Shift Cipher Program")
    print("1. Encrypt Plaintext")
    print("2. Decrypt Ciphertext")
    print("3. Brute Force Attack")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    return choice

# Main function to demonstrate encryption and decryption with user input
def main():
    while True:
        choice = display_menu()
        
        if choice == '1':
            # Encrypt Plaintext
            plaintext = input("Enter the plaintext: ")
            shift = 3  # Fixed shift value for encryption
            encrypted_text = encrypt(plaintext, shift)
            print(f"Encrypted Text: {encrypted_text}")
        
        elif choice == '2':
            # Decrypt Ciphertext
            ciphertext = input("Enter the ciphertext: ")
            shift = int(input("Enter the shift value (0-25): "))
            decrypted_text = decrypt(ciphertext, shift)
            print(f"Decrypted Text: {decrypted_text}")
        
        elif choice == '3':
            # Break Cipher
            ciphertext = input("Enter the ciphertext to break: ")
            print("")
            pd = break_cipher(ciphertext)
            print("")
            cs= int(input("Enter the shift value that gives the correct decryption: "))
            print(f"The correct decryption using shift {cs} is: {pd[cs]}")
        
        elif choice == '4':
            # Exit
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()

