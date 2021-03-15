# RC6

Реализация блочного алгоритма RC6 на Python
Предусматривает различные его вариации:\
*****w*****: размер слова (16/32/64 бит) шифрование происходит блоками по 4 слова\
*****r*****: количество раундов\
*****Key*****: секретный ключ, любой длины
#
###### Подготовка окружения:
`python -m venv venv` - Инициализировать виртуальное окружение\
`venv/Scripts/activate` - Активировать виртуальное окружение\
`deactivate` - Декативировать виртуальное окружение (если оно активно)\
*При активном виртуальном окружении:*\
`pip install -r requirements.txt` - Установить необходимые пакеты
#
###### Запуск приложения с графическим интерфейсом (работа с файлами):
`python main.py`
#
###### Запуск консольного приложения (работа со строками):
`python RC6.py`
