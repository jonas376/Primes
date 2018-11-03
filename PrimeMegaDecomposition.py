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
    #sqrtCheck = math.sqrt(x)
    y = int(intPart) + 1

    z = y ** 2 - x

    #v = math.floor(math.sqrt(z))
    v = int(decimal.Decimal(decimal.Decimal(z).sqrt()).to_integral(rounding = 'ROUND_FLOOR'))
    w = v + 1

    s = z - v ** 2

    t = 2 * w - 1

    C = 2 * y - 1

    counter = 0

    # Diff = 0
    #
    #
    #
    # fCounter = 0
    #
    # fData = []
    #
    # position = 0
    #
    # tGreater = 0
    #
    # sGreaterOnce = 0
    #
    # sGreaterMany = 0
    #
    # n = 0

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
                # n = math.ceil(((-t-1) + math.sqrt(t**2 - 2*t + 4*s + 1))/2)
                # t = t + 2*n
                # s = s - t*n - n(n+1) + 2*n
                s = s - t
                t = t + 2
                counter = 0
                # tGreater = tGreater + 1
                # fCounter = fCounter + 1

            else:
                # fData.append(fCounter)
                fCounter = 0
                if counter == 0:
                    C = C + 2
                    L = t - s
                    s = C - L
                    t = t + 2
                    counter = counter + 1
                    # sGreaterOnce = sGreaterOnce + 1
                else:
                    M = t - s
                    Diff = L - M
                    N = int(math.ceil(L/Diff))-1
                    C = C + 2*N
                    s = C - (L - Diff*N)
                    t = t + 2*N
                    counter = 0
                    # sGreaterMany = sGreaterMany + 1


            # position = position + 1
            # print(position)
            # print(C,s,t,Diff, counter)

        a = round((C + 1) / 2)

        b = round((t + 1) / 2)



    endTime = datetime.datetime.now()

    timePassed = endTime - startTime
    return str(timePassed), a - b, a + b
    # return fData,str(timePassed), a-b, a+b
    # with open('fCount.txt', 'w') as f:
    #     print(fData,str(timePassed), a-b, a+b, file=f)

    # print("Factors of ", x, ":")
    #
    # print(a - b, a + b)
    #
    # print("t > s =", tGreater,",", "s > t once = ", sGreaterOnce,",", "s > t many = ", sGreaterMany)
    #
    # print(str(timePassed))

# for x in range(200):
#     myFactor(2*x+1)

# with open('file.txt', 'w') as f:
#     print('hello world', file=f)
#
# with open('file.txt', 'a') as f:
#     print('hello world', file=f)