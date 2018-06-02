import dpkt
import socket
from scapy.all import *

WRITE_MULTIPLE_COILS_RESPONSE = b'\x00\x00\x00\x00\x00\x06\x00\x0F\x00\x00\x00\x06'

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0', 502))
    s.listen(10)
    cnx, addr = s.accept()
    print("Connection donde by " + str(addr))
    while True:
        # data = cnx.recv(1024).decode()
        data = cnx.recv(1024)     # OPTIMIZE: lower buffer = faster
        if not data:
            pass
        else:
            print(data)
            cnx.sendto(WRITE_MULTIPLE_COILS_RESPONSE, (addr[0], addr[1]))

    cnx.close()


if __name__ == "__main__":
    main()