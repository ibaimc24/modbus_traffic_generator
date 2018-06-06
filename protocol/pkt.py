import struct

LEN_BYTE = 5
CODE_BYTE = 7

class Modbus(object):

    def __init__(self):
        self.__raw__ = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        #self.__pktlen__ = self.__header__[5]
        self.to_modify = bytearray(self.__raw__)
        self.raw = bytes(self.to_modify)

    def set_len(self, value):
        self.to_modify[LEN_BYTE] = value
        self.raw = bytes(self.to_modify)

    def set_code(self, code):
        self.to_modify[CODE_BYTE] = code
        self.raw = bytes(self.to_modify)


class ReadCoils(Modbus):

    """
    The query message specifies the starting coil (SAHI (Starting Address High) and SALO(Starting Address Low)) and
    quantity of coils to be read (NPH (Number Of Points High) and NPL (Number Of Points Low)).
    Coils are addressed starting at zero:  coils 1–16 are addressed as 0–15
    """

    def __init__(self, start_address, number_of_points):
        super().__init__()
        self.to_modify = self.to_modify[0: CODE_BYTE+5]
        self.to_modify[CODE_BYTE] = 1
        self.to_modify[LEN_BYTE] = 6
        self.to_modify[8] = struct.pack('>H', start_address)[0]
        self.to_modify[9] = struct.pack('>H', start_address)[1]
        self.to_modify[10] = struct.pack('>H', number_of_points)[0]
        self.to_modify[11] = struct.pack('>H', number_of_points)[1]
        self.raw = bytes(self.to_modify)

    def size(self):
        # Must be always 12
        return len(self.raw)


class ReadDiscreteInputs(Modbus):

    """
    Reads the ON/OFF status of discrete inputs (1X references) in the slave. Broadcast is not supported.
    The query message specifies the starting input and quantity of inputs to be read. Inputs are addressed starting at
    zero:  inputs 1–16 are addressed as 0–15.
    """

    def __init__(self, start_address, number_of_points):
        super().__init__()
        self.to_modify = self.to_modify[0: CODE_BYTE+5]
        self.to_modify[CODE_BYTE] = 2
        self.to_modify[LEN_BYTE] = 6
        self.to_modify[8] = struct.pack('>H', start_address)[0]
        self.to_modify[9] = struct.pack('>H', start_address)[1]
        self.to_modify[10] = struct.pack('>H', number_of_points)[0]
        self.to_modify[11] = struct.pack('>H', number_of_points)[1]
        self.raw = bytes(self.to_modify)

    def size(self):
        # Must be always 12
        return len(self.raw)


class ReadHoldingRegisters(Modbus):

    """
    Reads the ON/OFF status of discrete inputs (1X references) in the slave. Broadcast is not supported.
    The query message specifies the starting input and quantity of inputs to be read. Inputs are addressed starting at
    zero:  inputs 1–16 are addressed as 0–15.
    """

    def __init__(self, start_address, number_of_points):
        super().__init__()
        self.to_modify = self.to_modify[0: CODE_BYTE+5]
        self.to_modify[CODE_BYTE] = 1
        self.to_modify[LEN_BYTE] = 6
        self.to_modify[8] = struct.pack('>H', start_address)[0]
        self.to_modify[9] = struct.pack('>H', start_address)[1]
        self.to_modify[10] = struct.pack('>H', number_of_points)[0]
        self.to_modify[11] = struct.pack('>H', number_of_points)[1]
        self.raw = bytes(self.to_modify)

    def size(self):
        # Must be always 12
        return len(self.raw)