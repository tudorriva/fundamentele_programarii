from math import gcd
import time

def add(a, b):
    return simplify((a[0] * b[1] + b[0] * a[1], a[1] * b[1]))

def sub(a,b):
    return simplify((a[0] * b[1] - b[0] * a[1], a[1] * b[1]))

def mul(a,b):
    return simplify((a[0] * b[0], a[1] * b[1]))

def div(a,b):
    return simplify((a[0] * b[1], a[1] * b[0]))

def simplify(frac):
    g = gcd (frac[0], frac[1])
    return frac[0]//g, frac[1]//g


def add_frac(fracs, frac):
    fracs.append(frac)

def del_fracs(fracs, frac):
    fracs.remove(frac)

def sum_fracs(fracs):
    sum = (0, 1)

    for frac in fracs:
        sum = add(sum, frac)

    return sum

def test_simplify():
    assert simplify((20, 12)) == (5,3)

def test_sub():
    assert sub((5, 6), (2,3)) == (1, 6)
def test_sum():
    assert  sum_fracs([(1, 2), (2, 3), (1, 2)]) == (5, 3)

def test_mul():
    assert mul((2,4), (2,2)) == (1,2)
def test_add():
    assert add((1,2), (2,3)) == (7, 6)
    assert add((1,2), (1,2)) == (1, 1)

def test_div():
    assert div((2,3),(1,2)) == (4,3)

def menu():
    return """
        1 - add frac to list
        2 - remove frac from list
        3 - add 2 fracs
        4 - sub 2 fracs
        5 - multiply 2 fracs
        6 - divide 2 fracs
        7 - calculate sum
        0 - exit
        """
def main():
    fracs = []
    while True:
        print(menu())

        opt = int(input('opt='))
        if opt == 1:
            n = int(input('n='))
            m = int(input('m='))

            add_frac(fracs, (n, m))

        if opt == 2:
            n = int(input('n='))
            m = int(input('m='))
            del_fracs((n,m))

        if opt == 3:
            n = int(input('first frac (idx) = '))
            m = int(input('second frac (idx) = '))
            (a, b) = fracs[n]
            (c, d) = fracs[m]

            print(add((a, b),(c, d)))
            time.sleep(3)

        if opt == 4:
            n = int(input('first frac (idx) = '))
            m = int(input('second frac (idx) = '))
            (a, b) = fracs[n]
            (c, d) = fracs[m]

            print(sub((a, b), (c, d)))
            time.sleep(3)

        if opt == 5:
            n = int(input('first frac (idx) = '))
            m = int(input('second frac (idx) = '))
            (a, b) = fracs[n]
            (c, d) = fracs[m]

            print(mul((a, b), (c, d)))
            time.sleep(3)

        if opt == 6:
            n = int(input('first frac (idx) = '))
            m = int(input('second frac (idx) = '))
            (a, b) = fracs[n]
            (c, d) = fracs[m]

            print(div((a, b), (c, d)))
            time.sleep(3)

        if opt == 7:
            n, m = sum_fracs(fracs)
            print('sum = ', (n, m))
            time.sleep(3)

        if opt == 0:
            break


test_div()
test_mul()
test_sub()
test_simplify()
test_sum()
test_add()
main()