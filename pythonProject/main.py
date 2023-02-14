import socket

print("에코 클라이언트 시작됨")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Stream은 TCP, datagram은 UDP
client_socket.connect(("165.246.115.165", 20000))
print("서버에 연결됨")

while True:
    msg = input("전송 메세지 입력: ")
    if msg == "exit" or "EXIT":  #종료 메세지
        break
    client_socket.sendall((msg+"\n").encode())  #송신
    data = client_socket.recv(1024).decode()  #수신 (1바이트로)
    print(f"서버로부터 받은 메세지: {data}")

client_socket.close()
