import math
import datetime
import decimal

def myFactor(x):
    #### Setup Phase
    startTime = datetime.datetime.now()
    decimal.getcontext().prec = 30  # try to use more than the number of digits of given number
    sqrtCheck = decimal.Decimal(x).sqrt()
    intPart = decimal.Decimal(sqrtCheck).to_integral(rounding = 'ROUND_FLOOR')
    issqrt = sqrtCheck == intPart
    y = int(intPart) + 1
    z = y ** 2 - x
    v = int(decimal.Decimal(decimal.Decimal(z).sqrt()).to_integral(rounding = 'ROUND_FLOOR'))
    w = v + 1
    s = z - v ** 2
    t = 2 * w - 1
    C = 2 * y - 1
    counter = 0

    ##############
    if issqrt:
        a = int(intPart)
        b = 0

    elif s == 0:
        a = y
        b = v

    else:

        while s != t:

            if s > t:
                s = s - t
                t = t + 2
                counter = 0

            else:
                if counter == 0:
                    C = C + 2
                    L = t - s
                    s = C - L
                    t = t + 2
                    counter = counter + 1

                else:
                    M = t - s
                    Diff = L - M
                    N = int(math.ceil(L/Diff))-1
                    C = C + 2*N
                    s = C - (L - Diff*N)
                    t = t + 2*N
                    counter = 0



        a = round((C + 1) / 2)

        b = round((t + 1) / 2)



    endTime = datetime.datetime.now()

    timePassed = endTime - startTime
    return str(timePassed), a - b, a + b
