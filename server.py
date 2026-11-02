import socket

HOST = "127.0.0.1"
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print("Server waiting for a client...")

    connection, address = server.accept()

    with connection:
        print("Connected by", address)

        while True:
            message = connection.recv(1024).decode("utf-8")

            if not message or message.lower() == "quit":
                print("Client left the chat.")
                break

            print("Client:", message)
            reply = input("You: ")
            connection.sendall(reply.encode("utf-8"))

            if reply.lower() == "quit":
                break