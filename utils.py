#  Дополнение 0
def bin_expansion(bit_string, length):
    output = bit_string
    while len(output) != length + 2:
        output = output[:2] + '0' + output[2:]

    return output


def circular_shift(number, w, bits, side):
    bin_string = bin_expansion(bin(number), w)
    bits %= w
    bin_string = bin_string[2:]
    if side == 'left':
        return int('0b' + bin_string[bits:] + bin_string[:bits], 2)
    if side == 'right':
        return int('0b' + bin_string[-bits:] + bin_string[:-bits], 2)


# Операция a mod b
def mod(a, b):
    return int(a % b)


# Побитовое сложение по модулю 2
def XOR(a, b):
    return a ^ b


# Функция f
def f(x, w):
    return mod(x * (2 * x + 1), 2**w)


def bytesToBin(bytes_string):
    output = bytearray(bytes_string)
    output = [bin_expansion(bin(char), 8)[2:] for char in output]
    output = ''.join(output)
    return output


def binToBytes(bin_string):
    output = [int('0b' + bin_string[block * 8: (block + 1) * 8], 2) for block in range(int(len(bin_string) / 8))]
    output = bytes(output)
    return output