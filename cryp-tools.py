import sys
import Atbash.Atbash as Atbash

if sys.argv[1] == "--gui":
	print("Starting graphical interface... \n")

print("Select the encryption system you will use.")

encryption_system = input("\n")
text = input("Insert the text to encrypt: ")

encrypted_text = Atbash.Atbash(text)

print(encrypted_text)


# 