# 
L = [
	'A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','L','l','M','m',
	'Z','z','Y','y','X','x','W','w','V','v','U','u','T','t','S','s','R','r','Q','q','P','p','O','o','N','n'
	]
# 
def main():
	# 
	texto = input('\033[;33m'+'\n')
	# 
	if texto == 'exit' : pass
	# 
	else:
		# 
		texto_i = []
		# 
		for letra in texto:
			# 
		    if letra in L and L.index(letra) < (len(L)//2) : texto_i.append(L[L.index(letra)+26])
			# 
		    elif letra in L and L.index(letra) >= (len(L)//2) : texto_i.append(L[L.index(letra)-26])
		    # 
		    else : texto_i.append(letra)
	    # 
		print('\033[;32m'+''.join(texto_i))
		# 
		main()
# 
print('\033[;31m'+'Ingrese su texto: ')
# 
main()