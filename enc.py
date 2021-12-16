from cryptography.fernet import Fernet

# SECCIÓN CON CÓDIGO PARA ENCRIPTAR:

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





# SECCIÓN CON CÓDIGO PARA DESENCRIPTAR:

# Función que desencripta el mensaje:
def decrypt_message(encrypted_message):
    
    key = input("INGRESE LA LLAVE: " )

    f = Fernet(key)
    
    # Desencripta el mensaje usando la llave asignada a f, ingresada por el usuario.
    decrypted_message = f.decrypt(encrypted_message)

    print(decrypted_message.decode())





# Inicio:
if __name__ == "__main__":
    #Opciones:
    eleccion = input("""ELEGIR LA OPCIÓN DESEADA Y PRESIONAR ENTER:
    1) PARA ENCRIPTAR MENSAJE
    2) PARA DESENCRIPTAR UN MENSAJE ENCRIPTADO

    """)
    
    #Opción Encriptar:
    if eleccion == "1":
        
        generate_key()

        global mensaje
        mensaje = input("INGRESE EL TEXTO A ENCRIPTAR: ")

        encrypt_message(mensaje)

        # Generamos un archivo de texto con el mensaje ya encriptado:
        archivo_mensaje_encriptado = open("mensaje_encriptado.txt", "w")
        archivo_mensaje_encriptado.write(str(encrypted_message))
        archivo_mensaje_encriptado.close()

        print("LLAVE GENERADA.")
        print("MENSAJE ENCRIPTADO CON ÉXITO")

    
    # Opción Desencriptar:    
    elif eleccion == "2":
        # Input para ingresar el mensaje encriptado:
        
        mensaje = input("INGRESE EL MENSAJE ENCRIPTADO: ")

        # Codifica el mensaje a bytes y saca el b" iniciales y el " del final en el mensaje encriptado:
        mensaje = mensaje.encode()[1:-1]
        # el método encode() transforma las strings a bytes, necesarios para el módulo Fernet, que no acepta strings como tokens.

        decrypt_message(mensaje)
