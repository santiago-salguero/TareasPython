import socket
import threading

usuario = input('Ingrese su usuario: ')

host = '127.0.0.1'
port = 55555

clientes= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientes.connect((host, port))

def recibir_mensajes():
    while True:
        try:
            mensaje = clientes.recv(1024).decode('utf-8')
            if mensaje == "@usuario":
                clientes.send(usuario.encode('utf-8'))
            else:
                print(mensaje)
        except:
            print("ha ocurrido un error")
            clientes.close
            break


def escribir_mensajes():
    while True:
        mensaje= f"{usuario}: {input('')}"
        clientes.send(mensaje.encode('utf-8'))

receive_thread = threading.Thread(target=recibir_mensajes)
receive_thread.start()

write_thread = threading.Thread(target= escribir_mensajes)
write_thread.start()