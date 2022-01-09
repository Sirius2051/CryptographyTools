# import sys

import EncryptionSystems.Atbash as Atbash
import EncryptionSystems.Bifido as Bifido
import EncryptionSystems.Blowfish as Blowfish
import EncryptionSystems.Cesar as Cesar
import EncryptionSystems.ChaffingAndWinnowing as ChaffingAndWinnowing
import EncryptionSystems.DES as DES
import EncryptionSystems.Exponential as Exponential
import EncryptionSystems.Gronsfeld as Gronsfeld
import EncryptionSystems.RSA as RSA
import EncryptionSystems.Skipjack as Skipjack

class CryptographyTool:
	def __init__(self):
		self.Atbash = Atbash.Atbash()
		self.Bifido = Bifido.Bifido()
		self.Blowfish = Blowfish.Blowfish()
		self.Cesar = Cesar.Cesar()
		self.ChaffingAndWinnowing = ChaffingAndWinnowing.ChaffingAndWinnowing()
		self.DES = DES.DES()
		self.Exponential = Exponential.Exponential()
		self.Gronsfeld = Gronsfeld.Gronsfeld()
		self.RSA = RSA.RSA()
		self.Skipjack = Skipjack.Skipjack()
		self.EncryptionSystems = [
			self.Atbash,
			self.Bifido,
			self.Blowfish,
			self.Cesar,
			self.ChaffingAndWinnowing,
			self.DES,
			self.Exponential,
			self.Gronsfeld,
			self.RSA,
			self.Skipjack,
		]
	
	def Main(self):
		self.SystemSelector()
		self.ConvertionProcess(self.encryption_system)
		print("\033[0;37m" + self.encrypted_text)

	def SystemSelector(self):
		try:
			self.encryption_system = int(input("\033[0;35mSelect the encryption system you want to use: "))
			if self.encryption_system in range(0, 10):
				print(type(self.EncryptionSystems[self.encryption_system]).__name__ + " Selected!")
		except:
			print("Incorrect option \n")
			self.SystemSelector()
	
	def ConvertionProcess(self, index):
		text = input("\033[0;35mInsert the text to encrypt: ")
		if len(text) > 0:
			self.encrypted_text = self.EncryptionSystems[index].Convertion(text)
		else:
			self.ConvertionProcess(self.encryption_system)

print("""
\033[1;33m
-------------------------------------------------------------------------------
\033[1;32m
        _____                  _                              _           
       / ____|                | |                            | |          
      | |     _ __ _   _ _ __ | |_ ___   __ _ _ __ __ _ _ __ | |__  _   _ 
      | |    | '__| | | | '_ \| __/ _ \ / _` | '__/ _` | '_ \| '_ \| | | |
      | |____| |  | |_| | |_) | || (_) | (_| | | | (_| | |_) | | | | |_| |
       \_____|_|   \__, | .__/ \__\___/ \__, |_|  \__,_| .__/|_| |_|\__, |
                    __/ | |              __/ |         | |           __/ |
                   |___/|_|             |___/          |_|          |___/ 
                               _______          _ 
                              |__   __|        | |
                                 | | ___   ___ | |
                                 | |/ _ \ / _ \| |
                                 | | (_) | (_) | |
                                 |_|\___/ \___/|_|
\033[1;33m
-------------------------------------------------------------------------------
\033[0;37m
The encryption systems available are:

0) Atbash
1) Bifido
2) Blowfish
3) Cesar
4) ChaffingAndWinnowing
5) DES
6) Exponential
7) Gronsfeld
8) RSA
9) Skipjack
""")

cryptography_tool = CryptographyTool()

cryptography_tool.Main()

# if sys.argv[1] != False and sys.argv[1] == "--gui":
	# print("Starting graphical interface... \n")