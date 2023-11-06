

def is_perfnr (number):
    suma = 0
    for d in range(1, (number//2) + 1):
        if number % d == 0:
            suma = suma + d
    return number == suma

def sum_col(matrix, j):
    sum = 0
    for i in range(len(matrix)):
        sum = sum + matrix[i][j]

    return sum


def is_palindrom(word):
    return word == word[::-1]

def find_count(filename, word):
    f = open(filename, 'r')
    count = 0
    for linie in f:
        words = linie.split(' ')

        for w in words:
            if word == w.strip():
                count = count + 1
    f.close()
    return count

def perfNronCol(matrix):
    res = True
    for i in range(len(matrix)):
        sum = sum_col(matrix, i)

        if is_perfnr(sum) == False:
            res = False

    return res

def sum_diag(matrix):
    result = []
    for idx in range(len(matrix)):
        sum_lin = 0
        for jdx in range(len(matrix[idx])):

            if idx != jdx:
                sum_lin = sum_lin + matrix[idx][jdx]

        result.append((sum_lin == matrix[idx][idx]))

    return result
        #if sum_lin == matrix[idx][idx]:
        #    result.append(True)
        #else:
        #    result.append(False)

def folgeInMat (matrix):
    lastel_p = 0
    lastel_ip = 0

    for idx in range(len(matrix)):
        if idx % 2 == 0:
            for jdx in range(len(matrix[idx]) - 1):
                if matrix[idx][jdx + 1] != matrix[idx][jdx] + 1:
                    return False
                if jdx == len(matrix[idx])
                    lastel_p = matrix[idx][jdx]
        else:
            for jdx in range(0, len(matrix[idx]), -1):
                if matrix[idx][jdx] != matrix[idx][jdx - 1] + 1:
                    return False
                if jdx == 0:
                    lastel_ip = matrix[idx][jdx]


    return True



def max_line_file(filename):
    f = open(filename, 'r')
    res = []
    max_len = 0
    for line in f:
        max_word = ''
        words = line.split(' ')

        for word in words:
            word = word.strip()

            if len(word) > max_len:
                max_word, max_len = word, len(word)
        res.append(max_len)

    return res


def count_palindrom(filename):
    f = open(filename, 'r')
    result = {}

    for line in f:
        words = line.split(' ')

        for word in words:
            if is_palindrom(word):
                result[word] = find_count(filename, word.strip())

    f.close()
    return result


def test_nrPerfCol():
    assert perfNronCol([
        [4, 3, 10],
        [1, 2, 10],
        [1, 1, 8]
    ]) == True


def test_sum_diag():
    assert sum_diag([
        [4, 3, 1],
        [1, 2, 1],
        [0, 5, 1]
        ]
    ) == [True, True, False]

    assert sum_diag(
        [
            [1, 2, 3],
            [1, 2, 1],
            [0, 4, 0]
        ]
    ) == [False, True, False]

def test_folgeInMate():
    assert folgeInMat(
        [
            [1, 2, 3],
            [6, 5, 4],
            [7, 8, 9]
        ]
    ) == True

    assert folgeInMat(
        [
            [4, 5, 6],
            [1, 2, 3],
            [7, 8, 9]
        ]
    ) == False
def test_max_line_file():
    assert max_line_file('data.input') == [4, 4]

def testt_count_pali():
    assert count_palindrom('data2.input') == {'anna': 2, 'abbcbba': 1, 'abba': 2}

def main():
    pass

test_folgeInMate()
test_sum_diag()
test_max_line_file()
testt_count_pali()
main()