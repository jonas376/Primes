import math
import datetime

def myNumber(x):
    #### Setup Phase
    startTime = datetime.datetime.now()

    sqrtCheck = math.sqrt(x)

    y = math.floor(sqrtCheck) + 1

    z = y ** 2 - x

    v = math.floor(math.sqrt(z))

    w = v + 1

    s = z - v ** 2

    t = 2 * w - 1

    C = 2 * y - 1


    ##############
    if sqrtCheck.is_integer():
        a = int(sqrtCheck)
        b = 0
    elif s == 0:
        a = y
        b = v
    else:
        while s != t:

            if s > t:
                s = s - t
                t = t + 2

            else:
                C = C + 2
                L = t - s
                s = C - L
                t = t + 2
        a = round((C + 1) / 2)

        b = round((t + 1) / 2)



    endTime = datetime.datetime.now()

    timePassed = endTime - startTime

    print(a - b, a + b)

    print(str(timePassed))
# ex. 69522569 - eight digit
# ex. 163508473 - nine digit
# ex.1000000007 - ten digit
# ex.5772173207 - ten digit composite
# ex.10000169 - eight digit
# ex. 100123456789 - twelve digit
# ex. 1000000000000037 - sixteen digit
# ex. 11367529096227137 - 17 digit composite two primes
# ex. 10093100991010310111 - twenty digit
# ex. 18446744073709551617  - twenty digit composite
# ex. 26672757247744730197  - twenty digit composite
# 74747474747474747 div by zero error prime