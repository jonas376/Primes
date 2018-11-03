for numbers in range(1,2):
    firstNum = numbers*10 #00000000000000
    lastNum = numbers*10 + 500 #00000000000000+500
    prime = False
    winner = 'NONE'
    tie = 0
    me = 0
    them = 0
    for x in range(firstNum,lastNum):
        y = 2*x+1
        mine = myFactor(y)
        theirs = prime_factors(y)
        if mine[0] == 1:
            prime = True
        if mine[0] == theirs[0]:
            winner = 'TIE'
            tie = tie + 1
        elif mine[0] > theirs[0]:
            winner = 'THEM'
            me = me + 1
        else:
            winner = 'ME'
            them = them + 1


        with open('Contest.txt', 'a') as f:
        # print("Numbers from ",firstNum, "to", lastNum, "Time winners:", "Ties =", tie, "Me =", me, "Them =", them, file=f)
            print("Finding factors of ", y, ": ","myFactor says: ", mine[1],",",mine[2], "prime_factors says: ", theirs[1], file=f)
            print("Prime? ", prime, "myFactor time: ",mine[0],"prime_factor time: ", theirs[0], "Winner = ", winner, file=f )
            print("Time Difference = ", mine[0] - theirs[0], file=f)