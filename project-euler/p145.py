total = 0

for exp in range(1,9):				# para los exponentes de 1 a 9
	if exp%2 == 1:					# si el exponente es impar
		n=20*int(30**((exp-1)/2 ))
	elif exp%4 == 2:				# si el exponente/4 tiene resto 2 (2,6,10...)
		n=100*int(500**((exp-2)/4))
	else:							# y si no..
		n = 0
	total+=n						# suma n al total

print(total)						# muestra el total




