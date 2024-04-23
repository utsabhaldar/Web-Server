import socket
# import time

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# server_socket.setblocking(False)

server_socket.bind((SERVER_HOST, SERVER_PORT))

server_socket.listen(5)

print(f"Listening on port {SERVER_PORT}")

# try:
#     client_socket, client_address = server_socket.accept()

#     print(client_socket)
#     print(client_address)

# except:
#     time.sleep(1)
#     print('error caught, can do something!')

while True:
    client_socket, client_address = server_socket.accept()

    # print(client_socket)
    # print(client_address)

    request = client_socket.recv(1500)
    print(request)

    headers = request.split('\n')
    # print(headers[0])
    first_header_components = headers[0].split()

    http_method = first_header_components[0]
    path = first_header_components[1]

    if http_method == 'GET':
        if path == '/':
            fin = open('index.html')

            # STATUS LINE
            # HEADERS
            # MESSAGE-BODY

            # client_socket.sendall(response.encode())
            # client_socket.close()

        elif path == '/book':
            fin = open('book.json')

        content = fin.read()
        fin.close()
        response = 'HTTP/1.1 200 OK\n\n' + content


    else:
        response = 'HTTP/1.1 405 Method Not Allowed\n\nAllow: GET'
    
    client_socket.sendall(response.encode())
    client_socket.close()