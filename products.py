import os # operating system

# read file
products = []
if os.path.isfile('products.csv'):
	print('yeah! Find file!')
	with open('products.csv', 'r', encoding = 'utf-8') as f: #Check is file exist
		for line in f:
			if 'Product,Price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('No file found...')

#Let user enter data
while True:
	name = input('Please enter product\'s name: ')
	if name == 'q':
		break
	price = input('Please enter product\'s price: ')
	price = int(price)
	products.append([name, price])
print(products)

#print all purchase records
for p in products:
	print(p[0], 'price is', p[1])

#write in a file
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('Product,Price\n')
	for p in products:
		f.write(str(p[0]) + ',' + str(p[1]) + '\n')
