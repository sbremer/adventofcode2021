from aoc21 import get_input_lines

lines = get_input_lines(2)

pos_h = 0
pos_d = 0

for line in lines:
    cmd, i = line.split(' ')
    i = int(i)

    if cmd == 'forward':
        pos_h += i
    elif cmd == 'down':
        pos_d += i
    elif cmd == 'up':
        pos_d -= i
    else:
        raise ValueError

print(f'Product of h and d pos: {pos_h * pos_d}')

pos_h = 0
pos_d = 0
aim = 0

for line in lines:
    cmd, i = line.split(' ')
    i = int(i)

    if cmd == 'forward':
        pos_h += i
        pos_d += aim * i
    elif cmd == 'down':
        aim += i
    elif cmd == 'up':
        aim -= i
    else:
        raise ValueError

print(f'New product of h and d pos: {pos_h * pos_d}')
