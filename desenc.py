from cryptography.fernet import Fernet


# Cargar la llave:
def load_key():
    
    return open("secret.key", "rb").read()


# Desencripta el mensaje:
def decrypt_message(encrypted_message):
    
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    print(decrypted_message.decode())

if __name__ == "__main__":
    decrypt_message(b'gAAAAABhtO2IvAUMf5zgY7V3UTVilkQjkcwJ5iA4Y8KGS9sQbKlLDz8Vv24ium4O08FJPivZeAscYlxCJ5MChr_6lZNu5OAJewulhp1NxDwD7SYgGh05gwTByxv_9T0NMkK6UsCeqtEMSW7SR3dLzmyCVIPqoUvsyjAyXoKgEGVlFMW8jRR9VkCS96zJEVAk4mXi-a2YO6YU')