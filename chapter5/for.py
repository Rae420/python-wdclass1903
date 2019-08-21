states = ['Imo', 'Enugu', 'Abia', 'Ebonyi', 'Anambra']

for item in states:
    print(item)


# print in range
print(range(6))

for x in range(6):
    print(x)



# 2 x 1 = 2
# 2 x 2 = 4
# 2 x 3 = 6
# 2 x 4 = 8
# 2 x 5 = 10
# 2 x 6 = 12
# 2 x 7 = 14
# 2 x 8 = 16
# 2 x 9 = 18
# 2 x 10 = 20
# 2 x 11 = 22
# 2 x 12 = 24

# for x in range(1, 13):
#     print('2 x ',x, '=', 2*x)

# number = int(input('Enter number: '))

# for number in range(1, 13):
#     print(number, 'x',x, ' = ', number*x)



states = {
    'Imo':'Owerri',
    'Abia':'Umahia',
    'Enugu':'Enugu',
    'Jigawa':'Dutse',
}

for ky in states:
    print(ky, ' : ',states[ky])