import socket

HOST = "127.0.0.1"
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    print("Connected to the chat. Type quit to leave.")

    while True:
        message = input("You: ")
        client.sendall(message.encode("utf-8"))

        if message.lower() == "quit":
            break

        reply = client.recv(1024).decode("utf-8")

        if not reply:
            print("Server disconnected.")
            break

        print("Server:", reply)

        if reply.lower() == "quit":
            break