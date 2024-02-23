import socket
from threading import Thread


HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 80  # The port used by the server
username = ""
def receive_messages(sock):
    """Receive messages from the server and display them."""
    while True:
        try:
            msg = sock.recv(1024).decode()
            if msg[0:3] == "SRV":
                global username
                username = "[" + msg[3::] + "]: "
            else:
                print("\033[32m", msg, "\033[0m")
        except Exception as e:
            print(f"[!] Error receiving message: {e}")
            break

def send_messages(sock):
    """Send user input to the server."""
    while True:
        user_input = input()
        if user_input.lower() == "exit":
            break
        msg = username + user_input
        sock.sendall(msg.encode())


client_socket = socket.socket()

try:
    # Connect to the server
    client_socket.connect((HOST, PORT))
    print(f"[*] Connected to {HOST}:{PORT}")

    # Start threads for receiving and sending messages
    Thread(target=receive_messages, args=(client_socket,)).start()
    Thread(target=send_messages, args=(client_socket,)).start()

except ConnectionRefusedError:
    print("[!] Server is not running or incorrect server address.")
    client_socket.close()


