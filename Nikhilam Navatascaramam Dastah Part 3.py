def main(num1, num2):
    if num1 == 0 or num2 == 0:
        return 0

    if num1 == 1:
        return num2
    elif num2 == 1:
        return num1

    if num1 <= 5 and num2 <= 5:
        return multiple_table[num1][num2]

    if num2 < num1:
        num1, num2 = num2, num1

    base1 = int('1' + ('0' * len(str(num1))))
    base2 = int('1' + ('0' * (len(str(num2)) - 1)))

    if not base1 == base2:
        return 'Formula Not Applicable'

    if num1 % 10 == 0 or num2 % 10 == 0:
        return 'Formula Not Applicable'

    zeros = len(str(base1)) - 1

    right1 = base1 - num1
    right2 = num2 - base2

    left_ans = num1 + right2
    right_ans = main(right1, right2)

    if right_ans == 'Formula Not Applicable':
        return 'Formula Not Applicable'

    right_ans = base1 - int(right_ans)
    left_ans -= 1

    if right_ans < 0:
        return 'Formula Not Applicable'

    while len(str(right_ans)) < zeros:
        right_ans = '0' + str(right_ans)

    return int(str(left_ans) + str(right_ans))


# Hard-coded 5x5 multiplication table
multiple_table = [[0, 0, 0, 0, 0, 0],
                  [0, 1, 2, 3, 4, 5],
                  [0, 2, 4, 6, 8, 10],
                  [0, 3, 6, 9, 12, 15],
                  [0, 4, 8, 12, 16, 20],
                  [0, 5, 10, 15, 20, 25],
                  ]
