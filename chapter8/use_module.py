import module1

module1.add_range(1, 40)

for state in module1.states:
    print(module1.states[state])
    
# for statei module1.states.values():
#     print(state)


emp1 = module1.Employee('Benedict', 'Uwazie', 3000)

# print (type(emp1))
print(emp1.salary())