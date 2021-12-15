from cryptography.fernet import Fernet


# Genera la llave y la guarda en un archivo:
def generate_key(): 
    
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file: 
        key_file.write(key)


# Carga la llave generada por la función generate_key():
def load_key():
    
    return open("secret.key", "rb").read()


# Encripta el mensaje:
def encrypt_message(message):
    
    # Asigna la llave que generó generate_key() a la variable key:
    key = load_key()
    
    # Codifica el mensaje y lo encripta: 
    encoded_message = message.encode()
    f = Fernet(key)
    
    global encrypted_message
    encrypted_message = f.encrypt(encoded_message)

   




generate_key()

if __name__ == "__main__":
   mensaje = input("Ingrese el texto a encriptar: ")

   encrypt_message(mensaje)

   # Generamos un archivo de texto con el mensaje ya encriptado:
   archivo_mensaje_encriptado = open("mensaje_encriptado.txt", "w")
   archivo_mensaje_encriptado.write(str(encrypted_message))
   archivo_mensaje_encriptado.close()

   print("Llave generada.")
   print("Mensaje encriptado exitosamente.")



