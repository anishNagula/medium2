import string

# --- Challenge Setup ---
# The final password the participant must find to submit to the login_portal.html
PLAINTEXT_PASSWORD = "KHUL JA SIM SIM"

# The Vigenere key provided as a hint on the web page (The key is the ECHO)
KEY = "ECHO"

# --- Vigenere Encryption Function ---

def vigenere_encrypt(plaintext, key):
    """Encrypts the plaintext using the Vigenere cipher."""
    plaintext = plaintext.replace(" ", "").upper()
    key = key.upper()
    
    # Repeat the key to match the length of the plaintext
    key_repeated = (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]
    
    ciphertext = []
    
    for i, char in enumerate(plaintext):
        # A=0, B=1, ..., Z=25
        plain_index = string.ascii_uppercase.index(char)
        key_index = string.ascii_uppercase.index(key_repeated[i])
        
        # Cipher Formula: C = (P + K) mod 26
        cipher_index = (plain_index + key_index) % 26
        cipher_char = string.ascii_uppercase[cipher_index]
        ciphertext.append(cipher_char)
        
    # Re-insert spaces for readability (e.g., QIPSRU YM XGZIR)
    # This is often skipped in CTFs, but makes it look more like the original target text.
    final_ciphertext = ""
    plain_index_counter = 0
    for original_char in PLAINTEXT_PASSWORD:
        if original_char == ' ':
            final_ciphertext += ' '
        else:
            final_ciphertext += ciphertext[plain_index_counter]
            plain_index_counter += 1

    return final_ciphertext

# --- Execution ---
encrypted_text = vigenere_encrypt(PLAINTEXT_PASSWORD, KEY)

print("--- The Forgotten Terminal Challenge Components ---")
print(f"Original Password (Plaintext): {PLAINTEXT_PASSWORD}")
print(f"Vigenere Key (Hint from Web Page): {KEY}")
print(f"Encrypted Text (Place on Terminal Image): {encrypted_text}")
