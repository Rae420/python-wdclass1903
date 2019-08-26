def add_range(start, stop=20):
    start += 1
    total = 0
    
    while start <= stop:
        total += start
        start += 1
    print(total)
    
states = {
    'Imo':'Owerri',
    'Abia':'Umahia',
    'Enugu':'Enugu',
    'Jigawa':'Dutse',
}   