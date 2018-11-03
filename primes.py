import matplotlib.pyplot as plt
import gc

# get prime list -- first 100k primes
text_file = open("primes100k.txt", "r")
lines = text_file.read()
b = lines.split('\n')
text_file.close()
b.remove('')
b = [int(i) for i in b]

# set range of numbers you want - starts at 1
myRange = 10000

# extract prime numbers less than or equal to your range
primes = [x for x in b if x <= myRange]


# Creating list array -- n is rows -- m is columns -- n x m
n = myRange
m = myRange
a = [[0] * m for i in range(n)]

# First column - all numbers 1 to myRange
for x in range(0,myRange):
    a[x][0] = x + 1


# Go through the primes and work the list
i = 0
for prime in primes:
    for x in range(0, myRange):
        if a[x][i] % prime != 0:
            a[x][i+1] = a[x][i]
    i = i + 1

# # Printing list
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print(a[i][j], end=' ')
#     print()

myCounts = []
for i in range(0,myRange):
    myCounts.append(sum(j > 0 for j in a[i]))

# plot
plt.plot(myCounts)


# # Second column - all numbers divisible by 2 are eliminated
#
#
#
# # Third column - all numbers divisible by 3 are eliminated
# for x in range(0,myRange):
#     if a[x][1] % 3 != 0:
#         a[x][2] = a[x][1]
#

#
#
#     else:
#         print(" ", end="", flush=True)
#
#
#
# print("X", end="", flush=True)
#  print("%d" % (x), end = "", flush=True)
# print()
# n = 3
# m = 4
# a = [[0] * m for i in range(n)]
# print("%d X" % (x))
# print "We're on time %d" % (x)
#
# print('.', end='', flush=True)



# plt.plot([1,2,3,4])
# plt.ylabel('some numbers')
# plt.show()