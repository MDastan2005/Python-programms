import socket
import threading
from constants import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
clients = []


def receive_message(conn: socket.socket, addr: tuple) -> str:
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if not msg_length:
        return None
    msg_length = int(msg_length)
    msg = conn.recv(msg_length).decode(FORMAT)
    if msg == DISCONNECT_MESSAGE:
        print(f"[DISCONNECTION] {addr} disconnected.")
        return None
    print(f"[{addr}] {msg}")
    return msg


def send_message(client: socket.socket, msg: str) -> None:
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def send_all_from_client(senderClient: socket.socket, msg: str) -> None:
    for client, _ in clients:
        if client != senderClient:
            send_message(client, msg)


def send_all(msg : str):
    for client, _ in clients:
        send_message(client, msg)


def send_command(senderClient: socket.socket, cmd: str, num: int, *args) -> None:
    send_all_from_client(senderClient, cmd)
    send_all_from_client(senderClient, str(num))
    for arg in args:
        send_all_from_client(senderClient, str(arg))


def handle_client(conn: socket.socket, addr: tuple) -> None:
    print(f"[NEW CONNECTION] {addr} connected.")
    clients.append((conn, addr))

    connected = True
    while connected:
        msg = receive_message(conn=conn, addr=addr)
        if msg is None:
            connected = False
            break
        thread = threading.Thread(target=send_all_from_client, args=(conn, msg))
        thread.start()

    clients.remove((conn, addr))
    conn.close()


def start() -> None:
    server.listen(1)
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
