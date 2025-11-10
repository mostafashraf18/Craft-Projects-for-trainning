import socket


HOST = "127.0.0.1"
PORT = 9000

RESPONSE = b"""\
HTTP/1.1 200 OK
Content-type: text/html
Content-length: 15

<h1>Hello!</h1>""".replace(b"\n", b"\r\n")

#By Default socket creates TCP sockets

with socket.socket() as server_sock:
    #This tells the kernel to reuse sockets that are in 'TIME_WAit'
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    #This tells the kernel what address to bind to.
    server_sock.bind((HOST, PORT))

    server_sock.listen(0)
    print(f"Listening onn {HOST}:{PORT}...")

    while True:
        client_sock, client_addr = server_sock.accept()
        print(f"New Connection from {client_addr}.")

        with client_sock:
          client_sock.sendall(RESPONSE)

