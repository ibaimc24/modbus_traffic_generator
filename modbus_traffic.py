from scapy.all import *
from protocol.pkt import Modbus
import time
from protocol.codes import *

DESTINATION_IP = "192.168.1.7"
DESTINATION_PORT = 502
BUFFER_SIZE = 1024


def latency():
    time.sleep(3)
    pass


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((DESTINATION_IP, DESTINATION_PORT))
        print("Connected")
        while True:
            message = Modbus(WRITE_MULTIPLE_COILS).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            latency()
            data = s.recv(BUFFER_SIZE)
            print(data)

    finally:
        s.close()


if __name__ == "__main__":
    main()
