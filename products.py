products = []
while True:
	name = input('Please enter product\'s name: ')
	if name == 'q':
		break
	price = input('Please enter product\'s price: ')
	products.append([name, price])
print(products)

for p in products:
	print(p)
