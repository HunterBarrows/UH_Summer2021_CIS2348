# Hunter Barrows 1550107

# Zylab 5.22 Automobile service invoice

# service menu
print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')
print()
menu1 = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7, 'Car wax': 12}

# user inputs service needed
Service1 = input('Select first service:\n')
Service2 = input('Select second service:\n')
print()

# Invoice
print('Davy\'s auto shop invoice\n')

if Service1 == '-':
    print('Service 1: No service')
    print('Service 2:', '{}, {}{}'.format(Service2, '$', menu1[Service2]))
    print()
    print('Total:', '{}{}'.format('$', menu1[Service2]))
elif Service2 == '-':
    print('Service 1:', '{}, {}{}'.format(Service1, '$', menu1[Service1]))
    print('Service 2: No service')
    print()
    print('Total:', '{}{}'.format('$', menu1[Service1]))
else:
    print('Service 1:', '{}, {}{}'.format(Service1, '$', menu1[Service1]))
    print('Service 2:', '{}, {}{}'.format(Service2, '$', menu1[Service2]))
    print()
    total = menu1[Service1] + menu1[Service2]
    print('Total:', '{}{}'.format('$', total))

