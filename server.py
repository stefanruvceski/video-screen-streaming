from vidstream import StreamingServer
import  threading

server = StreamingServer('192.168.1.175', 11000)

t = threading.Thread(target=server.start_server)
t.start()

while input('') != 'STOP':
    continue

server.stop_server()
