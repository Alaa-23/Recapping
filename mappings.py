from random import randint as randomized



lista = []

choosing = str(input("(R)andomized or (i)nput? "))

y = 0
if choosing in ['i','I','input']:
    while y < 5:
        user_input = int(input ("Enter Random --> "))
        lista.append(user_input)
        y = y+1

elif choosing in ['None','','r','R','Randomized']:
    while y < 5:
        lista.append(randomized)
        y = y+1

def add_one(x):
    return x+1
#Usage of maps here
result = list(map(add_one,lista))

print('\n',result)

z = 0
def filteration(z):
    if z == 1:
       return False
    else:
        return True

#Usage of filters here
filtered = list(filter(filteration,result))
print(filtered)
