# Newlines
# Create string with three sets of quotes to escape newlines in string
print('''Hello
    World''')

# In-place Operators + - | ^ & / >> % // **
x=2
x += 3
print(x)

x=7
x %= 5
print(x)

# Comparison => bez znaczenia (float or int)
# <= or >= moża także używać do Str
print(7 > 7.0)

# KALKULATOR ------------
while True:
    print('''
    Opcje:
    Enter "add"
    Enter "multiply"
    Enter "quit"''')
    user_input = input('--> ')

    if user_input == 'quit':
        break
    elif user_input == 'add':
        num1 = float(input('1th number --> '))
        num2 = float(input('2th number --> '))
        print('Result: ' + str(num1 + num2) )
    elif user_input == 'multiply':
        print()
    else:
        print('Unknow input')
