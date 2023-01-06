def bindecimal_function():
    print("You choose Binary - Decimal.")
    print("Please type 'binary' if you want to convert from 'binary' to 'decimal':")
    print("Please type 'decimal' if you want to convert from 'decimal' to 'binary':")

    binary_input = input()

    if (binary_input == "binary"):
        print("Give the binary value you want to convert...")

        txt = input()
        bin_txt = int(txt, 2)
        print(bin_txt)
    
    if (binary_input == "decimal"):
        print("Give the decimal value you want to convert...")

        txt = input()
        dec_txt = bin(int(txt))
        dec_txt = dec_txt[2:]
        print(dec_txt)