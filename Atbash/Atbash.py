# Rules definition
lettersList = [
	'A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m',
	'Z','z','Y','y','X','x','W','w','V','v','U','u','T','t','S','s','R','r','Q','q','P','p','O','o','N','n'
	]

# Main function
def Atbash(text="Hello, World!"):
	convertedText = []
	for letter in text:
		# 
	    if letter in lettersList and lettersList.index(letter) < (len(lettersList)//2) : convertedText.append(lettersList[lettersList.index(letter)+26])
        # 
	    elif letter in lettersList and lettersList.index(letter) >= (len(lettersList)//2) : convertedText.append(lettersList[lettersList.index(letter)-26])
	    # 
	    else : convertedText.append(letter)
	return ''.join(convertedText)

