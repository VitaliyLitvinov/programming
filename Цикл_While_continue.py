while True:
	string = str(input('Введите предложение: '))
	if len(string) < 5:
		print('Слищком мало.')
		continue
	elif len(string) <= 5:
		print('Символов достаточно')
		break