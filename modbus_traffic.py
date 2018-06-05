import socket
from protocol.pkt import Modbus
import time
from protocol.codes import *
import argparse

DESTINATION_IP = "192.168.1.22"
DESTINATION_PORT = 502
BUFFER_SIZE = 560


def continuous(code_value):
    try:
        # Establish TCP Connection
        message = Modbus(code(code_value)).raw

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((DESTINATION_IP, DESTINATION_PORT))
        print("Connected to slave")
        for i in range(1000):
            # Create Modbus packet
            message = Modbus(WRITE_MULTIPLE_COILS_Q).raw
            # Send
            #print()
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            # Read response
            data = s.recv(BUFFER_SIZE)
            #print(data)
            # Wait for next request packet

    finally:
        s.close()


def bursts_of_main():
    try:
        # Establish TCP Connection
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((DESTINATION_IP, DESTINATION_PORT))
        print("Connected")
        for i in range(100):
            # Create Modbus packet
            message = Modbus(READ_COILS_Q).raw
            # Send
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            # Read response
            s.recv(BUFFER_SIZE)
            # print(data.hex)
            # Wait for next request packet

        for i in range(100):
            # Create Modbus packet
            message = Modbus(READ_DISCRETE_INPUTS_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            data = s.recv(BUFFER_SIZE)

        for i in range(100):
            message = Modbus(READ_HOLDING_REGISTERS_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            data = s.recv(BUFFER_SIZE)

        for i in range(100):
            message = Modbus(READ_INPUT_REGISTERS_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            data = s.recv(BUFFER_SIZE)

        for i in range(100):
            message = Modbus(WRITE_SINGLE_COIL_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            data = s.recv(BUFFER_SIZE)

        for i in range(100):
            message = Modbus(WRITE_SINGLE_REGISTER_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            data = s.recv(BUFFER_SIZE)

        for i in range(100):
            message = Modbus(READ_EXCEPTION_STATUS_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            data = s.recv(BUFFER_SIZE)

        for i in range(100):
            message = Modbus(DIAGNOSTICS_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            data = s.recv(BUFFER_SIZE)

        for i in range(100):
            message = Modbus(GET_COMM_EVENT_COUNTER_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            data = s.recv(BUFFER_SIZE)

        for i in range(100):
            message = Modbus(GET_COMM_EVENT_LOG_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            data = s.recv(BUFFER_SIZE)


        for i in range(100):
            message = Modbus(WRITE_MULTIPLE_COILS_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            data = s.recv(BUFFER_SIZE)

        for i in range(100):
            message = Modbus(WRITE_MULTIPLE_REGISTERS_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            data = s.recv(BUFFER_SIZE)


        s.close()
    finally:
        s.close()


def one_of_each():
    # Establish TCP Connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((DESTINATION_IP, DESTINATION_PORT))
    print("Connected")
    # Create Modbus packet
    message = Modbus(READ_COILS_Q).raw
    # Send
    s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
    # Read response
    data = s.recv(BUFFER_SIZE)
    message = Modbus(READ_DISCRETE_INPUTS_Q).raw
    s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
    # Read response
    data = s.recv(BUFFER_SIZE)
    message = Modbus(READ_HOLDING_REGISTERS_Q).raw
    s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
    # Read response
    data = s.recv(BUFFER_SIZE)
    message = Modbus(WRITE_MULTIPLE_REGISTERS_Q).raw
    s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
    # Read response
    data = s.recv(BUFFER_SIZE)
    message = Modbus(READ_INPUT_REGISTERS_Q).raw
    s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
    # Read response
    data = s.recv(BUFFER_SIZE)
    message = Modbus(WRITE_SINGLE_COIL_Q).raw
    s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
    # Read response
    s.close()







if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a ModbusTCP traffic to specified host addr:port ")
    parser.add_argument("addr", help="Slave IP address", type=str)
    parser.add_argument("port", type=int, help="Slave TCP port", default=502)
    parser.add_argument("--option", help="Specifies the burst option: ", type=int, choices=[1, 2, 3], default=3)
    parser.add_argument("--code", help="Specifies Modbus function code in decimal of the burst: ", type=int, choices=[1, 2, 3, 4, 15])
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true")

    args = parser.parse_args()
    if args.option==1 and args.code is None:
        parser.error("--option requires --code")

    DESTINATION_IP = args.addr
    DESTINATION_PORT = args.port
    op = args.option
    code_value = args.code

    # if args.verbosity:

    if op is 1:
        print("Starting continuous traffic...")
        continuous(code_value)
    elif op is 2:
        print("Starting bursts of Modbus packets...")
        #bursts_of_main()
    elif op is 3:
        print("Sending one packet of each Modbus function code...")
        #one_of_each()
    else:
        print("Invalid option.")
        exit(2)