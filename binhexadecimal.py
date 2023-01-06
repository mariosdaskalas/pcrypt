import binascii

def binhex_function():
    print("You choose Binary - Hexadecimal.")
    print("Please type 'binary' if you want to convert from 'binary' to 'hex':")
    print("Please type 'hex' if you want to convert from 'hex' to 'binary':")

    binary_input = input()

    if (binary_input == "binary"):
        print("Give the binary value you want to convert...")

        txt = input()
        hex_txt = hex(int(txt, 2))
        hex_txt = hex_txt[2:]
        print(hex_txt.upper())
    
    if (binary_input == "hex"):
        print("Give the hex value you want to convert...")

        txt = input()
        bin_txt = bin(int(txt, 16))[2:]
        print(bin_txt)