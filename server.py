import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    s.bind(('127.0.0.1', 4577))

    s.listen()

    print(f'Listening on port {4577}')

    conn, addr = s.accept()

    print(f'Connected by {addr}')

    with conn:
        with open('image-copy.jpg', 'wb') as f:
            while True:
                data = conn.recv(1024)
                print(data)
                f.write(data)
                if not data:
                    break