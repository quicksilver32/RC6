# Циклический побитовый сдвиг
def shift(number, steps):
    if steps == 0:
        return number
    number = list(bin(number)[2:])
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            number.append(number.pop(0))
    else:
        for i in range(steps):
            number.insert(0, number.pop())
    number = "0b" + "".join(number)
    return int(number, 2)


# Циклический сдвиг вправо
def right_shift(x, n, bits):
    mask = (2 ** n) - 1
    mask_bits = x & mask
    return (x >> n) | (mask_bits << (bits - n))


# Циклический сдвиг влево
def left_shift(x, n, bits):
    return right_shift(x, bits - n, bits)


# Операция a mod b
def mod(a, b):
    return int(a % b)


# Побитовое сложение по модулю 2
def XOR(a, b):
    return a ^ b
