from cryptography.fernet import Fernet



def generate_key(): 
    """
    Generates a key and save it into a file
    Los archivos con extensión .key se usan para las llaves.

    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file: #with es una sentencia propia de python para abrir archivos. 
        key_file.write(key)



def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()


# Encripta el mensaje:
def encrypt_message(message):
    
    # Carga la llave que generó generate_key():
    key = load_key()
    
    # Codifica el mensaje y lo encripta: 
    encoded_message = message.encode()
    f = Fernet(key)
    
    global encrypted_message
    encrypted_message = f.encrypt(encoded_message)

    print(encrypted_message)


generate_key()

if __name__ == "__main__":
   mensaje = input("Ingrese el texto e encriptar: ")

   encrypt_message(mensaje)

   # Generamos un archivo de texto con el mensaje ya encriptado:
   archivo_mensaje_encriptado = open("mensaje_encriptado.txt", "w")
   archivo_mensaje_encriptado.write(str(encrypted_message))
   archivo_mensaje_encriptado.close()



