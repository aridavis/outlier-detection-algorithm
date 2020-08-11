from Data import data
import Utility

DATA = data
K = 3
DATA_SIZE = len(data)
MATRIX = Utility.fill_matrix_with_destination(data)

K_DISTANCE = []
K_DISTANCE_NEIGHBORHOOD = []
REACH_DISTANCES = []
LRD = []
LOF = []


def get_lrd(idx):
    sum = 0
    for i in REACH_DISTANCES[idx]:
        sum += i
    return 1 / (sum / len(REACH_DISTANCES[idx]))


def get_lof(idx):
    o_accent = 0
    for i in K_DISTANCE_NEIGHBORHOOD[idx]:
        o_accent += get_lrd(i['dest'])

    return ((o_accent / get_lrd(idx))) / len(K_DISTANCE_NEIGHBORHOOD[idx])


def fill_k_distance():
    global i
    for i in Utility.fill_matrix(data):
        i.sort()
        K_DISTANCE.append(i[K])


def fill_k_neighbor_distance():
    global i, temp, j
    for i in range(0, DATA_SIZE):
        temp = []
        for j in range(0, DATA_SIZE):
            if MATRIX[i][j]['distance'] <= K_DISTANCE[i] and i != j:
                temp.append(MATRIX[i][j])
        K_DISTANCE_NEIGHBORHOOD.append(temp)


def fill_reach_distance():
    global i, temp, j
    for i in range(0, DATA_SIZE):
        temp = []
        for j in K_DISTANCE_NEIGHBORHOOD[i]:
            temp.append(Utility.get_max(K_DISTANCE[j['dest']], j['distance']))
        REACH_DISTANCES.append(temp)


def fill_lrd():
    global i
    for i in range(0, DATA_SIZE):
        LRD.append(get_lrd(i))


def fill_lof():
    global i
    for i in range(0, DATA_SIZE):
        LOF.append(get_lof(i))


if __name__ == '__main__':

    fill_k_distance()

    fill_k_neighbor_distance()

    fill_reach_distance()

    fill_lrd()

    fill_lof()

    idx = 0
    for i in LOF:
        if (i > 1):
            print(data[idx]['id'])
        idx += 1

