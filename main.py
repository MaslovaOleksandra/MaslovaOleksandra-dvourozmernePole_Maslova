import random

pole = []

for i in range(3):
    radek = []
    for j in range(3):
        radek.append(random.randint(1, 10))
    pole.append(radek)

print(pole)
