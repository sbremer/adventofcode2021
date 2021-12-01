import numpy as np

from aoc21 import get_input_lines

lines = get_input_lines(1)

numbers = np.array(list(map(int, lines)))

larger = (numbers[1:] > numbers[:-1]).sum()
print(larger)

numbers_windowed = np.convolve(numbers, np.array([1, 1, 1]), mode='valid')

larger = (numbers_windowed[1:] > numbers_windowed[:-1]).sum()
print(larger)
