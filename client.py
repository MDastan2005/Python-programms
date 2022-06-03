import socket
import threading
from constants import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
finish = False


def receive_message(conn: socket.socket) -> str:
    msg_length = conn.recv(HEADER).decode(FORMAT)
    if msg_length:
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        return msg


def send_message(msg: str) -> None:
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def send_command(cmd: str, num: int, *args) -> None:
    send_message(cmd)
    send_message(str(num))
    for arg in args:
        send_message(str(arg))


def receive_thread() -> str:
    msg = receive_message(client)
    print(msg)


def send_thread() -> bool:
    sendMsg = input()
    if sendMsg == "exit":
        global finish
        finish = True
        send_message(DISCONNECT_MESSAGE)
    send_message(sendMsg)


def start() -> None:
    global finish
    receiveThread = None
    sendThread = None

    while not finish:
        if receiveThread is None or not receiveThread.is_alive():
            receiveThread = threading.Thread(target=receive_thread)
            receiveThread.start()
        if sendThread is None or not sendThread.is_alive():
            sendThread = threading.Thread(target=send_thread)
            sendThread.start()
    exit(0)


start()
