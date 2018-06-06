import argparse
from protocol.pkt import *
import socket
import time

DESTINATION_IP = "0.0.0.0"
DESTINATION_PORT = 502
BUFFER_SIZE = 512

def dataaddr_exceptions():
    """
    If starting address + number of outputs is not in range, an ExceptionCode (02)
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((DESTINATION_IP, DESTINATION_PORT))
    try:
        for i in range(257):
            pkt = ReadCoils(start_address=i, number_of_points=1999)
            message = pkt.raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            s.recv(BUFFER_SIZE)
            time.sleep(1)
    finally:
        s.close()

def outputs_exceptions():
    """
    If number of requested outputs is larger than 2000, an ExceptionCode (03) is returned.
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((DESTINATION_IP, DESTINATION_PORT))
    try:
        pkt = ReadCoils(start_address=0, number_of_points=2001)
        message = pkt.raw
        s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
        s.recv(BUFFER_SIZE)

        # Read Discrete Inputs
        pkt.set_code(2)
        message = pkt.raw
        s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
        s.recv(BUFFER_SIZE)

    finally:
        s.close()

def function_exceptions():
    """
    If function code specified in Modbus packet is not supported by the device, an ExceptionCode (01) is
    retrned by the slave.
    :return:
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((DESTINATION_IP, DESTINATION_PORT))
    try:
        for i in range(46):
            pkt = Modbus()
            pkt.set_code(i)
            pkt.set_len(6)
            message = pkt.raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            s.recv(BUFFER_SIZE)
            time.sleep(1)
    finally:
        s.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='''Generate a ModbusTCP traffic to specified host addr:port. It builds 
    Modbus packets with specified function codes and it waits until slaves answers. The delay between sended packets 
    can be set by -d option.''')
    parser.add_argument("addr", help="Slave IP address", type=str)
    parser.add_argument("port", type=int, help="Slave TCP port", default=502)
    parser.add_argument("--function", action="store_true", help="Force slave to get function error")
    parser.add_argument("--noutputs", action="store_true", help="Force slave to get quantity outputs error")
    parser.add_argument("--dataaddr", action="store_true", help="Force slave to get illegal data address error")

    args = parser.parse_args()

    DESTINATION_IP = args.addr
    DESTINATION_PORT = args.port

    if args.function:
        function_exceptions()
    if args.noutputs:
        outputs_exceptions()
    if args.dataaddr:
        dataaddr_exceptions()
