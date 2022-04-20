fak = input('Введите название факультета: ')
slova = fak.split()
for i in range(len(slova)):
    slova[i] = slova[i][:3]
s = '.'.join(slova)
print(s)

a = '.'.join([a[:3] for a in input('Введите название факультета: ').split()])
print(a)