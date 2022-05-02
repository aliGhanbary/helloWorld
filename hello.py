import socket
import threading

server= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipv4=socket.gethostbyname(socket.gethostname())
port=5626

print(ipv4)
server.bind((ipv4, port))
server.listen()
print("wait for other players...")

def handle_client(client, address):
    print("("+str(client)+" , "+str(address)+") has been connected")


while True:
    (client, address)= server.accept()
    thread=threading.Thread(target=handle_client,args=(client,address))
    thread.start()
    print(str(threading.activeCount()-1)+" devices has been connected to the server")
