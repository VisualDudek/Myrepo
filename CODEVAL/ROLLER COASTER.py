
test = 'To be, or not to be: that is the question.'

L = []
switch = True

for x in test:
    if x.isalpha() and switch:
        L.append(x.upper())
        switch = not switch
    elif x.isalpha() and not switch:
        L.append(x.lower())
        switch = not switch
    else:
        L.append(x)

print(''.join(L))

#Mozna uproscic

L = []
switch = True

for x in test:
    if x.isalpha():
        L.append([x.lower(), x.upper()][switch])
        switch = not switch
    else:
        L.append(x)

print(''.join(L))

# Czytelniejszy wariant

L = []
switch = True

for x in test:
    if x.isalpha():
        L.append(x.upper() if switch else x.lower())
        switch = not switch
    else:
        L.append(x)

print(''.join(L))