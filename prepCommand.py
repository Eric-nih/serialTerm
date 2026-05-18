def prepCommand(str):
    output = bytearray(b'\x02')
    output += bytearray(str,"utf-8")
    output += bytearray('\r\n',"utf-8")
    return output                 