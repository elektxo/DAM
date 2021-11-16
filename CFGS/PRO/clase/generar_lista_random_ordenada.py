import random

lista=[]
for _ in range(10):
    lista+=[int(random.random() * 100)]

print(sorted(lista))
print(sorted(lista, reverse=True))