import socket
import threading

client: socket.socket
ADDR = None
recvQ = []
recvQLock = threading.Lock()
connected = False


def return_msg():
    if recvQ == []:
        return ""
    msg = recvQ[0]
    recvQLock.acquire()
    recvQ.pop(0)
    recvQLock.release()
    return msg


def connect_client_socket(address, name):
    global client
    global recvQ
    global connected
    recvQ = []

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM,)
    try:
        client.connect(address)
        connected = True
        client.send(bytes(name, 'utf-8'))
        t1 = threading.Thread(target=communicate, daemon=True)
        t1.start()
        return True
    except Exception as e:
        print(f"Connection to server failed because {e}")
        return False


def send_to_server(msg):
    global client
    if not client:
        print("Unable to send message.")
    client.send(bytes(msg, 'utf-8'))


def communicate():
    global client
    global connected

    while connected:
        # if no message is received it is empty string
        msg = bytes.decode(client.recv(2000))
        if msg == "" or msg.isspace():
            continue
        recvQLock.acquire()
        recvQ.append(msg)
        recvQLock.release()
        print('\n'+msg+"\nEnter message to send to server: ", end="")


def disconnect():
    global client
    global connected
    client.send(bytes("", 'utf-8'))
    connected = False
    client.shutdown(socket.SHUT_RDWR)
    client.close()
    print("Disconnected")
