# CS6352 project 1
# Zheheng Zhao
# zxz163930

import random
import numpy as np
import matplotlib.pyplot as plt
import rv
from event import Event
from event import EventList

m = 2.0
K = 4

mu = 3.0

# def isblock():
#     prob = random.random()
#     if prob < 0.5:
#         return True
#     else:
#         return False


def simulation(rho):
    #define arrival with 1, departure with 0
    lam = rho * m * mu
    #print lam
    clock = 0.0
    N = 0.0
    Narr = 0
    Nblock = 0
    Njob = 0
    Ndep = 0
    EN = 0.0
    U = 0.0

    p = np.zeros(2 * K + 1)

    p[0] = 1

    for i in range(1, K + 1):
        p[i] = (lam / mu) * p[i-1]
    
    for i in range(K + 1, 2 * K + 1):
        p[i] = (1.0 / 4) * (lam / mu) * p[i-1]

    sum = 0.0
    for i in range(2 * K + 1):
        sum += p[i]

    for i in range(2 * K + 1):
        p[i] /= sum

    En_the = 0.0
    for i in range(2 * K + 1):
        En_the += i * p[i]

    Tao_the = 0.0
    Bprob_the = 0.0
    lam_avg = 0.0
    for i in range(0, K):
        lam_avg += lam * p[i]
    
    for i in range(K, 2 * K):
        lam_avg += 0.5 * lam * p[i]

    Bprob_the = p[-1] * 0.5 * lam / (lam_avg + 0.5 * lam * p[-1])
    Tao_the = En_the / lam_avg

    U_the = 0.0
    for i in range(1, K + 1):
        U_the += 0.5 * p[i]
    
    for i in range(K + 1, 2 * K + 1):
        U_the += 1.0 * p[i]

    done = False

    Elist = EventList(0, 0)
    Elist.insert(rv.exp_rv(lam), 1)

    while not done:
        #print str(N) + ' ' + str(Nblock)
        CurrentEvent = Elist.get()
        prev = clock
        #print prev
        clock = CurrentEvent.time
        EN += N * (clock - prev)
        #print clock
        #print CurrentEvent.kind
        if N > K:
            U += (clock - prev)
        else:
            U += (1.0 / m) * (clock - prev) 

        if CurrentEvent.kind == 1:
            Narr += 1
            #EN += N * (clock - prev)
            if N < K:
                N += 1
                Njob += 1
                Elist.insert(clock + rv.exp_rv(lam), 1)
                if N == 1:
                    Elist.insert(clock + rv.exp_rv(mu), 0)
            elif N >= K and N < (2 * K):
                N += 1
                Njob += 1
                Elist.insert(clock + rv.exp_rv(0.5 * lam), 1)
            elif N >= (2 * K):
                Nblock += 1
                Elist.insert(clock + rv.exp_rv(0.5 * lam), 1)
        elif CurrentEvent.kind == 0:
            N -= 1
            Ndep += 1
            if N > 0:
                if N <= K:
                    Elist.insert(clock + rv.exp_rv(mu), 0)
                else:
                    Elist.insert(clock + rv.exp_rv(2.0 * mu), 0)
        del CurrentEvent
        if Ndep > 100000:
            done = True

    del Elist
    #print str(EN) + ' ' + str(clock)
    #print 'Current number of customers in system: ' + str(N)
    print 'Expected number of customers (simulation): ' + str(EN / clock)
    print 'Expected number of customers (theoretical): ' + str(En_the)
    print 'Expected time for each request spend in the sytem (simulation): ' + str(EN / Njob)
    print 'Expected time for each request spend in the sytem (theoretical): ' + str(Tao_the)
    print 'Block probalibity is (simulation): ' + str(1.0 * Nblock / Narr)
    print 'Block probalibity is (theoretical): ' + str(Bprob_the)
    print 'Total utilization of the system (simulation): ' + str(U / clock)
    print 'Total utilization of the system (theoretical): ' + str(U_the)
    
    return (EN / clock), (EN / Njob), (1.0 * Nblock / Narr), (U / clock), En_the, Tao_the, Bprob_the, U_the


En = np.zeros(10)
Tao = np.zeros(10)
Bprob = np.zeros(10)
util = np.zeros(10)
En_the = np.zeros(10)
Tao_the = np.zeros(10)
Bprob_the = np.zeros(10)
U_the = np.zeros(10)
for i in range(10):
    En[i], Tao[i], Bprob[i], util[i], En_the[i], Tao_the[i], Bprob_the[i], U_the[i] = simulation((i + 1) / 10.0)

print Bprob
p = np.array([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])

f = plt.figure()

plt.subplot(221)
plt.plot(p, En, p, En_the)
plt.title('En: blue--sim red--the')
plt.grid(True)

plt.subplot(222)
plt.plot(p, Tao, p, Tao_the)
plt.title('Average time: blue--sim red--the')
plt.grid(True)

plt.subplot(223)
plt.plot(p, Bprob, p, Bprob_the)
plt.title('Block probability: blue--sim red--the')
plt.grid(True)

plt.subplot(224)
plt.plot(p, util, p, U_the)
plt.title('Utilization: blue--sim red--the')
plt.grid(True)

plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                    wspace=0.35)

plt.show()

f.savefig("result.pdf", bbox_inches = 'tight')

# import random
# import numpy as np
# import matplotlib.pyplot as plt
# import rv
# from event import Event
# from event import EventList

# def simulation():
#     #define arrival with 1, departure with 0
#     lam = 0.8
#     mu = 1.0
#     #print lam
#     clock = 0.0
#     N = 0
#     Ndep = 0
#     EN = 0.0

#     done = False

#     Elist = EventList(0, 0)
    
    

#     while not done:
#         if N == 0:
#             Elist.insert(clock + rv.exp_rv(lam), 1)
#         #print str(N) + ' ' + str(Nblock)
#         CurrentEvent = Elist.get()
#         prev = clock
#         #print prev
#         clock = CurrentEvent.time

#         if CurrentEvent.kind == 1:
#             EN += N * (clock - prev)
#             N += 1
#             Elist.insert(clock + rv.exp_rv(lam), 1)
#             if N == 1:
#                 Elist.insert(clock + rv.exp_rv(mu), 0)
#         elif CurrentEvent.kind == 0:
#             EN += N * (clock - prev)
#             N -= 1
#             Ndep += 1
#             if N > 0:
#                 Elist.insert(clock + rv.exp_rv(mu), 0)
#         del CurrentEvent
#         if Ndep > 100000:
#             done = True

#     del Elist
#     rho = lam / mu
#     #print 'Current number of customers in system: ' + str(N)
#     print 'Expected number of customers (simulation): ' + str(EN / clock)
#     print 'Expected time for each request spend in the sytem (simulation): ' + str(rho / (1-rho))

# simulation()