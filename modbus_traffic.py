import socket
from protocol.pkt import Modbus
from datetime import datetime
from protocol.codes import *
import argparse
import time

DESTINATION_IP = "192.168.1.22"
DESTINATION_PORT = 502
BUFFER_SIZE = 560
N_PACKETS = 1000

# in seconds
DELAY = 0.1340666407541925


def continuous(code_value):
    # Establish TCP Connection
    message = Modbus(code(code_value)).raw
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((DESTINATION_IP, DESTINATION_PORT))
    print("Connected to slave")
    try:
        for i in range(N_PACKETS):
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            tic = datetime.now()
            s.recv(BUFFER_SIZE)
            toc = datetime.now()
            w8(tic, toc)

    finally:
        s.close()
    print("DONE")


def bursts_of_main():
    # Establish TCP Connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((DESTINATION_IP, DESTINATION_PORT))
    print("Connected")
    try:
        for i in range(N_PACKETS):
            # Create Modbus packet
            message = Modbus(READ_COILS_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            tic = datetime.now()
            s.recv(BUFFER_SIZE)
            toc = datetime.now()
            w8(tic, toc)

        for i in range(N_PACKETS):
            message = Modbus(READ_DISCRETE_INPUTS_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            tic = datetime.now()
            s.recv(BUFFER_SIZE)
            toc = datetime.now()
            w8(tic, toc)

        for i in range(N_PACKETS):
            message = Modbus(READ_HOLDING_REGISTERS_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            tic = datetime.now()
            s.recv(BUFFER_SIZE)
            toc = datetime.now()
            w8(tic, toc)

        for i in range(N_PACKETS):
            message = Modbus(READ_INPUT_REGISTERS_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            tic = datetime.now()
            s.recv(BUFFER_SIZE)
            toc = datetime.now()
            w8(tic, toc)

        for i in range(N_PACKETS):
            message = Modbus(WRITE_SINGLE_COIL_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            tic = datetime.now()
            s.recv(BUFFER_SIZE)
            toc = datetime.now()
            w8(tic, toc)

        for i in range(N_PACKETS):
            message = Modbus(WRITE_SINGLE_REGISTER_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            tic = datetime.now()
            s.recv(BUFFER_SIZE)
            toc = datetime.now()
            w8(tic, toc)

        for i in range(N_PACKETS):
            message = Modbus(READ_EXCEPTION_STATUS_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            tic = datetime.now()
            s.recv(BUFFER_SIZE)
            toc = datetime.now()
            w8(tic, toc)

        for i in range(N_PACKETS):
            message = Modbus(DIAGNOSTICS_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            tic = datetime.now()
            s.recv(BUFFER_SIZE)
            toc = datetime.now()
            w8(tic, toc)

        for i in range(N_PACKETS):
            message = Modbus(GET_COMM_EVENT_COUNTER_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            tic = datetime.now()
            s.recv(BUFFER_SIZE)
            toc = datetime.now()
            w8(tic, toc)

        for i in range(N_PACKETS):
            message = Modbus(GET_COMM_EVENT_LOG_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            tic = datetime.now()
            s.recv(BUFFER_SIZE)
            toc = datetime.now()
            w8(tic, toc)

        for i in range(N_PACKETS):
            message = Modbus(WRITE_MULTIPLE_COILS_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            tic = datetime.now()
            s.recv(BUFFER_SIZE)
            toc = datetime.now()
            w8(tic, toc)

        for i in range(N_PACKETS):
            message = Modbus(WRITE_MULTIPLE_REGISTERS_Q).raw
            s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
            tic = datetime.now()
            s.recv(BUFFER_SIZE)
            toc = datetime.now()
            w8(tic, toc)

    finally:
        s.close()
    print("DONE")


def one_of_each():
    # Establish TCP Connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((DESTINATION_IP, DESTINATION_PORT))
    print("Connected")
    try:
        message = Modbus(READ_COILS_Q).raw
        s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
        tic = datetime.now()
        s.recv(BUFFER_SIZE)
        toc = datetime.now()
        w8(tic, toc)

        message = Modbus(READ_DISCRETE_INPUTS_Q).raw
        s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
        tic = datetime.now()
        s.recv(BUFFER_SIZE)
        toc = datetime.now()
        w8(tic, toc)

        message = Modbus(READ_HOLDING_REGISTERS_Q).raw
        s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
        tic = datetime.now()
        s.recv(BUFFER_SIZE)
        toc = datetime.now()
        w8(tic, toc)

        message = Modbus(WRITE_MULTIPLE_REGISTERS_Q).raw
        s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
        tic = datetime.now()
        s.recv(BUFFER_SIZE)
        toc = datetime.now()
        w8(tic, toc)

        message = Modbus(READ_INPUT_REGISTERS_Q).raw
        s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
        tic = datetime.now()
        s.recv(BUFFER_SIZE)
        toc = datetime.now()
        w8(tic, toc)

        message = Modbus(WRITE_SINGLE_COIL_Q).raw
        s.sendto(message, (DESTINATION_IP, DESTINATION_PORT))
        s.recv(BUFFER_SIZE)

    finally:
        s.close()
    print("DONE")


def w8(tic, toc):
    tdelta = (toc - tic).total_seconds()
    if tdelta < DELAY:
        time.sleep(DELAY-tdelta)


def interleaved(cod_1, cod_2):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((DESTINATION_IP, DESTINATION_PORT))
    message1 = Modbus(code(cod_1)).raw
    message2 = Modbus(code(cod_2)).raw
    print("Connected")
    try:
        for i in range(N_PACKETS):
            s.sendto(message1, (DESTINATION_IP, DESTINATION_PORT))
            tic = datetime.now()
            s.recv(BUFFER_SIZE)
            toc = datetime.now()
            w8(tic, toc)
            s.sendto(message2, (DESTINATION_IP, DESTINATION_PORT))
            tic = datetime.now()
            s.recv(BUFFER_SIZE)
            toc = datetime.now()
            w8(tic, toc)
    finally:
        s.close()
    print("DONE")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a ModbusTCP traffic to specified host addr:port ")
    parser.add_argument("addr", help="Slave IP address", type=str)
    parser.add_argument("port", type=int, help="Slave TCP port", default=502)
    parser.add_argument("--option", help="Specifies the burst option: ", type=int, choices=[1, 2, 3, 4], default=3)
    parser.add_argument("-d", "--delay", help="Specifies the delay between sended packets: ", type=float, default=0.15)
    parser.add_argument("-n", "--number", help="Specifies the number of packets per burst: ", type=int, default=1000)
    parser.add_argument("--code", help="Specifies Modbus function code in decimal of the burst: ", type=int,
                        choices=[1, 2, 3, 4, 15], action="append")
    parser.add_argument("-v", "--verbose", help="increase output verbosity", action="store_true", default=False)

    args = parser.parse_args()
    if args.option == 1 and args.code is None:
        parser.error("--option requires --code")
    if args.option == 4 and len(args.code) < 2:
        parser.error("--option 4 requires --code [code_1] [code_2]")

    DESTINATION_IP = args.addr
    DESTINATION_PORT = args.port
    N_PACKETS = args.number
    DELAY = args.delay
    VERB = args.verbose

    if args.option is 1:
        print("Starting continuous traffic...")
        continuous(args.code[0])
    elif args.option is 2:
        print("Starting bursts of Modbus packets...")
        bursts_of_main()
    elif args.option is 3:
        print("Sending one packet of each Modbus function code...")
        one_of_each()
    elif args.option is 4:
        print("Starting Interleaved burst with function codes {} and {}".format(args.code[0], args.code[1]))
        interleaved(cod_1=args.code[0], cod_2=args.code[1])
    else:
        raise Exception("OptionError: Invalid option.")
