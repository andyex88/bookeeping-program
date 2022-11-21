products = []
while True:
	name = input('Please enter product\'s name: ')
	if name == 'q':
		break
	price = input('Please enter product\'s price: ')
	products.append([name, price])
print(products)

for p in products:
	print(p[0], 'price is', p[1])

with open('products.csv', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
