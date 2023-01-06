def binoctal_function():
    print("You choose Binary - Octal.")
    print("Please type 'binary' if you want to convert from 'binary' to 'octal':")
    print("Please type 'octal' if you want to convert from 'binary' to 'binary':")

    binary_input = input()

    if (binary_input == "binary"):
        print("Give the binary value you want to convert...")

        txt = input()
        octal = int(txt, 2)
        octal = oct(octal)
        print(octal[2:])

    if (binary_input == "octal"):
        print("Give the octal value you want to convert...")
        
        txt = input()
        bin_txt = int(txt, 8)
        bin_txt = bin(bin_txt)
        print(bin_txt[2:])