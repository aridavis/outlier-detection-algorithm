import Utility
from Data import data

DISTANCE_THRESHOLD = 4
PROPORTION = 0.2
DATA_SIZE = len(data)
ABSOLUTE_PROPORTION_COUNT = PROPORTION * DATA_SIZE

matrix = []
outliers = []


def find_outliers():
    for i in range(0, DATA_SIZE):
        count = 0
        for j in range(0, DATA_SIZE):
            if matrix[i][j] <= DISTANCE_THRESHOLD and i != j:
                count += 1
        if count < ABSOLUTE_PROPORTION_COUNT:
            outliers.append(data[i])


def print_outliers():
    for outlier in outliers:
        print(outlier['id'])


if __name__ == '__main__':
    matrix = Utility.fill_matrix(data)
    find_outliers()
    print_outliers()
