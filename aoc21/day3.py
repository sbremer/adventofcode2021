import numpy as np

from aoc21 import get_input_lines

lines = get_input_lines(3)

data = np.array([[int(i) for i in line] for line in lines])

most_common = data.mean(axis=0).round().astype(int)
least_common = abs(most_common - 1)

gamma = int(''.join(str(i) for i in most_common), 2)
epsilon = int(''.join(str(i) for i in least_common), 2)

print(f'Power consumption: {gamma * epsilon}')

data_ = data.copy()
n_bits = data.shape[1]

remaining = data_.shape[0]
at_bit = 0
while remaining > 1:
    ones = data_[:, at_bit].sum()

    if ones >= remaining / 2:
        data_ = data_[data_[:, at_bit] == 1, :]
    else:
        data_ = data_[data_[:, at_bit] == 0, :]

    at_bit = at_bit + 1 % n_bits
    remaining = data_.shape[0]

oxygen = int(''.join(str(i) for i in data_[0]), 2)

data_ = data.copy()

remaining = data_.shape[0]
at_bit = 0
while remaining > 1:
    ones = data_[:, at_bit].sum()

    if ones >= remaining / 2:
        data_ = data_[data_[:, at_bit] == 0, :]
    else:
        data_ = data_[data_[:, at_bit] == 1, :]

    at_bit = at_bit + 1 % n_bits
    remaining = data_.shape[0]

co2 = int(''.join(str(i) for i in data_[0]), 2)

print(f'Life support rating: {oxygen * co2}')
