from cryptography.fernet import Fernet

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    print(decrypted_message.decode())

if __name__ == "__main__":
    decrypt_message(b'gAAAAABhtO2IvAUMf5zgY7V3UTVilkQjkcwJ5iA4Y8KGS9sQbKlLDz8Vv24ium4O08FJPivZeAscYlxCJ5MChr_6lZNu5OAJewulhp1NxDwD7SYgGh05gwTByxv_9T0NMkK6UsCeqtEMSW7SR3dLzmyCVIPqoUvsyjAyXoKgEGVlFMW8jRR9VkCS96zJEVAk4mXi-a2YO6YU')