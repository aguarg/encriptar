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
    
    # Carga la llave que genera generate_key() y la asigna a key:
    key = load_key()
    
    # Codifica el mensaje a bytes y lo encripta: 
    encoded_message = message.encode()
    f = Fernet(key)
    
    global encrypted_message
    encrypted_message = f.encrypt(encoded_message)

    


generate_key()

if __name__ == "__main__":

    accion = input("""PRESIONE:
         1) PARA ENCRIPTAR 
         2) PARA DESENCRIPTAR
         """) 

    # ENCRIPTAR:
    if accion == "1":
        mensaje_para_encriptar = input("Ingrese el texto e encriptar: ")

        encrypt_message(mensaje_para_encriptar)

        # Generamos un archivo de texto con el mensaje ya encriptado:
        archivo_mensaje_encriptado = open("mensaje_encriptado.txt", "w")
        archivo_mensaje_encriptado.write(str(encrypted_message))
        archivo_mensaje_encriptado.close()

        print("Archivo con mensaje encriptado y clave creados satisfactoriamente.")



    # DESENCRIPTAR:
    else:
        

        print("holiisss") 
        
        """"
        Creo que uno de los tantos errores que me tira, es porque input devuelve una string, pero mas abajo,
        cuando quiero desencriptar, el método decrypt() de Fernet requiere el el argumento en bytes (que se genera cuando
        usamos encrypt() mas arriba).
        """
        mensaje_a_desencriptar = input("Introduzca el mensaje a desencriptar: ")
        
        mensaje_a_desencriptar = bytes(mensaje_a_desencriptar,'utf-8') # esto est'aagregado a las piñas. No sé si funciona.
        

        llave = input("Introduzca la llave: ")
        llave = Fernet(llave)

        
        # Desencripta el mensaje:
        def decrypt_message(mensaje_para_desencriptar):
    
            mensaje_desencriptado = llave.decrypt(mensaje_para_desencriptar)


            print(mensaje_desencriptado.decode())


        decrypt_message(mensaje_a_desencriptar)   