from cryptography.fernet import Fernet


mensaje = input("Ingrese el mensaje encriptado: ")


def decrypt_message(encrypted_message):
    
    key = input("Ingrese la llave: " )

    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    print(decrypted_message.decode())



if __name__ == "__main__":
    decrypt_message(mensaje)