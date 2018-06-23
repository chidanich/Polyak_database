import pickle as pk

# загрузка параметров из файла



def load_file():
        """
        Входных параметров нет
        Выхожной параметр - database - база данных из файла
        Загрузка базы данных из файла в глобальную переменную database
        Автор: Петин Д.М.
        """
        par = pk.load(open('parametrs.pic', mode='rb'))
        database = pk.load(open(par['way_to_base'], mode='rb'))
        return database


def save_file(database):
        """
        Входной парметр - database - база для записи в файл
        Выходных парметров нет
        Сохраняет бызу данных в файл
        Автор: Яценко И.Ю
        """

        par = pk.load(open('parametrs.pic', mode='rb'))  # загрузка параметров из файла
        pk.dump(database, open(par['way_to_base'], mode='wb'))


def addition(database, name, nation, age, club, position, value, contract_date, salary):
        """
        Входные параметры - name, nation, age, club, position, value, contract_date, salary - ключи-названия колонок базы
        Выходных параметров нет
        Добавление новой записи в базу данных
        Автор: Петин Д.М.
        """
        #  Поиск свободного ключа в базе
        i = 1
        while i in database:
            i += 1
        # Запись данных по найденному ключу
        database[i] = {'Name': name,
                       'Nationality': nation,
                       'Age': age,
                       'Club': club,
                       'Position': position,
                       'Transfer Value': value,
                       'Contract expiry date': contract_date,
                       'Salary': salary}


def delete(database, number):
        """
        Входные параметры - number  - номер колонки к удалению
        Выходных параметров нет
        Удаление записи по номеру
        Автор: Рыльников А.М.
        """
        number = int(number)
        database.pop(number, None)


def edition(database,k, name, nation, age, club, position, value, contract_date, salary):
        """
        ходные параметры - name, nation, age, club, position, value, contract_date, salary - ключи-названия колонок базы
        Выходных параметров нет
        Редактирование записи по номеру и ключу
        Автор: Яценко И.Ю.
        """
        database[k] = {'Name': name,
                       'Nationality': nation,
                       'Age': age,
                       'Club': club,
                       'Position': position,
                       'Transfer Value': value,
                       'Contract expiry date': contract_date,
                       'Salary': salary}


def is_int(s):
    """
            Входные параметры - s - переменная для проверки
            Возаращает True - если s - целое, иначе False
            Проверка на целочисленность
            Автор: Петин Д.М.
            """
    if s == '':
        return True
    try:
        int(s)
        return True
    except ValueError:
        return False

def is_float(s):
    """
                Входные параметры - s - переменная для проверки
                Возаращает True - если s - число, иначе False
                Проверка на число
                Автор: Петин Д.М.
                """
    if s == '':
        return True
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_date(s):
    """
                Входные параметры - s - переменная для проверки
                Возаращает True - если s - корректная дата, иначе False
                Проверка на корректную дату
                Автор: Рыльников А.М.
                """
    a = s[0:2]  # число
    b = s[3:5]  # месяц
    c = s[6:10] # год
    # проверка на целочисленность числа,месяца и года
    a1 = is_int(a)
    b1 = is_int(b)
    c1 = is_int(c)
    d30 = ['04', '06', '09', '11']  # месяцы 30 дней
    d29 = ['02'] # месяцы 29 дней
    d31 = ['01', '03', '05', '07', '08', '10', '12']  # месяцы 31 день
    if len(s) == 10 and a1 and b1 and c1 and s[2] == '.' and s[5] == '.' and int(a) > 0 and int(b) > 0 and \
            int(c) >= 2018 and ((b in d30 and int(a) <= 30) or (b in d31 and int(a) <= 31) or
                                (b in d29 and int(a) <= 29)):
        return True
    else:
        return False


def search(database, key, value):
    """
    Входной парметр - database, key, value - база для записи в файл
    Возвращает db - словарь словарей - база данных с найденными элементами
    Ищет элементы по строковым значениям
    Автор: Яценко И.Ю.
    """
    if value == '':
        return False
    else:
        db = {}
        res = 0
        for i in database.keys():
            if value.lower() in database[i][key].lower():
                db[res] = database[i]
                res += 1
        return db


def search_num(database,key, value1, value2):
    """
    Входной парметр - database, key, value1, value2 - база для записи в файл
    Возвращает db - словарь словарей - база данных с найденными элементами
    Ищет элементы по числовым значениям
    Автор: Петин Д.М
    """
    if value1 == '' and value2 == '':
        return False
    elif value1 != '' and value2 != '':
        db = {}
        res = 0
        for i in database.keys():
            if float(value1) <= float(database[i][key]) <= float(value2):
                db[i] = database[i]
                res += 1
        return db
    elif value1 != '' and value2 == '':
        db = {}
        res = 0
        for i in database.keys():
            if float(value1) <= float(database[i][key]) :
                db[i] = database[i]
                res += 1
        return db
    elif value1 == '' and value2 != '':
        db = {}
        res = 0
        for i in database.keys():
            if float(database[i][key])  <= float(value2):
                db[i] = database[i]
                res += 1
        return db


def search_date(database,key, value1, value2):
    """
    Входной парметр - database, key, value1, value2 - база для записи в файл
    Возвращает db - словарь словарей - база данных с найденными элементами
    Ищет значения по дате
    Автор: Рыльников А.М.
    """

    if value1 == '' and value2 == '':
        return False
    elif value1 != '' and value2 != '':
        db = {}
        value1 = float(str(value1)[-4:])
        value2 = float(str(value2)[-4:])
        res = 0
        for i in database.keys():
            if value1 <= float(str(database[i][key])[-4:]) <= value2:
                db[i] = database[i]
                res += 1
        return db
    elif value1 != '' and value2 == '':
        db = {}
        value1 = float(str(value1)[-4:])
        #value2 = float(str(value2)[-4:])
        res = 0
        for i in database.keys():
            if value1 <= float(str(database[i][key])[-4:]):
                db[i] = database[i]
                res += 1
        return db
    elif value1 == '' and value2 != '':
        db = {}
        #value1 = float(str(value1)[-4:])
        value2 = float(str(value2)[-4:])
        res = 0
        for i in database.keys():
            if float(str(database[i][key])[-4:]) <= value2:
                db[i] = database[i]
                res += 1
        return db