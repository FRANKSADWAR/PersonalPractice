import math
import sys
"""
Varous specialized string display formatting utilities. Test me with
canned self-test or command-line arguments
"""

def commas(N):
    """
    format positive integer-like N for display 
    with commas betweeb digit groupings: xxx, yyy.zz
    """
    digits = str(N) ### convert the input into a string
    assert(digits.isdigit()) ## will return true if the string is a digit string

    result = ''
    while digits: ## while the digits have not been split to the three
        digits, last3 = digits[:-3], digits[-3:] ## digits are the first numbers up to the 3 last ones, last3 are the last 3 digits
        result = (last3 + ',' + result) if result else last3
    return result

def money(N, width = 0):
    """
    format number N for display with commas, 2 decimal digits, a leading $ and sign, optional padding: $ 452,908.65
    """ 
    sign = '-' if N < 0 else '' ## a ternary operator that returns - if N is 0 
    N = abs(N)  ## conver the N to an absolute digit
    whole = commas(int(N))
    fract = ('%.2f' % N)[-2:]
    format = '%s%s.%s' % (sign, whole, fract)

    return '$%s%s' % (width, format)


if __name__ == "__main__":
    def selftest():
        tests = 0 , 1  # fails: -1, 1.23
        tests += 12, 123, 1234, 12345, 123456, 1234567
        tests += 2 ** 32, 2 ** 100

        for test in tests:
            print(commas(test))

        print('')
        tests = 0, 1, -1, 1.12, 1., 1.2, 3.14159
        tests += 12.34, 12.344, 12.245, 12.346
        tests += 2 ** 32, (2 ** 32 + .2345)
        tests += 1.2345, 1.2, 0.2345
        tests += -1.2345, -1.2, -0.2345
        tests += -(2 ** 32), -(2 **32 + .2345)
        tests += (2 ** 100), -(2 **100)

        for test in tests:
            print('%s [%s]' % (money(test,17), test))
    import sys
    if len(sys.argv) == 1:
        selftest()
    else:
        print(money(float(sys.argv[1]), int(sys.argv[2])))      ### sys.argv is used to represent command-line arguments  