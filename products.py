import os # operating system

# read file
def read_file(filename):
	products = []
	with open(filename, 'r', encoding = 'utf-8') as f: #Check is file exist
		for line in f:
			if 'Product,Price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products

#Let user enter data
def user_input(products):
	while True:
		name = input('Please enter product\'s name: ')
		if name == 'q':
			break
		price = input('Please enter product\'s price: ')
		price = int(price)
		products.append([name, price])
	print(products)
	return products

#print all purchase records
def print_products(products):
	for p in products:
		print(p[0], 'price is', p[1])

#write in a file
def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('Product,Price\n')
		for p in products:
			f.write(str(p[0]) + ',' + str(p[1]) + '\n')


def main():
	filename = 'products.csv'
	if os.path.isfile(filename): #check if file exist
		print('yeah! Find file!')
		products = read_file(filename)
	else:
		print('No file found...')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)


main()
