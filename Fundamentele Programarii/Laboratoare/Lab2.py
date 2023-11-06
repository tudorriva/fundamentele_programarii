l = [1, 4, 7, 9, 10, 1, 4, 10 ]
strng = "1479101410"
ls = [12, 34, 45, 59, 23, 44, 41]
import sys
# Ubung 1
def repeatedNum (list):
    new_list = []
    for idx in range(0, len(list)):
        ct = 1
        for jdx in range(idx, len(list)):
            if list[jdx] == list[idx] or list[idx] not in new_list:
                ct = ct + 1
                if ct > 1 and list[jdx] not in new_list:
                    new_list.append(list[idx])
                    break
                else:
                    if ct == 1:
                        new_list.append(list[idx])
    return new_list

#Ubung 2
def sym_numbers(list):
    pairs = []
    for idx in range(len(list)):
        for jdx in range(idx+1, len(list)):
            if str(list[idx])[::-1] == str(list[jdx]): #in string ca sa pot sa il inversez usor
                pairs.append((list[idx], list[jdx]))
    return pairs

#Ubung 3

def sort(list):
    i=0
    for idx in range (i , len(list)):
        for jdx in range (i+1 , len(list)):
            if(list[idx] < list[jdx]):
                list[idx], list[jdx] = list[jdx], list[idx]
        i += 1
    return list

def biggestNumber (list):
    sorted_list = sort(list)
    string =  ''.join(map(str,sorted_list))
    return string

    return str
print(sort([4,5,76,77,4,3,3,2,55,7]))
print(biggestNumber([4,5,76,77,4,3,3,2,55,7]))

#Ubung 4

def decrypt(list):
    new_list = []
    for number in list:
        new_number = (number//10)
        new_list.append(new_number)

    return new_list

def encrypt (list):
    new_list = []
    old_list = []
    first_nr = list[0]
    for number in list:
        new_number = (number * 10) + first_nr
        new_list.append(new_number)

    #old_list = decrypt(new_list)

    return new_list  #, old_list
#Ubung 5
def nrRelation (string, list):
    for idx in range(len(list)):
        for jdx in range(idx, len(list)):
            x,y = list[idx], list[jdx]
            if eval(string):
                return x,y


#Ubung 6
def dominoSeq (list):
    acc_list = []
    max_list = []
    ct = 0
    max_ct = 0
    for idx in range(len(list)):
        nr1 = list[idx]
        for jdx in range(idx, len(list)):
            nr2 = list[jdx]
            if nr1%10 == nr2//10:
                ct = ct + 1
                acc_list.append(nr2)
                nr1 = nr2
            else:
                ct = 0
                acc_list = [nr2]

            if ct>max_ct:
                max_ct = ct
                max_list = acc_list

    return max_list

def lcm(a, b):
    if a > b:
        gr = a
    else:
        gr = b

    while(True):
        if gr % a == 0 and gr % b == 0:
            lcm = gr
            break
        gr = gr + 1

    return lcm
def min_lcm(list, x1, x2): #ls = [12, 34, 45, 59, 23, 44, 41]
    aux_lcm = 0
    lcmm = 0
    (a, b) = 0, 0
    (ma, mb) = 0, 0
    if x1 < len(list) and x2 < len(list):
        for idx in range(x1, x2):
            if aux_lcm == 0:
                aux_lcm = lcm(list[idx], list[idx+1])
            else:
                aux_lcm = lcm(aux_lcm, list[idx+1])

    return aux_lcm


#print(repeatedNum([1, 4, 7, 9, 10, 1, 4, 10 ]))
#print(sym_numbers([12, 23, 45, 26, 21, 54, 45]))
#print(encrypt(l))
#print(nrRelation("x==y*3", [23, 44, 93, 51, 75, 33]))
#print(dominoSeq(ls)) #ls = [12, 34, 45, 59, 23, 44, 41]
print(min_lcm([12, 24, 48, 59, 23, 44, 41], 0, 2))