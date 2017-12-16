GenA = 699
GenB = 124

FactorA = 16807
FactorB = 48271

Div = 2147483647

Mask = int('1111111111111111', 2)

count = 0

for i in range (0, 40000000):
    GenA = (GenA * FactorA) % Div
    GenB = (GenB * FactorB) % Div
    if GenA & Mask == GenB & Mask:
        count += 1

print(count)