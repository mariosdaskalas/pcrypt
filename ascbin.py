def ascbin_function():
    print("You choose Binary - Text.")
    print("Please type 'text' if you want to convert from 'text' to 'binary':")
    print("Please type 'binary' if you want to convert from 'binary' to 'text':")
    
    binary_input = input()

    if (binary_input == "text"):
        print("Give the text you want to convert...")

        txt = input()
        bin_decimal = ' '.join(format(ord(i), 'b') for i in txt)
        print("Result: " + bin_decimal)

    if (binary_input == "binary"):
        print("Give the binary you want to convert...")

        txt = input()
        bin_values = txt.split()
        ascii_str = ""
        for bin_value in bin_values:
            integer_val = int(bin_value, 2)
            ascii_char = chr(integer_val)
            ascii_str = ascii_str + ascii_char

        print(ascii_str)