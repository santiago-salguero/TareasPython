import socket 
import threading

host = '127.0.0.2'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()
print(f"Server Running on {host}:{server}")

clients = []
usernames = []

def broadcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message)

def handle_messages(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message,client)
        except:
            index = clients.index(client)
            username = usernames[index]
            broadcast(f"ChatBot: {username} desconectado.".encode('utf-8'), client)
            clients.remove(client)
            usernames.remove(username)
            client.close()

            break

def receive_connections():
    while True:
        client, adresss = server.accept()
        client.send("@username".encode("utf-8"))
        username = client.recv(1024).decode('utf-8')

        clients.append(client)
        usernames.append(username)

        print(f"{username} esta conectado con {str(address)}")

        message = f"ChatBot: {username} se ha unido al chat!".encode("utf-8")
        broadcast(message,client)
        client.send("conectado con el servidor".encode('utf-8'))

        thread = threading.Thread(target=handle_messages, args=(client,))
        thread.start()

receive_connections()
