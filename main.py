import socket


server_socked = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socked.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socked.bind(('localhost', 8000))
server_socked.listen()

while True:
    print('Before accept()')
    client_socked, address = server_socked.accept()
    print("Connetction from", address)
    
    while True:
        print('Before recv()') 
        request = client_socked.recv(4096)
        
        if not request:
            break
        else:
            response = 'Hello world!\n'.encode()
            client_socked.send(response)
    print('Outside inner loop')
    client_socked.close()
        