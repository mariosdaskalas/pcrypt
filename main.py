import base64
import binascii
import base
import ascbin
import binoctal
import bindecimal
import binhexadecimal

print("Welcome to prcrypt!")
print("Please choose one of the following options:")

print("Choice 1: Base64:")
print("Choice 2: Binary - Text:")
print("Choice 3: Binary - Octal:")
print("Choice 4: Binary - Decimal:")
print("Choice 5: Binary - Hexadecimal:")
print("Choice 0: Terminate the program:")


choice = input()

if (choice == "0"):
    print("Ending...")
elif (choice == "1"):
    base.base64_function()
elif (choice == "2"):
    ascbin.ascbin_function()
elif (choice == "3"):
    binoctal.binoctal_function()
elif (choice == "4"):
    bindecimal.bindecimal_function()
elif (choice == "5"):
    binhexadecimal.binhex_function()
else:
    print("Invalid Choice...")
    print("Ending program...")