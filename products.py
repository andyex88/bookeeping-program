products = []
while True:
	name = input('Please enter product\'s name: ')
	if name == 'q':
		break
	price = input('Please enter product\'s price: ')
	price = int(price)
	products.append([name, price])
print(products)

for p in products:
	print(p[0], 'price is', p[1])

with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('Product,Price\n')
	for p in products:
		f.write(str(p[0]) + ',' + str(p[1]) + '\n')
