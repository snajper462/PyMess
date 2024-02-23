import socket
from threading import Thread
# server.py

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 80  # Port to listen on (non-privileged ports are > 1023)

connected_clients = []
users = ["Admin", "user1", "user2", "user3", "user4"]
passwd = ["haslo123", "pass1", "pass2", "pass3", "pass4"]


def authentication(client_sock):
    while True:
        client_sock.send(b"Username: ")
        username = client_sock.recv(1024).decode()
        if username in users:
            requested_passwd = passwd[users.index(username)]
            client_sock.send(b"Password: ")
            password = client_sock.recv(1024).decode()
            if requested_passwd == password:
                username_pass = "SRV"+username
                client_sock.send(username_pass.encode())
                break
            else:
                client_sock.send(b"Wrong password!")
        else:
            client_sock.send(b"No user under this name! ")


def receive_messages(sock):
    """Receive messages from the server and display them."""
    while True:
        try:
            msg = sock.recv(1024).decode()
            print("\033[32m", msg, "\033[0m")
            for client in connected_clients:
                if client != sock:
                    client.sendall(msg.encode())
        except Exception as e:
            print(f"[!] Error receiving message: {e}")
            break


def send_messages(clients):
    """Send user input to the server."""
    while True:
        user_input = input()
        if user_input.lower() == "exit":
            break
        msg = "[Server]: " + user_input
        for client in clients:
            client.sendall(msg.encode())


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    while True:
        server_socket.listen()
        new_client_socket, addr = server_socket.accept()
        if new_client_socket not in connected_clients:
            authentication(new_client_socket)
            print("New user : ", addr, " connected")
            connected_clients.append(new_client_socket)
            Thread(target=receive_messages, args=(new_client_socket,)).start()
            Thread(target=send_messages, args=(connected_clients,)).start()
