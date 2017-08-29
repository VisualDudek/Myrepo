
test = 'zero;two;five;seven;eight;four'

d = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}

print(''.join([d[x] for x in test.split(';')]))