import math


def find_euclidean(data1, data2):
    temp = []
    for i in range(0, len(data1['attr'])):
        attr1 = data1['attr'][i]
        attr2 = data2['attr'][i]
        temp.append(pow(attr1 - attr2, 2))

    sum = 0
    for t in temp:
        sum += t

    return math.sqrt(sum)


def fill_matrix(data):
    matrix = []
    for i in data:
        euclidean_arr = []
        for j in data:
            euclidean_arr.append(find_euclidean(i, j))
        matrix.append(euclidean_arr)
    return matrix


def fill_matrix_with_destination(data):
    matrix = []
    for i in data:
        euclidean_arr = []
        idx = 0
        for j in data:
            euclidean_arr.append({'dest': idx, 'distance': find_euclidean(i, j)})
            idx += 1
        matrix.append(euclidean_arr)
    return matrix


def get_max(a, b):
    if a > b:
        return a
    return b
