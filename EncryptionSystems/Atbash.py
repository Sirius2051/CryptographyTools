class Atbash:
	def __init__(self):
		self.rules = [
			'A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m',
			'Z','z','Y','y','X','x','W','w','V','v','U','u','T','t','S','s','R','r','Q','q','P','p','O','o','N','n'
		]

	def Convertion(self, text):
		self.converted_text = []
		for letter in text:
			# 
			if letter in self.rules and self.rules.index(letter) < (len(self.rules)//2): 
				self.converted_text.append(self.rules[self.rules.index(letter)+26])
			# 
			elif letter in self.rules and self.rules.index(letter) >= (len(self.rules)//2): 
				self.converted_text.append(self.rules[self.rules.index(letter)-26])
			# 
			else:
				self.converted_text.append(letter)
		return ''.join(self.converted_text)
