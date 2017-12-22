GenA = 699
GenB = 124

FactorA = 16807
FactorB = 48271

Div = 2147483647

Mask = int('1111111111111111', 2)
MaskA = int('11', 2)
MaskB = int('111', 2)

count = 0


for i in range (0, 5000000):
    while (GenA & MaskA) != 0:
        GenA = (GenA * FactorA) % Div
    while (GenB & MaskB) != 0:
        GenB = (GenB * FactorB) % Div
    if GenA & Mask == GenB & Mask:
        count += 1
    GenA = (GenA * FactorA) % Div
    GenB = (GenB * FactorB) % Div

print(count)