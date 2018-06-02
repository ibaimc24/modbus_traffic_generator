

class Modbus(object):



    def __init__(self, code, size=10):
        self.size = size
        to_modify = bytearray(code)
        to_modify[5] = size
        self.raw = bytes(to_modify)

    def raw(self):
        return self.raw()