## Manual Testing ##
num1 =
num2 =

try:
    ANS = main(num1, num2)
    print('ANSWER:  ', ANS)
    print('IS IT CORRECT?', int(ANS) == num1 * num2)
except RecursionError:
    print('ERROR: ', num1, 'x', num2)


## Exahaustive check for equations solved ##
count = 0
for i in range(10):
    for x in range(10):
        try:
            ANS = main(x, i)
            if ANS == 'Formula Not Applicable':
                pass
            elif not ANS == x * i:
                print('NOT EQUAL', x, 'x', i, ANS)
            else:
                count += 1
        except RecursionError:
            print('ERROR: ', x, 'x', i)

print(count, 'equations solved')
