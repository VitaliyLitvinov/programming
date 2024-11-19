guess = 10
running = True

while True:
	string = input('введите предложение: ')
	if string == 'выход':
		print('конец программы')
		break
	print('количество символов в предложении: ', len(string))
