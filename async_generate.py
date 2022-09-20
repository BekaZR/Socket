import socket
from select import select


tasks = []

to_read = {}
to_write = {}

def server():
    server_socked = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socked.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socked.bind(('localhost', 8000))
    server_socked.listen()

    while True:
        yield ('read',server_socked)
        
        client_socked, address = server_socked.accept()
        print("Connetction from", address)
        
        tasks.append(client(client_socked))


def client(client_socked):
    while True:
        yield ('read', client_socked)
        
        request = client_socked.recv(4096)
        
        if not request:
            break
        else:
            response = 'Hello world!\n'.encode()
            
            yield ('write', client_socked)
            client_socked.send(response)
            
    print('Outside inner loop')
    client_socked.close()


def even_loop():
    
    while any([tasks, to_read, to_write]):
        
        while not tasks:
            ready_to_read, ready_to_write, _ = select(to_read, to_write, [])
            
            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))
                
            for sock in ready_to_write:
                tasks.append(to_write.pop(sock))
    
        try:
            
            task = tasks.pop(0)
            reason, sock = next(task)
            
            if reason == 'read':
                to_read[sock] = task
            if reason == 'write':
                to_write[sock] = task
                
            
        except StopIteration:
            pass
            

tasks.append(server())
even_loop()