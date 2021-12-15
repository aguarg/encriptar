from cryptography.fernet import Fernet

# Input para ingresar el mensaje encriptado:
mensaje = input("Ingrese el mensaje encriptado: ")

# Para sacar el b" iniciales y el " del final en el mensaje encriptado:
mensaje = mensaje.encode()[1:-1]
# el método encode() transforma las strings a bytes, necesarios para el módulo Fernet.


# Función que desencripta el mensaje:
def decrypt_message(encrypted_message):
    
    key = input("Ingrese la llave: " )

    f = Fernet(key)
    
    # Desencripta el mensaje usando la llave asignada a f, ingresada por el usuario.
    decrypted_message = f.decrypt(encrypted_message)

    print(decrypted_message.decode())



if __name__ == "__main__":
    decrypt_message(mensaje)