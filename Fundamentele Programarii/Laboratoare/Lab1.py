#Tema Laborator
from math import gcd
#Exercitiul 1
def primTest(number):
    if number < 2:
        return False
    else:
        for d in range(2, int(number/2)+1):
            if (number % d) == 0:
                return False

    return True


#print(primTest(5))

def toateNrPrime (number):
    ct = 0
    for idx in range(1, number):
        if primTest(idx) == True:
            print(idx)

toateNrPrime(11)

list1 = [17, 2, 5, 7, 9, 1, 19]

def celMailungSirCresc (list):
    ct = 1
    act = 1
    for idx in range(0, len(list) - 1):
        if list[idx] < list[idx+1]:
            ct = ct + 1
        else:
            ct = 1

        if ct > act:
            act = ct
    return act

def celMailungSirCresc2 (list):
    ct = []
    act = []
    for idx in range(len(list)):
        if not ct or list[idx] > ct[-1]:
            ct.append(list[idx])
        else:
            if len(ct) > len(act):
                act = ct
            ct = [list[idx]]
    if len(ct) > len(act):
        act = ct

    return act

#print(celMailungSirCresc(list1))
print(celMailungSirCresc2(list1))

#Exercitiul 12


def zahlen(number):
    list = []
    for nr in range(number):
        if gcd(nr, number) == 1:
            if primTest(nr) == True:
                list.append(nr)
    return list

print(zahlen(13))

def ceaMaiMareSuma (list):
    maxsecv = []
    secv = []
    maxsum = 0
    sum = 0
    for nr in list:
        if not secv or nr > secv[-1]:
            secv.append(nr)
            sum = sum + nr
        else:
            if sum > maxsum:
                maxsecv = secv
                maxsum = sum
            secv = [nr]
            sum = nr

    if sum > maxsum:
        maxsecv = secv
        maxsum = sum

    return maxsecv,maxsum


print(ceaMaiMareSuma([1, 30, 3, 7, 2, 9, 17]))