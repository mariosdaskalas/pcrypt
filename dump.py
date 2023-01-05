import base64
import simple_colors

print(simple_colors.red("Welcome to prcrypt!", ['bold']))
print("Please choose one of the following options:")

print(simple_colors.green("Choice 1: Base64:"))
print(simple_colors.blue("Choice 2: Binary - Text:"))

choice = input()

if (choice == "1"):
    print("You choose Base64.")
    print("Please type if you want to 'encode' or 'decode...")

    encdec = input()

    # base64 encoding
    if (encdec == "encode"):
        print(simple_colors.red("You choose Encode...", ['bold']))
        print("Please type the text you want to encode...")

        base64txt = input()
        base64txt_byte = base64txt.encode("ascii")
        base64_byte = base64.b64encode(base64txt_byte)
        base64_final = base64_byte.decode("ascii")

        print(simple_colors.red("Result: " + base64_final, "bold"))

    # base64 decoding
    if (encdec == "decode"):
        print(simple_colors.red("You choose Decode...", ['bold']))
        print("Please type the text you want to decode...")

        base64txt = input()
        base64txt_byte = base64txt.encode("ascii")
        base64_byte = base64.b64decode(base64txt_byte)
        base64_final = base64_byte.decode("ascii")

        print(simple_colors.red("Result: " + base64_final, ['bold']))

if (choice == "2"):
    print(simple_colors.red("You choose Binary - Text.", ['bold']))
    print("Please type 'text' if you want to convert from 'text' to 'binary':")
    print("Please type 'binary' if you want to convert from 'binary' to 'text':")
    
    binary_input = input()

    if (binary_input == "text"):
        print("Give the text you want to convert...")

        txt = input()
        bin_decimal = ' '.join(format(ord(i), 'b') for i in txt)
        print(simple_colors.red("Result" + bin_decimal, ['bold']))

    if (binary_input == "binary"):
        print("Give the binary you want to convert...")

        txt = input()
        print("Nothing yet.")
        

    
