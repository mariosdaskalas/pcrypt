import base64
import binascii
import base
import ascbin
import binoctal

print("Welcome to prcrypt!")
print("Please choose one of the following options:")

print("Choice 1: Base64:")
print("Choice 2: Binary - Text:")
print("Choice 3: Binary - Octal:")

choice = input()

if (choice == "1"):
    base.base64_function()
elif (choice == "2"):
    ascbin.ascbin_function()
elif (choice == "3"):
    binoctal.binoctal_function()
        