from utils import *

w = 32  # Размер слова в битах  (16, 32, 64)
r = 2  # Кол-во раундов
K = "1231231231231231"  # Секретный ключ
l = len(K)  # Размер ключа в байтах

K = list(K)

for i in range(len(K)):  # Преобразование ключа в байты
    K[i] = ord(K[i])

if (8 * l) % w != 0:  # Дополнение ключа до кратности с w
    K.extend([0] * int((w / 8) - l % (w / 8)))
    l = len(K)

Pw = {16: 0xb7e1, 32: 0xb7e15163, 64: 0xb7e151628aed2a6b}
Qw = {16: 0x9e37, 32: 0x9e3779b9, 64: 0x9e3779b97f4a7c15}

# Формирование раундового ключа
W = [Pw[w], ]  # Раундовый ключ длиной в 2r+4

c = int(8 * l / w)  # число слов в ключе

# Преобразование ключа в массив из с слов
L = []
for i in range(int(l/c)):
    temp = "0b"
    for j in range(i*c, i*c+c):
        temp += bin(K[j])[2:]
    L.append(int(temp, 2))

for i in range(2 * r + 4 - 1):  # Инициализация массива раундовых ключей
    W.append(mod((W[-1] + Qw[w]), (2**w)))

i, j, a, b = 0, 0, 0, 0

for count in range(3 * c):  # Формирование раундового ключа
    # W[i] = shift(mod((W[i] + a + b), (2**w)), -3)
    W[i] = left_shift(mod((W[i] + a + b), (2 ** w)), 3, w)
    a = W[i]
    # L[j] = shift(mod((L[j] + a + b), (2**w)), mod((a + b), (2**w)) % len(bin((L[j] + a + b))) - 2)
    L[j] = left_shift(mod((L[j] + a + b), (2 ** w)), mod(mod((a + b), (2 ** w)), len(bin((L[j] + a + b))) - 2), w)
    b = L[j]
    i = mod((i + 1), (2 * r + 4))
    j = mod((j + 1), c)

print(W)

# Шифрование
message = "qweqweqwewqe"

