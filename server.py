import cv2
import socket
import pickle

s = socket.socket()
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_ip = "ip"
server_port = port
s.bind((server_ip,server_port)) 
print("Ask client to connect!!!")

s.listen()
client_session , addr = s.accept()

print("The server is connected to ",addr)

cap = cv2.VideoCapture(0)
while True:
    ret , photo = cap.read()
    photo = cv2.resize(photo,(700,500))
    ret, buffer = cv2.imencode('photo.PNG',photo)
    Image_in_bytes = pickle.dumps(buffer)
    client_session.send(Image_in_bytes)

    received_data = client_session.recv(1000000)
    
    try:
        data = pickle.loads(received_data)
        data = cv2.imdecode(data,cv2.IMREAD_COLOR)
        if data is not None :
            cv2.imshow('SERVER',data)
            if cv2.waitKey(10) == 13 :
                break
    except: 
        print("Reconnecting...")
cv2.destroyAllWindows()

