import socket

def main():
  
    scIP = "192.168.31.128"
    scPort = 8080
    serversc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversc.bind ((scIP,scPort))
    serversc.listen(1)
    
    print("Waiting for Client....")
    
    while True:
    
           clientsocket, addr = serversc.accept()
           print("Got a connection from %s" % str(addr))
           
           temp_frh = clientsocket.recv(1024).decode()
           temp_celc = frh_to_celc (float(temp_frh))
           temp_celc = round (temp_celc,2)
           temp_celc = str(temp_celc)
           clientsocket.send(temp_celc.encode())
           
      def frh_to_celc(temp_frh):
      
            temp_celc = (temp_frh -32) * (5/9)
            return temp_celc
            
       main()
