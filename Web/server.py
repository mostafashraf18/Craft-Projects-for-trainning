import socket
import typing


HOST = "127.0.0.1"
PORT = 9000

RESPONSE = b"""\
HTTP/1.1 200 OK
Content-type: text/html
Content-length: 15

<h1>Hello!</h1>""".replace(b"\n", b"\r\n")


def iter_lines(sock: socket.socket, bufsize: int =16_384)-> typing.Generator[bytes, None, bytes]:
   """Given a socket, read all the individual CRLF-separeted lines adn yield each one 
   until an empty one is found. Return the remainder after the empty line."""

   buff = b""
   while True:
      data = sock.recv(bufsize)
      if not data:
         return b""
      
      buff += data
      while True: 
        try:
            i = buff.index(b"\r\n")
            line, buff = buff[:i], buff[i + 2:]
            if not line:
               return buff
            
            yield line
        except IndexError:
           break

#By Default socket creates TCP sockets
class Request(typing.NamedTuple):
    method: str
    path: str
    headers: typing.Mapping[str, str]

    @classmethod
    def from_socket(cls, sock: socket.socket) -> "Request":
        """Read and parse the request from a socket object.

        Raises:
          ValueError: When the request cannot be parsed.
        """
        lines = iter_lines(sock)

        try:
            request_line = next(lines).decode("ascii")
        except StopIteration:
            raise ValueError("Request line missing.")

        try:
            method, path, _ = request_line.split(" ")
        except ValueError:
            raise ValueError(f"Malformed request line {request_line!r}.")

        headers = {}
        for line in lines:
            try:
                name, _, value = line.decode("ascii").partition(":")
                headers[name.lower()] = value.lstrip()
            except ValueError:
                raise ValueError(f"Malformed header line {line!r}.")

        return cls(method=method.upper(), path=path, headers=headers)
    
    
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
          
          for request_line in iter_lines(client_sock):
             print(request_line)
          client_sock.sendall(RESPONSE)

