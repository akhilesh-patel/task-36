import cv2
import socket
import urllib
import pickle
import numpy as np


url = 'http://windows_ip:8080/shot.PNG'

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_ip = "ip"
server_port = port

s.connect((server_ip,server_port))

while True:
    
    received_data = s.recv(1000000)
    print("Recieving")
    
    imgResp=urllib.request.urlopen(url)
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)
    img = cv2.resize(img,(700,500))
    ret, buffer = cv2.imencode('.jpg',img)
    Image_in_bytes = pickle.dumps(buffer)
    
    s.send(Image_in_bytes)
    try:
        data = pickle.loads(received_data)
        data = cv2.imdecode(data,cv2.IMREAD_COLOR)
        if data is not None :
            cv2.imshow('CLIENT',data)
            if cv2.waitKey(10) == 13 :
                break
    except: 
        print("Waiting for the server!")
     
cv2.destroyAllWindows()
