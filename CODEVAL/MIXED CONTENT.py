
test = '8,33,21,0,16,50,37,0,melon,7,apricot,peach,pineapple,17,21'
# test = '8,33,21,0,16,50,37,0'

word_list = []
numbers_list = []

for x in test.rstrip().split(','):
    if x.isdigit():
        numbers_list.append(x)
    else:
        word_list.append(x)


# wywala sie w przypadku samych slow lub samych liczb
# print(','.join(word_list) + '|' + ','.join(numbers_list))

if len(word_list) == 0 or len(numbers_list) == 0:
    print(','.join(word_list) + '' + ','.join(numbers_list)) # UWAGA może byc bez ''
else:
    print(','.join(word_list) + '|' + ','.join(numbers_list))

# uproszczenie karkolomne ale zawsze cos
print(','.join(word_list) + str(['','|'][len(word_list) * len(numbers_list) > 0]) + ','.join(numbers_list))


print('------------------------')# Uproszczenie poprzez .sort()

L = test.split(',')

d = { key:(value+len(L) if key.isdigit() else value) for value,key in enumerate(L)}   # EVERNOTE/ANKI

print(sorted(d.items(), key = lambda x: x[1] ))  # Jak zapisać żeby na OUT były tylko keys???

print(','.join( [ x[0] for x in sorted(d.items(), key = lambda x: x[1] ) ] ))

# Nadal brakuje '|'
