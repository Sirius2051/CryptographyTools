class Cesar:
	def __init__(self):
		self.rules = [
			'A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m',
			'N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V','v','W','w','X','x','Y','y','Z','z'
		]

	def Convertion(self, text):
		self.converted_text = []
		for letter in text:
			if letter in self.rules:
				try:
					self.converted_text.append(self.rules[self.rules.index(letter) + 6])
				except:
					self.converted_text.append(self.rules[self.rules.index(letter) + 6 - len(self.rules)])
			else:
				self.converted_text.append(letter)
		return ''.join(self.converted_text)
