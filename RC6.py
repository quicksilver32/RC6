from utils import *
import bitarray as ba
import math

w = 16  # Размер слова в битах  (16, 32, 64)
r = 20   # Кол-во раундов
Key = "12312312312312"  # Секретный ключ
print("KEY: ", Key)
l = len(Key)  # Размер ключа в байтах

Key_bit = ba.bitarray()
Key_bit.frombytes(Key.encode('utf-8'))
while len(Key_bit) % w != 0:
    Key_bit.insert(0, 0)
l = int(len(Key_bit) / 8)

# K = list(K)
#
# for i in range(len(K)):  # Преобразование ключа в байты
#     K[i] = ord(K[i])
#
# if (8 * l) % w != 0:  # Дополнение ключа до кратности с w
#     K.extend([0] * int((w / 8) - l % (w / 8)))
#     l = len(K)

Pw = {16: 0xb7e1, 32: 0xb7e15163, 64: 0xb7e151628aed2a6b}
Qw = {16: 0x9e37, 32: 0x9e3779b9, 64: 0x9e3779b97f4a7c15}

# Формирование раундового ключа
W = [Pw[w], ]  # Раундовый ключ длиной в 2r+4

c = int(8 * l / w)  # число слов в ключе

# Преобразование ключа в массив из с слов
L = []
for i in range(c):
    L.append(int(Key_bit[i:i + w].to01(), 2))

# L = []
# for i in range(int(l / c)):
#     temp = "0b"
#     for j in range(i * c, i * c + c):
#         temp += bin(K[j])[2:]
#     L.append(int(temp, 2))

for i in range(2 * r + 4 - 1):  # Инициализация массива раундовых ключей
    W.append(mod((W[-1] + Qw[w]), (2 ** w)))

i, j, a, b = 0, 0, 0, 0

for count in range(3 * c):  # Формирование раундового ключа
    # W[i] = shift(mod((W[i] + a + b), (2**w)), -3)
    # W[i] = left_shift(mod((W[i] + a + b), (2 ** w)), 3, w)
    W[i] = circular_shift(mod((W[i] + a + b), (2 ** w)), w, 3, 'left')
    a = W[i]
    # L[j] = shift(mod((L[j] + a + b), (2**w)), mod((a + b), (2**w)) % len(bin((L[j] + a + b))) - 2)
    # L[j] = left_shift(mod((L[j] + a + b), (2 ** w)), mod(mod((a + b), (2 ** w)), len(bin((L[j] + a + b))) - 2), w)
    L[j] = circular_shift(mod((L[j] + a + b), (2 ** w)), w, mod((a + b), (2 ** w)), 'left')
    b = L[j]
    i = mod((i + 1), (2 * r + 4))
    j = mod((j + 1), c)

# print(W)

# Шифрование
message = "уууу  qqqq"  # Сообщение
print("MESSAGE: ", message)
message_bit = ba.bitarray()  # Инициализация массива битов
message_bit.frombytes(message.encode('utf-8'))  # Сообщение в битах
while len(message_bit) % (4 * w) != 0:
    message_bit.insert(0, 0)  # Дополнение нулями до кратности в 4w
print("BIN MESSAGE: ", message_bit.to01())
encoded_message_bit = ""  # Инициализация зашифрованного сообщения

# print('encode')

for i in range(0, len(message_bit), 4 * w):  # Цикл по блокам в 4 слова
    A = int(message_bit[i:i + w].to01(), 2)
    B = int(message_bit[i + w:i + 2 * w].to01(), 2)
    C = int(message_bit[i + 2 * w:i + 3 * w].to01(), 2)
    D = int(message_bit[i + 3 * w:i + 4 * w].to01(), 2)

    B = mod(B + W[0], 2 ** w)
    D = mod(D + W[1], 2 ** w)

    for i in range(1, r+1):
        t = circular_shift(f(B, w), w, int(math.log(w)), "left")
        u = circular_shift(f(D, w), w, int(math.log(w)), "left")
        A = mod((circular_shift(XOR(A, t), w, u, 'left') + W[2 * i]), (2**w))
        C = mod((circular_shift(XOR(C, u), w, t, 'left') + W[2 * i + 1]), (2**w))

        aa, bb, cc, dd = B, C, D, A
        A, B, C, D = aa, bb, cc, dd

    A = mod(A + W[2 * r + 2], 2 ** w)
    C = mod(C + W[2 * r + 3], 2 ** w)
    encoded_message_bit += bin_expansion(bin(A), w)[2:] + bin_expansion(bin(B), w)[2:] + \
                           bin_expansion(bin(C), w)[2:] + bin_expansion(bin(D), w)[2:]

print("ENCODED BIN MESSAGE: ", encoded_message_bit)

# print('decode')

# Дешифрование
decoded_message_bit = ""
for i in range(0, len(encoded_message_bit), 4 * w):
    A = int('0b' + encoded_message_bit[i:i + w], 2)
    B = int('0b' + encoded_message_bit[i + w:i + 2 * w], 2)
    C = int('0b' + encoded_message_bit[i + 2 * w:i + 3 * w], 2)
    D = int('0b' + encoded_message_bit[i + 3 * w:i + 4 * w], 2)

    A = mod(A - W[2 * r + 2], 2 ** w)
    C = mod(C - W[2 * r + 3], 2 ** w)

    for j in range(1, r+1):
        i = r - j + 1

        aa, bb, cc, dd = D, A, B, C
        A, B, C, D = aa, bb, cc, dd

        t = circular_shift(f(B, w), w, int(math.log(w)), "left")
        u = circular_shift(f(D, w), w, int(math.log(w)), "left")
        A = XOR(circular_shift(mod((A - W[2 * i]), 2**w), w, u, 'right'), t)
        C = XOR(circular_shift(mod((C - W[2 * i + 1]), (2**w)), w, t, 'right'), u)

    B = mod(B - W[0], 2 ** w)
    D = mod(D - W[1], 2 ** w)
    decoded_message_bit += bin_expansion(bin(A), w)[2:] + bin_expansion(bin(B), w)[2:] + \
                           bin_expansion(bin(C), w)[2:] + bin_expansion(bin(D), w)[2:]

print("DECODED BIN MESSAGE: ", decoded_message_bit)
import base64
print("DECODED MESSAGE: ", base64.b16decode(hex(int(decoded_message_bit, base=2))[2:], casefold=True).decode('utf-8'))


