def main(num1, num2):
    '''
    This function can only divide with the numerator being
    1 and the denominator ending in 9.

    num1 is the numerator
    num2 is the denominator

    Note: The LENGTH of the denominator can't be greater than 2.
    '''
    answer = '1'
    to_carry = 0
    to_add = 0
    multiplier = int(str(num2)[0]) + 1
    half_way = num2 - num1

    if len(str(num2)) <= 2:
        if num1 == 1 and str(num2)[-1] == '9':
            # Run until we reach half way
            while (not (int(to_carry) == int(str(half_way)[0]) and int(to_add) == int(str(half_way)[1]))):
                to_add = (int(str(answer)[0]) * multiplier)
                to_add = (to_add) + int(to_carry)

                # Carry the first digit
                if len(str(to_add)) > 1:
                    to_carry = str(to_add)[:-1]
                    to_add = str(to_add)[1:]
                else:
                    to_carry = 0

                answer = str(to_add) + answer
                # If we get 1, the decimal will repeat, so we can stop
                if int(to_add) == 0 and int(to_carry) == 1:
                    return '0.' + answer + '...'

            # Once finished with half of the work, the rest can be derived
            # by subtracting the already obtained numbers by 9.
            answer = answer[1:]
            for i in range(len(answer)):
                answer = str((9 - int(answer[(-1 * i) - 1]))) + answer
        else:
            return None
        return '0.' + answer + '...'


num1 = 1
num2 = 19
print(main(num1, num2))
print(num1 / num2)
