import socket

def main():
    
    scIP = "192.168.31.128"
    scPort = 8080
    sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sc.connect ((scIP,scPort))
    
    temp_frh = input ("Please enter temperature in Fahrenherit : ")
    sc.send(temp_frh.encode())
    
    temp_celc = sc.recv(1024).decode()
    print("Temperature in Celcius : ,temp_celc)
    
    main()
