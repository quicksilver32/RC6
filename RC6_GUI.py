import base64
import math
from utils import *

Pw = {16: 0xb7e1, 32: 0xb7e15163, 64: 0xb7e151628aed2a6b}
Qw = {16: 0x9e37, 32: 0x9e3779b9, 64: 0x9e3779b97f4a7c15}


def generate_round_key(Key, w, r):
    Key_bit = base64.b64encode(bytes(Key, 'utf-8'))
    Key_bit = bytesToBin(Key_bit)  # Преобразование ключа в биты

    while len(Key_bit) % w != 0:  # Дополнение ключа до кратности w
        Key_bit = "0" + Key_bit
    l = int(len(Key_bit) / 8)

    # Формирование раундового ключа
    W = [Pw[w], ]  # Раундовый ключ длиной в 2r+4

    c = int(8 * l / w)  # число слов в ключе

    # Преобразование ключа в массив из с слов
    L = []
    for i in range(c):
        L.append(int(Key_bit[i:i + w], 2))

    for i in range(2 * r + 4 - 1):  # Инициализация массива раундовых ключей
        W.append(mod((W[-1] + Qw[w]), (2 ** w)))

    i, j, a, b = 0, 0, 0, 0

    for count in range(3 * c):  # Формирование раундового ключа
        W[i] = circular_shift(mod((W[i] + a + b), (2 ** w)), w, 3, 'left')
        a = W[i]
        L[j] = circular_shift(mod((L[j] + a + b), (2 ** w)), w, mod((a + b), (2 ** w)), 'left')
        b = L[j]
        i = mod((i + 1), (2 * r + 4))
        j = mod((j + 1), c)

    return W


def encode(message_bit, Key, w, r):
    W = generate_round_key(Key, w, r)

    # Дополнение сообщения нулями до кратности в 4w
    while len(message_bit) % (4 * w) != 0:
        message_bit = "0" + message_bit

    encoded_message_bit = ""  # Инициализация зашифрованного сообщения

    for i in range(0, len(message_bit), 4 * w):  # Цикл по блокам в 4 слова
        A = int('0b' + message_bit[i:i + w], 2)
        B = int('0b' + message_bit[i + w:i + 2 * w], 2)
        C = int('0b' + message_bit[i + 2 * w:i + 3 * w], 2)
        D = int('0b' + message_bit[i + 3 * w:i + 4 * w], 2)

        B = mod(B + W[0], 2 ** w)
        D = mod(D + W[1], 2 ** w)

        for i in range(1, r + 1):
            t = circular_shift(f(B, w), w, int(math.log(w)), "left")
            u = circular_shift(f(D, w), w, int(math.log(w)), "left")
            A = mod((circular_shift(XOR(A, t), w, u, 'left') + W[2 * i]), (2 ** w))
            C = mod((circular_shift(XOR(C, u), w, t, 'left') + W[2 * i + 1]), (2 ** w))

            aa, bb, cc, dd = B, C, D, A
            A, B, C, D = aa, bb, cc, dd

        A = mod(A + W[2 * r + 2], 2 ** w)
        C = mod(C + W[2 * r + 3], 2 ** w)
        encoded_message_bit += bin_expansion(bin(A), w)[2:] + bin_expansion(bin(B), w)[2:] + \
                               bin_expansion(bin(C), w)[2:] + bin_expansion(bin(D), w)[2:]

    return encoded_message_bit


def decode(encoded_message_bit, Key, w, r):
    W = generate_round_key(Key, w, r)

    # Дополнение сообщения нулями до кратности в 4w
    while len(encoded_message_bit) % (4 * w) != 0:
        encoded_message_bit = "0" + encoded_message_bit

    decoded_message_bit = ""
    for i in range(0, len(encoded_message_bit), 4 * w):
        A = int('0b' + encoded_message_bit[i:i + w], 2)
        B = int('0b' + encoded_message_bit[i + w:i + 2 * w], 2)
        C = int('0b' + encoded_message_bit[i + 2 * w:i + 3 * w], 2)
        D = int('0b' + encoded_message_bit[i + 3 * w:i + 4 * w], 2)

        A = mod(A - W[2 * r + 2], 2 ** w)
        C = mod(C - W[2 * r + 3], 2 ** w)

        for j in range(1, r + 1):
            i = r - j + 1

            aa, bb, cc, dd = D, A, B, C
            A, B, C, D = aa, bb, cc, dd

            t = circular_shift(f(B, w), w, int(math.log(w)), "left")
            u = circular_shift(f(D, w), w, int(math.log(w)), "left")
            A = XOR(circular_shift(mod((A - W[2 * i]), 2 ** w), w, u, 'right'), t)
            C = XOR(circular_shift(mod((C - W[2 * i + 1]), (2 ** w)), w, t, 'right'), u)

        B = mod(B - W[0], 2 ** w)
        D = mod(D - W[1], 2 ** w)
        decoded_message_bit += bin_expansion(bin(A), w)[2:] + bin_expansion(bin(B), w)[2:] + \
                               bin_expansion(bin(C), w)[2:] + bin_expansion(bin(D), w)[2:]

    decoded_message_bit = decoded_message_bit.lstrip("0")
    while len(decoded_message_bit) % 8:
        decoded_message_bit = "0" + decoded_message_bit

    return decoded_message_bit