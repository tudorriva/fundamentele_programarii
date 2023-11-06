def add(x, y):
    return x + y


add(3, 4)
#print(add(3, 4)) #3,4 parametrii actuali
a = 3
b = 4
#print(add(a, b)) #a, b parametrii formali


#d = {'a':1, 'b':2}
#print('first elem', d['a'])
#print('second elem', d['b'])
#print('length', len(d))
#d['c'] = 5
#print('third elem', d['c'])
#print('length', len(d))
#for key in d:
#    print(key, d[key])



#Ubungen

#1

def countr_to_dict(word):
    d = {}

    for char in word:
        ct = 0
        for other_ch in word:
            if char == other_ch:
                ct = ct + 1
        d[char] = ct

    return d

#print(countr_to_dict('sochool'))

def countr_to_dict2(word):
    d = {}

    for char in word:
        if char in d:
            d[char] = d[char] + 1
        else:
            d[char] = 1

    return d

#print(countr_to_dict2('sochool'))

""""
l = [1,2,3]
print(1 in l) --> True O(n)

d = {1:'s', 2:'b'}
print(1 in d) --> True approx O(1)
"""

def add_tags(char, word):
    return '<' + char + '> ' + word + ' </' + char + '>'

#print(add_tags('i', 'Python'))

def palindrom(word):

    for idx in range(len(word)//2):
        if word[idx] != word[- idx - 1]:
            return False
    return True

#print(palindrom('anna'))
#print(palindrom('aba'))
#print(palindrom('qwerewq'))
#print(palindrom('abc'))

word = 'anna'
#print(word[0:2]) # primele 2 elemente din word
word = 'anba'
#print(word[0:len(word):2]) # din 2 in 2 elemente
#print(word[::-1]) # scrie invers
#print(word[::-1] == word) # test palindrom simplu

def calcul_n_fact(numere):
    s = 1
    for i in range(1, numere+1):
        s = s * i
    return s

print(calcul_n_fact(5))

def count_uniqe (word):
    counts = countr_to_dict2(word)
    ct = 0
    for key in counts:
        if counts[key] == 1:
            ct = ct + 1
    return ct

print(count_uniqe('school'))

def words_anagram (word1, word2):
    for char in word1:
        if len(word1) != len(word2):
            return False
        if char not in word2:
            return False
    for char in word2:
        if len(word1) != len(word2):
            return False
        if char not in word1:
            return False
    return True

#print(words_anagram('anna','annb'))
#print(words_anagram('abcd', 'efgh'))
#print(words_anagram('abc', 'bbca'))

def encrypt(word, shift):
    new_word = ''
    for idx in range(len(word)):
        char = ord(word[idx])
        new_word = new_word + chr(char + 3)
    return new_word

print(encrypt('string', 3))


def str_find(target, source):
    if source in target:
        return True
    else:
        return -1

#print(str_find('targeting', 'abc'))

#12

nr = 2