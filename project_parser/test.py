el1 = 1
el2 = 1
n = 10
print(el1)
print(el2)
for _ in range(n-2):
    el2, el1 = (el1 + el2), el2
    print(el2)
