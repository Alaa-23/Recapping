def multiplex(y):
    
    i = 0
    lista = []
    while i < y:
        new = yield i
        lista.append(new)
        i += 1    
    print(lista) 

multiplex(11)