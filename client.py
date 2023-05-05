import socket, os, time

buffer = 0

HOST = '127.0.0.1'
PORT = 4577

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    with open('image.jpg', 'rb') as f:
        size = os.path.getsize('image.jpg')
        while True:
            buffer += 1024
            buffer_read = size - buffer

            if buffer_read < 1024:
                data = f.read(buffer_read)
            else:
                data = f.read(1024)

            if not data:
                break
            
            s.sendall(data)

            print(f"Sending... {buffer}/{size}", end='\r')
            if buffer_read < 1024:
                break
            time.sleep(0.5)
        
        print('Done...!')