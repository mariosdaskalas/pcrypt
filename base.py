import base64

def base64_function():
    print("You choose Base64.")
    print("Please type if you want to 'encode' or 'decode...")

    encdec = input()

    # base64 encoding
    if (encdec == "encode"):
        print("You choose Encode...")
        print("Please type the text you want to encode...")

        base64txt = input()
        base64txt_byte = base64txt.encode("ascii")
        base64_byte = base64.b64encode(base64txt_byte)
        base64_final = base64_byte.decode("ascii")

        print("Result: " + base64_final)

    # base64 decoding
    if (encdec == "decode"):
        print("You choose Decode...")
        print("Please type the text you want to decode...")

        base64txt = input()
        base64txt_byte = base64txt.encode("ascii")
        base64_byte = base64.b64decode(base64txt_byte)
        base64_final = base64_byte.decode("ascii")

        print("Result: " + base64_final)