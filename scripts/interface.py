# -*- coding: utf-8 -*-
import sys  # модули sys и os для функции перезагрузки программы
import os
sys.path.append('../library')
import base as b  # модуль со стандартной базой
import functions as f  # модуль с функциями
import tkinter as t  # модуль tkinter для создания графического интерфейса
from tkinter import messagebox as mb  # messagebox из tkinter для сообщений пользователю
import tkinter.filedialog as fd  # tkinter.filedialog для диалоговых окон
import tkinter.colorchooser as cl  # tkinter.colorchooser для цветового селектора
import pickle as pk  # модуль pickle

par = pk.load(open('parametrs.pic', mode='rb'))  # загрузка параметров из файла


def print_base(fra, database):
    """
        Входные параметры - fra - фрейм для записи базы данных, database - база
        Выходных параметров нет
        Вывод базы на экран
        Автор: Петин Д.М.
        """
    par = pk.load(open('parametrs.pic', mode='rb'))
    k = 0
    for i in database.keys():
        k = k+1
    if k == 0:
        bas = t.Label(fra, text=' No items in database', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                      font=(par['font'], '40', 'bold'))
        bas.grid(row=0, column=0, sticky=t.NSEW)
    else:
        # Столбик с номерами
        bas = t.Label(fra, text=' Number', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                      font=(par['font'], par['letter_size_h1'], 'bold'))
        bas.grid(row=0, column=0, sticky=t.NSEW)
        for i in range(len(database)):
            bas = t.Label(fra, text=' %s ' % (i + 1), relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                          font=(par['font'], par['letter_size_h1'], 'bold'))
            bas.grid(row=i + 1, column=0, sticky=t.NSEW)

        # Названия столбцов
        bas = t.Label(fra, text=' Key ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                      font=(par['font'], par['letter_size_h1'], 'bold'))
        bas.grid(row=0, column=1, sticky=t.NSEW)
        for l in database.keys():
            for i, j in enumerate(database[l]):
                bas = t.Label(fra, text='  %s  ' % j, relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                              font=(par['font'], par['letter_size_h1'], 'bold'))
                bas.grid(row=0, column=i + 2, sticky=t.NSEW)
            break
        bas = t.Label(fra, text='    ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                      font=(par['font'], par['letter_size_h1'], 'bold'))
        bas.grid(row=0, column=10, columnspan=2, sticky=t.NSEW)

        # Вывод данных
        lis = [2, 3, 4, 5, 6, 7, 8, 9]
        j = 1
        val_sal = 0
        val_aver = 0
        sam_v = 0
        sam_t = 0
        av_ag = 0
        sam_a = 0

        for k in database.keys():
            bas = t.Label(fra, text=' %s ' % k, relief=t.GROOVE, bg=par['table_colour'], fg=par['letter_colour'],
                          font=(par['font'], par['letter_size']))
            bas.grid(row=j, column=1, sticky=t.NSEW)
            for i, item in zip(lis, database[k].values()):
                bas = t.Label(fra, text=' %s ' % item, relief=t.GROOVE, bg=par['table_colour'], fg=par['letter_colour'],
                              font=(par['font'], par['letter_size']))
                bas.grid(row=j, column=i, sticky=t.NSEW)



        # ПОДВЕДЕНИЕ ИТОГОВ
            if -1 not in database.keys():

                av_ag = av_ag + int(database[k]['Age'])
                val_aver = val_aver + float(database[k]['Transfer Value'])
                val_sal = val_sal + float(database[k]['Salary'])
            deleti = t.Button(fra, text="X", width=1, height=1, bg='red',
                              fg=par['letter_colour'],
                              font=(par['font'], par['letter_size_h1'], 'bold'), command=lambda db=database, k=k: delet(db, k))
            deleti.grid(row=j, column=10, sticky=t.NSEW)
            editi = t.Button(fra, text="Edit", width=6, height=1, bg='orange',
                              fg=par['letter_colour'],
                              font=(par['font'], par['letter_size_h1'], 'bold'),
                              command=lambda db=database, ke=k, n=j: edit(db, ke, n))
            editi.grid(row=j, column=11, sticky=t.NSEW)
            j += 1
        if -1 not in database.keys():
            numbr = '  ' + str(len(database)) + '  '
            val_aver = float(val_aver) / float(numbr)
            val_sal = float(val_sal) / float(numbr)
            av_ag = float(av_ag) / float(numbr)
            for k in database.keys():
                sam_v = sam_v + (float(database[k]['Transfer Value']) - val_aver)**2
                sam_t = sam_t + (float(database[k]['Salary']) - val_sal)**2
                sam_a = sam_a + (int(database[k]['Age']) - av_ag) ** 2
            tot = t.Label(dele_f, text=' \nTotals\n ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                        font=(par['font'], par['letter_size_h1'], 'bold'))
            tot.grid(row=0, column=2, columnspan=2, sticky=t.NSEW)

            # КОЛ-ВО ЭЛЕМЕНТОВ

            ni = t.Label(dele_f, text=' Number of items: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                        font=(par['font'], par['letter_size_h1'], 'bold'))
            ni.grid(row=1, column=2, sticky=t.NSEW)
            ni = t.Label(dele_f, text='%s' % numbr, relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                        font=(par['font'], par['letter_size_h1'], 'bold'))
            ni.grid(row=1, column=3, sticky=t.NSEW)


            sam_v = float(sam_v)/float(numbr)
            sam_t = float(sam_t) / float(numbr)
            sam_a = float(sam_a) / float(numbr)

            # СРЕДНИЙ ВОЗРАСТ

            ava = t.Label(dele_f, text=' Average age: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                        font=(par['font'], par['letter_size_h1'], 'bold'))
            ava.grid(row=2, column=2, sticky=t.NSEW)
            ava = t.Label(dele_f, text='%.2f' % av_ag, relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                        font=(par['font'], par['letter_size_h1'], 'bold'))
            ava.grid(row=2, column=3, sticky=t.NSEW)

            # ВЫБОРОЧНАЯ ДИСПЕРСИЯ ВОЗРАСТА

            sampvar = t.Label(dele_f, text=' Sample variance of \n'
                                  'age: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                        font=(par['font'], par['letter_size_h1'], 'bold'))
            sampvar.grid(row=3, column=2, sticky=t.NSEW)
            sampvar = t.Label(dele_f, text='%.2f' % sam_a, relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                        font=(par['font'], par['letter_size_h1'], 'bold'))
            sampvar.grid(row=3, column=3, sticky=t.NSEW)

            # СРЕДНЯЯ ТРАНСФЕРНАЯ ЦЕНА

            avt = t.Label(dele_f, text=' Average transfer \nvalue: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                        font=(par['font'], par['letter_size_h1'], 'bold'))
            avt.grid(row=4, column=2, sticky=t.NSEW)
            avt = t.Label(dele_f, text='%.2f' % val_aver, relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                        font=(par['font'], par['letter_size_h1'], 'bold'))
            avt.grid(row=4, column=3, sticky=t.NSEW)

            # ВЫБОРОЧНАЯ ДИСПЕРСИЯ ТРАНСФЕРНОЙ ЦЕНЫ

            sampt = t.Label(dele_f, text=' Sample variance of \n'
                                     'transfer value: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                        font=(par['font'], par['letter_size_h1'], 'bold'))
            sampt.grid(row=5, column=2,rowspan=2, sticky=t.NSEW)
            sampt = t.Label(dele_f, text='%.2f' % sam_v, relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                        font=(par['font'], par['letter_size_h1'], 'bold'))
            sampt.grid(row=5, column=3, rowspan=2, sticky=t.NSEW)

            # СРЕДНЯЯ ЗАРПЛАТА

            avs = t.Label(dele_f, text=' Average salary: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                        font=(par['font'], par['letter_size_h1'], 'bold'))
            avs.grid(row=7, column=2, sticky=t.NSEW)
            avs = t.Label(dele_f, text='%.2f' % val_sal, relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                        font=(par['font'], par['letter_size_h1'], 'bold'))
            avs.grid(row=7, column=3, sticky=t.NSEW)

            # ВЫБОРОЧНАЯ ДИСПЕРСИЯ ЗАРПЛАТЫ

            sams = t.Label(dele_f, text='  Sample variance of \n'
                                     'salary: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                        font=(par['font'], par['letter_size_h1'], 'bold'))
            sams.grid(row=8, column=2,rowspan=2, sticky=t.NSEW)

            sams = t.Label(dele_f, text='%.2f' % sam_t, relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                        font=(par['font'], par['letter_size_h1'], 'bold'))
            sams.grid(row=8, column=3, rowspan=2, sticky=t.NSEW)

            ad =  t.Label(dele_f, text='', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                        font=(par['font'], par['letter_size_h1'], 'bold'))
            ad.grid(row=10, column=2, columnspan=2, sticky=t.NSEW)

            # ЗАПИСЬ В ФАЙЛ
            par = pk.load(open('parametrs.pic', mode='rb'))
            with open(par['way_to_total'], "a") as file:
                file.write('Total :\n\n'
                           'Number of items: ' +  str(numbr) + '\n' +
                           'Average age :' + '%.2f' % av_ag + '\n' +
                           'Sample variance of age: :' + '%.2f' % sam_a + '\n' +
                           'Average transfer value :' + '%.2f' % val_aver + '\n' +
                           'Sample variance of transfer value :' + '%.2f' % sam_v + '\n' +
                           'Average salary :' + '%.2f' % val_sal + '\n' +
                           'Sample variance of salary :' + '%.2f' % sam_t + '\n\n')


def print_butt(*args):
    """
            Входных параметров нет
            Выходных параметров нет
            Вызов функции печати базы для кнопки интерфейса
            Автор: Яценко И.Ю.
            """
    print_base(basafr, database)


def clear_base(fra):
    """
            Входные параметры - fra - фрейм для для удаления
            Выходных параметров нет
            Очистка фрейма от базы
            Автор: Рыльников А.М.
            """
    for bas in fra.grid_slaves():
        bas.grid_forget()


def load(*args):
    """
                Входные параметров нет
                Выходных параметров нет
                Вызов функции загрзуки базы из библиотеки для кнопки интерфейса
                Автор: Яценко И.Ю.
                """
    global database
    fi = fd.askopenfilename()
    if fi == '' or fi[-3:] != 'pic':
        mb.showerror("Error",
                     "File error\nChoose file\nYou can choose only 'pic' file")
    else:
        par['way_to_base'] = fi
        pk.dump(par, open('parametrs.pic', mode='wb'))
        fi = fd.askopenfilename()
        if fi == '' or fi[-3:] != 'txt':
            mb.showerror("Error",
                         "File error\nChoose file\nYou can choose only 'txt' file")
        else:
            par['way_to_total'] = fi
            pk.dump(par, open('parametrs.pic', mode='wb'))
            database = f.load_file()
            prnt.config(state="normal")
            clr.config(state="normal")
            defa.config(state="normal")
            ad.config(state="normal")
            sett.config(state="normal")
            fltr.config(state="normal")


def save_b(*args):
    """
                    Входные параметров нет
                    Выходных параметров нет
                    Вызов функции сохранения базы из библиотеки для кнопки интерфейса
                    Автор: Рыльников А.М.
                    """
    f.save_file(database)


def delet(db,k):
    """
                    Входные db и k
                    Выходных параметров нет
                    Удаление элемента по ключю для кнопки интерфейса
                    Автор: Яценко И.Ю.
                    """
    f.delete(db, k)
    f.save_file(db)
    database = f.load_file()
    clear_base(basafr)
    print_base(basafr, database)


def defaults(*args):
    """
                        Входные параметров нет
                        Выходных параметров нет
                        Возвращение начальных параметров
                        Автор: Яценко И.Ю
                        """
    b.defa()
    database = f.load_file()
    clear_base(basafr)
    print_base(basafr, database)
    f.save_file(database)

def add(*args):
    """
                        Входные параметров нет
                        Выходных параметров нет
                        Добавление элемента для кнопки интерфейса
                        Автор: Рыльников А.М.
                        """
    name = nam.get()
    nation = nat.get()
    age = age1.get()
    club = clu.get()
    position = pos.get()
    value = val.get()
    date = exp.get()
    salary = sal.get()
    s = f.is_float(value)
    s1 = f.is_float(salary)
    s2 = f.is_int(age)
    # проверка полученных данных на соответсвие
    if s == False or s1 == False or position == '' or date == '' or s2 == False or float(salary) <0 or float(value) < 0  or int(age) > 50 or int(age) < 16:
        mb.showerror("Error", "Input error\nAge must be integer from 16 to 50, Salary and value must be floats more than 0\nChoose position and date")
    else:
        database = f.load_file()
        f.addition(database, name, nation, age, club, position, value, date, salary)
        f.save_file(database)
        database = f.load_file()
        clear_base(basafr)
        print_base(basafr, database)


def edit(database,ke, n):
    """
                        Входные - database, k
                        Выходных параметров нет
                        Редактирование по ключю для кнопки интерфейса
                        Автор: Рыльников А.М.
                        """
    name1 = t.Entry(basafr, width=10, bd=8)
    name1.grid(row=n, column=2, sticky=t.NSEW)
    name1.insert(0, database[ke]['Name'])

    nat = t.Entry(basafr, width=10, bd=8)
    nat.grid(row=n, column=3, sticky=t.NSEW)
    nat.insert(0, database[ke]['Nationality'])

    ag = t.Entry(basafr, width=10, bd=8)
    ag.grid(row=n, column=4, sticky=t.NSEW)
    ag.insert(0, database[ke]['Age'])

    clubi = t.Entry(basafr, width=10, bd=8)
    clubi.grid(row=n, column=5, sticky=t.NSEW)
    clubi.insert(0, database[ke]['Club'])

    posi = t.StringVar(basafr)
    posi.set(database[ke]['Position'])
    posit = t.OptionMenu(basafr, posi, 'Forward', 'Winger', 'Attacking Midfielder', 'Defending Midfielder',
                        'Left Defender', 'Center Defender', 'Right Defender', 'Goalkeeper')
    posit.grid(row=n, column=6, sticky=t.NSEW)

    tv = t.Entry(basafr, width=10, bd=8)
    tv.grid(row=n, column=7, sticky=t.NSEW)
    tv.insert(0, database[ke]['Transfer Value'])

    da = t.StringVar(basafr)
    da.set(database[ke]['Contract expiry date'])
    dax = t.OptionMenu(basafr, da, '30.06.2018', '30.06.2019', '30.06.2020', '30.06.2021',
                        '30.06.2022', '30.06.2023', '30.06.2024', '30.06.2026', '30.06.2027', '30.06.2028', '30.06.2029')
    dax.grid(row=n, column=8, sticky=t.NSEW)

    sa = t.Entry(basafr, width=10, bd=8)
    sa.grid(row=n, column=9, sticky=t.NSEW)
    sa.insert(0, database[ke]['Salary'])

    savi = t.Button(basafr, text="Save", width=6, height=1, bg='light blue',
                     fg=par['letter_colour'],
                     font=(par['font'], par['letter_size_h1'], 'bold'),
                    command=lambda database=database,k=ke: sav(database, k))
    savi.grid(row=n, column=11, sticky=t.NSEW)

    def sav(database,k):
        name = name1.get()
        nation = nat.get()
        age = ag.get()
        club = clubi.get()
        position = posi.get()
        value = tv.get()
        contract = da.get()
        salary = sa.get()
        a1 = f.is_int(age)
        v1 = f.is_float(value)
        s1 = f.is_float(salary)
        if (a1 == False or int(age)<16 or int(age)>50 or v1 == False or float(value)<0.1 or float(value)>1000 or s1 == False or float(salary)<0.1 or float(salary)>1000):
            mb.showerror("Error",
                         "Input error\nAge must be integer from 16 to 50\nTransfer Value and Salary must be floats from 0.1 to 1000\nChoose column")
        else:
            f.edition(database, k, name, nation, age, club, position, value, contract, salary)
            f.save_file(database)
            database = f.load_file()
            clear_base(basafr)
            print_base(basafr, database)



def serch(*args):
    """
                        Входные параметров нет
                        Выходных параметров нет
                        Поиск элементов для кнопки интерфейса
                        Автор: Петин Д.М.
                       """
    def check_s(v):
        """
                                Входной ппарметр - s
                                Возвращает True или False
                                Проверка на наличие ввода
                                Автор: Петин Д.М.
                               """
        if v != '':
            return True
        else:
            return False
    # имя
    nam_v = nama.get()
    nc = check_s(nam_v)
    # страна
    nat_v = nata.get()
    natc = check_s(nat_v)
    # возраст
    age_v1 = a11.get()
    age_v2 = a12.get()
    a1_c = check_s(age_v1)
    a2_c = check_s(age_v2)
    ag_c1 = f.is_int(age_v1)
    ag_c2 = f.is_int(age_v2)

    # клуб
    cl_v = cl3.get()
    c2_c = check_s(cl_v)
    # клуб
    ps_v = pos12.get()
    p2_c = check_s(ps_v)
    # стоимость
    tv_v1 = t11.get()
    tv_v2 = t12.get()
    t1_c = check_s(tv_v1)
    t2_c = check_s(tv_v2)
    tv_c1 = f.is_float(tv_v1)
    tv_c2 = f.is_float(tv_v2)

    # дата
    d_v1 = d11.get()
    d_v2 = d12.get()
    d1_c = check_s(d_v1)
    d2_c = check_s(d_v2)
    # зарплата
    s_v1 = sl11.get()
    s_v2 = sl12.get()
    s1_c = check_s(s_v1)
    s2_c = check_s(s_v2)
    s_c1 = f.is_float(s_v1)
    s_c2 = f.is_float(s_v2)
    if (a1_c == True and a2_c == True and age_v1 > age_v2) or (t1_c == True and t2_c == True and tv_v1 > tv_v2) \
        or (d1_c == True and d2_c == True and d_v1 > d_v2) or (s1_c == True and s2_c == True and s_v1 > s_v2)\
        or s_c1 == False or s_c2 == False or tv_c1 == False or tv_c2 == False or ag_c1 == False or ag_c2 == False:
        mb.showerror("Error",
                     "Input error\nAge must be integer, Salary and Value must be floats\nValue 2 must be more than or Value 1")
    elif nc == False and s2_c == False and s1_c == False and d2_c == False and d1_c == False and t1_c == False and t2_c == False and p2_c == False and c2_c == False and a1_c == False and a2_c == False and natc == False:
        mb.showerror("Error",
                     "Nothing chosen")
    else:
        database = f.load_file()
        db1 = db2 = db3 = db4 = db5 = db6 = db7 = db8 = False
        db1 = f.search(database, 'Name', nam_v)

        if db1 != False:
            db2 = f.search(db1, 'Nationality', nat_v)
        else:
            db2 = f.search(database, 'Nationality', nat_v)

        if db2 != False:
            db3 = f.search_num(db2, 'Age', age_v1, age_v2)
        elif db1 != False:
            db3 = f.search_num(db1, 'Age', age_v1, age_v2)
        else:
            db3 = f.search_num(database, 'Age', age_v1, age_v2)

        if db3 != False:
            db4 = f.search(db3, 'Club', cl_v)
        elif db2 != False:
            db4 = f.search(db2, 'Club', cl_v)
        elif db1 != False:
            db4 = f.search(db1, 'Club', cl_v)
        else:
            db4 = f.search(database, 'Club', cl_v)

        if db4 != False:
            db5 = f.search(db4, 'Position', ps_v)
        elif db3 != False:
            db5 = f.search(db3, 'Position', ps_v)
        elif db2 != False:
            db5 = f.search(db2, 'Position', ps_v)
        elif db1 != False:
            db5 = f.search(db1, 'Position', ps_v)
        else:
            db5 = f.search(database, 'Position', ps_v)

        if db5 != False:
            db6 = f.search_num(db5, 'Transfer Value', tv_v1, tv_v2)
        elif db4 != False:
            db6 = f.search_num(db4, 'Transfer Value', tv_v1, tv_v2)
        elif db3 != False:
            db6 = f.search_num(db3, 'Transfer Value', tv_v1, tv_v2)
        elif db2 != False:
            db6 = f.search_num(db2, 'Transfer Value', tv_v1, tv_v2)
        elif db1 != False:
            db6 = f.search_num(db1, 'Transfer Value', tv_v1, tv_v2)
        else:
            db6 = f.search_num(database, 'Transfer Value', tv_v1, tv_v2)

        if db6 != False:
            db7 = f.search_date(db6, 'Contract expiry date', d_v1, d_v2)
        elif db5 != False:
            db7 = f.search_date(db5, 'Contract expiry date', d_v1, d_v2)
        elif db4 != False:
            db7 = f.search_date(db4, 'Contract expiry date', d_v1, d_v2)
        elif db3 != False:
            db7 = f.search_date(db3, 'Contract expiry date', d_v1, d_v2)
        elif db2 != False:
            db7 = f.search_date(db2, 'Contract expiry date', d_v1, d_v2)
        elif db1 != False:
            db7 = f.search_date(db1, 'Contract expiry date', d_v1, d_v2)
        else:
            db7 = f.search_date(database, 'Contract expiry date', d_v1, d_v2)

        if db7 != False:
            db8 = f.search_num(db7, 'Salary', s_v1, s_v2)
        elif db6 != False:
            db8 = f.search_num(db6, 'Salary', s_v1, s_v2)
        elif db5 != False:
            db8 = f.search_num(db5, 'Salary', s_v1, s_v2)
        elif db4 != False:
            db8 = f.search_num(db4, 'Salary', s_v1, s_v2)
        elif db3 != False:
            db8 = f.search_num(db3, 'Salary', s_v1, s_v2)
        elif db2 != False:
            db8 = f.search_num(db2, 'Salary', s_v1, s_v2)
        elif db1 != False:
            db8 = f.search_num(db1, 'Salary', s_v1, s_v2)
        else:
            db8 = f.search_num(database, 'Salary', s_v1, s_v2)

        db = {}
        if db8 is not False:
            db = db8
        elif db7 is not False:
            db = db7
        elif db6 is not False:
            db = db6
        elif db5 is not False:
            db = db5
        elif db4 is not False:
            db = db4
        elif db3 is not False:
            db = db3
        elif db2 is not False:
            db = db2
        elif db1 is not False:
            db = db1

        u = len(db)


        filter2 = t.Tk()
        filter2.title("Filter")
        filter2.geometry('800x750')
        def myfunction3(event):
            """
                                    Входные параметров нет
                                    Выходных параметров нет
                                    Функция обозначения размера экрана для скролла
                                    Автор: Рыльников А.М.
                                    """
            canvas.configure(scrollregion=canvas.bbox("all"), width=filter2.winfo_screenwidth() - 90,
                             height=filter2.winfo_screenheight() - 90)
            # создание скроллов
        myframe = t.Frame(filter2, relief=t.GROOVE, width=50, height=100, bd=2)
        myframe.place(x=1, y=1)
        canvas = t.Canvas(myframe)
        se = t.Frame(canvas)
        myscrollbar2 = t.Scrollbar(myframe, orient="vertical", command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar2.set)
        myscrollbar2.pack(side="right", fill="y")
        myscrollbar3 = t.Scrollbar(myframe, orient="horizontal", command=canvas.xview)
        canvas.configure(xscrollcommand=myscrollbar3.set)
        myscrollbar3.pack(side="bottom", fill="x")
        canvas.pack(side="left")
        canvas.create_window((0, 0), window=se, anchor='nw')
        se.bind("<Configure>", myfunction3)

        if u == 0:
            bas = t.Label(se, text=' No such items', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                          font=(par['font'], '40', 'bold'))
            bas.grid(row=0, column=0, sticky=t.NSEW)
        else:
            bas = t.Label(se, text=' Number', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                          font=(par['font'], par['letter_size_h1'], 'bold'))
            bas.grid(row=0, column=0, sticky=t.NSEW)
            for i in range(len(db)):
                bas = t.Label(se, text=' %s ' % (i + 1), relief=t.GROOVE, bg=par['table_colour_high'],
                              fg=par['letter_colour'],
                              font=(par['font'], par['letter_size_h1'], 'bold'))
                bas.grid(row=i + 1, column=0, sticky=t.NSEW)

            # Названия столбцов
            bas = t.Label(se, text=' Key ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                          font=(par['font'], par['letter_size_h1'], 'bold'))
            bas.grid(row=0, column=1, sticky=t.NSEW)
            for l in db.keys():
                for i, j in enumerate(db[l]):
                    bas = t.Label(se, text='  %s  ' % j, relief=t.GROOVE, bg=par['table_colour_high'],
                                  fg=par['letter_colour'],
                                  font=(par['font'], par['letter_size_h1'], 'bold'))
                    bas.grid(row=0, column=i + 2, sticky=t.NSEW)
                break

            # Вывод данных
            lis = [2, 3, 4, 5, 6, 7, 8, 9]
            j = 1

            for k in db.keys():
                bas = t.Label(se, text=' %s ' % k, relief=t.GROOVE, bg=par['table_colour'], fg=par['letter_colour'],
                              font=(par['font'], par['letter_size']))
                bas.grid(row=j, column=1, sticky=t.NSEW)
                for i, item in zip(lis, db[k].values()):
                    bas = t.Label(se, text=' %s ' % item, relief=t.GROOVE, bg=par['table_colour'], fg=par['letter_colour'],
                                  font=(par['font'], par['letter_size']))
                    bas.grid(row=j, column=i, sticky=t.NSEW)

                j += 1


        root.bind_all('<MouseWheel>', lambda event: rollWheel(event))
        root.update()
        filter2.mainloop()


def settings(*args):
    """
                            Входные параметров нет
                            Выходных параметров нет
                            Функция настрек интерфейса
                            Автор: Яценко И.Ю.
                            """
    # загрузка параметров
    par = pk.load(open('parametrs.pic', mode='rb'))
    # создание окна
    rt = t.Tk()
    rt.title("Settings")
    rt.geometry('1300x250')
    def myfunction2(event):
        """
                                Входные параметров нет
                                Выходных параметров нет
                                Функция обозначения размера экрана для скролла
                                Автор: Яценко И.Ю.
                                """
        canvas.configure(scrollregion=canvas.bbox("all"), width=rt.winfo_screenwidth() - 90,
                         height=rt.winfo_screenheight() - 90)

    # создание скроллов
    myframe = t.Frame(rt, relief=t.GROOVE, width=50, height=100, bd=2)
    myframe.place(x=1, y=1)
    canvas = t.Canvas(myframe)
    se = t.Frame(canvas)
    myscrollbar2 = t.Scrollbar(myframe, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar2.set)
    myscrollbar2.pack(side="right", fill="y")
    myscrollbar3 = t.Scrollbar(myframe, orient="horizontal", command=canvas.xview)
    canvas.configure(xscrollcommand=myscrollbar3.set)
    myscrollbar3.pack(side="bottom", fill="x")
    canvas.pack(side="left")
    canvas.create_window((0, 0), window=se, anchor='nw')
    se.bind("<Configure>", myfunction2)

    # ВЫБОР ПУТИ К ТЕКСТОВОМУ ФАЙЛУ ЗАПИСИ
    puti = t.Label(se, text=' Way to text file for totals: ', font=('12'))
    puti.grid(row=0, column=0, columnspan=2, sticky=t.NSEW)
    way = t.Label(se, text = '%s' % par['way_to_total'] ,font=('arial', '8'), fg='black', width=65, height=2)
    way.grid(row=1, column=0, sticky=t.NSEW)
    def s1():
        """
                                Входные параметров нет
                                Выходных параметров нет
                                Функция выбора пути к файлу записи итогов
                                Автор: Яценко И.Ю.
                                """
        par = pk.load(open('parametrs.pic', mode='rb'))

        fi = fd.askopenfilename()
        if fi == '' or fi[-3:] != 'txt':
            mb.showerror("Error",
                         "File error\nChoose file\nYou can choose only 'txt' file")
        else:
            par['way_to_total'] = fi
            pk.dump(par, open('parametrs.pic', mode='wb'))
            par = pk.load(open('parametrs.pic', mode='rb'))
            way = t.Label(se, text='%s' % par['way_to_total'], font=('arial', '8'), fg='black', width=65, height=1)
            way.grid(row=1, column=0, sticky=t.NSEW)
    sett = t.Button(se, text="Open..", width=45, height=1,
                    font=('arial', '9'), command=s1)
    sett.grid(row=1, column=1, sticky=t.NSEW)

    # ВЫБОР ТИПА ШРИФТА И ЕГО РАЗМЕРОВ
    fn = t.StringVar(se)
    fn.set(par['font'])
    puti = t.Label(se, text=' Font (current font: %s): ' % par['font'], font=('12'))
    puti.grid(row=2, column=0, sticky=t.NSEW)
    opm7 = t.OptionMenu(se, fn, 'arial', 'times new roman', 'calibri', 'arial black', 'mv boli',
                        'cambria', 'gothic', 'cursive', 'lucida console', 'segoe script', 'webdings', 'txt', 'stylus bt')
    opm7.grid(row=3, column=0, sticky=t.NSEW)

    fn1 = t.StringVar(se)
    fn1.set(par['letter_size'])
    puti = t.Label(se, text=' Table items font size(current size: %s): ' % par['letter_size'], font=('12'))
    puti.grid(row=2, column=1, sticky=t.NSEW)
    opm9 = t.OptionMenu(se, fn1, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                        '17', '18', '19', '20', '21', '22')
    opm9.grid(row=3, column=1, sticky=t.NSEW)

    fn2 = t.StringVar(se)
    fn2.set(par['letter_size_h1'])
    puti = t.Label(se, text=' Font size(current size: %s): ' % par['letter_size_h1'], font=('12'))
    puti.grid(row=4, column=0, sticky=t.NSEW)
    opm11 = t.OptionMenu(se, fn2, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                        '17', '18', '19', '20', '21', '22')
    opm11.grid(row=5, column=0, sticky=t.NSEW)

    fn3 = t.StringVar(se)
    fn3.set(par['letter_size_h2'])
    puti = t.Label(se, text=' Head font size(current size: %s): ' % par['letter_size_h2'], font=('12'))
    puti.grid(row=4, column=1, sticky=t.NSEW)
    opm12 = t.OptionMenu(se, fn3, '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16',
                         '17', '18', '19', '20', '21', '22')
    opm12.grid(row=5, column=1, sticky=t.NSEW)

    # ВЫБОР ЦВЕТОВ ФОНА, ТАБЛИЦЫ, ФУНКЦИЙ, КНОПОК И ШРИФТА
    def getCol(k, i, j):
        """
                                Входные k - ключ словаря к данным параметров, i - строка, j - столбец
                                Выходных параметров нет
                                Функция выбора цвета
                                Автор: Рыльников А.М.
                                """
        rgb, col = cl.askcolor()
        par[k] = col
        pk.dump(par, open('parametrs.pic', mode='wb'))
        puti = t.Label(se, text='  ', font=('12'), bg=par[k], width=5)
        puti.grid(row=i, column=j, sticky=t.NSEW)
    puti = t.Label(se, text='    ', font=('12'))
    puti.grid(row=0, column=2, sticky=t.NSEW)

    puti = t.Label(se, text=' Colours ', font=('12'))
    puti.grid(row=0, column=3,columnspan=3, sticky=t.NSEW)

    puti = t.Label(se, text=' Background colour: ', font=('12'))
    puti.grid(row=1, column=3, sticky=t.NSEW)
    puti = t.Label(se, text='  ', font=('12'), bg=par['frame_colour'], width=5)
    puti.grid(row=1, column=4, sticky=t.NSEW)
    ch = t.Button(se, text="Choose..", width=20, height=1,
                    font=('arial', '9'), command=lambda k='table_colour', i=1, j=4: getCol('frame_colour', 1, 4))
    ch.grid(row=1, column=5, sticky=t.NSEW)

    puti = t.Label(se, text=' Table colour: ', font=('12'))
    puti.grid(row=2, column=3, sticky=t.NSEW)
    puti = t.Label(se, text='  ', font=('12'), bg=par['table_colour'], width=5)
    puti.grid(row=2, column=4, sticky=t.NSEW)
    ch = t.Button(se, text="Choose..", width=20, height=1,
                  font=('arial', '9'), command=lambda k='table_colour', i=2, j=4: getCol('table_colour', 2, 4))
    ch.grid(row=2, column=5, sticky=t.NSEW)

    puti = t.Label(se, text=' Functions and table head colour: ', font=('12'))
    puti.grid(row=3, column=3, sticky=t.NSEW)
    puti = t.Label(se, text='  ', font=('12'), bg=par['table_colour_high'], width=5)
    puti.grid(row=3, column=4, sticky=t.NSEW)
    ch = t.Button(se, text="Choose..", width=20, height=1,
                  font=('arial', '9'), command=lambda k='table_colour_high', i=3, j=4: getCol('table_colour_high', 3, 4))
    ch.grid(row=3, column=5, sticky=t.NSEW)

    puti = t.Label(se, text=' Letter colour: ', font=('12'))
    puti.grid(row=4, column=3, sticky=t.NSEW)
    puti = t.Label(se, text='  ', font=('12'), bg=par['letter_colour'], width=5)
    puti.grid(row=4, column=4, sticky=t.NSEW)
    ch = t.Button(se, text="Choose..", width=20, height=1,
                  font=('arial', '9'),
                  command=lambda k='letter_colour', i=4, j=4: getCol('letter_colour', 4, 4))
    ch.grid(row=4, column=5, sticky=t.NSEW)

    puti = t.Label(se, text=' Buttons colour: ', font=('12'))
    puti.grid(row=5, column=3, sticky=t.NSEW)
    puti = t.Label(se, text='  ', font=('12'), bg=par['button_colour'], width=5)
    puti.grid(row=5, column=4, sticky=t.NSEW)
    ch = t.Button(se, text="Choose..", width=20, height=1,
                  font=('arial', '9'),
                  command=lambda k='button_colour', i=5, j=4: getCol('button_colour', 5, 4))
    ch.grid(row=5, column=5, sticky=t.NSEW)
    def s2():
        """
                                Входные параметров нет
                                Выходных параметров нет
                                Функция сохранения настроек и перезапуска программы
                                Автор: Рыльников А.М.
                                """
        par = pk.load(open('parametrs.pic', mode='rb'))
        par['font'] = fn.get()
        par['letter_size'] = fn1.get()
        par['letter_size_h1'] = fn2.get()
        par['letter_size_h2'] = fn3.get()
        pk.dump(par, open('parametrs.pic', mode='wb'))
        python = sys.executable
        os.execl(python, python, *sys.argv)
    fnt = t.Button(se, text="Save and Reset", width=45, height=2, bg = 'light grey',
                   font=('arial', '12', 'bold'), command=s2)
    fnt.grid(row=8, column=0, columnspan=6, sticky=t.NSEW)


def myfunction(event):
    """
                                    Входные параметров нет
                                    Выходных параметров нет
                                    Функция обозначения размера экрана для скролла
                                    Автор: Яценко И.Ю.
                                    """
    canvas.configure(scrollregion=canvas.bbox("all"),width=root.winfo_screenwidth()-90, height=root.winfo_screenheight()-90)


def rollWheel(event):
    """
                                       Входные параметров нет
                                       Выходных параметров нет
                                       Скролл колесом мыши
                                       Автор: Рыльников А.М.
                                       """
    direction = 0
    if event.delta == -120:
     direction = 1
    if event.delta == 120:
     direction = -1
    canvas.yview_scroll(direction, t.UNITS)


''' ИНТЕРФЕЙС Автор: Петин Д.М. '''


root = t.Tk()

root.title("Database")  # ЗАГОЛОВОК ОКНА
root.configure(bg=par['frame_colour'])
root.geometry('1170x670')
myframe=t.Frame(root,relief=t.GROOVE,width=50,height=100,bd=2)
myframe.place(x=1, y=1)

# СОЗДАНИЕ СКРОЛЛОВ
canvas=t.Canvas(myframe , bg=par['frame_colour'])
frame=t.Frame(canvas, bg=par['frame_colour'])
myscrollbar=t.Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)
myscrollbar.pack(side="right",fill="y")
myscrollbar1=t.Scrollbar(myframe,orient="horizontal",command=canvas.xview)
canvas.configure(xscrollcommand=myscrollbar1.set)
myscrollbar1.pack(side="bottom",fill="x")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)

# Вывод базы данных
# ГЛАВНЫЕ ФРЕЙМЫ
f1 = t.Frame(frame, width=250,height=200,bg=par['frame_colour'], bd=2)
f1.grid(row=0, column=0, sticky=t.NSEW)

fra2 = t.Frame(frame , width=250,height=200,bg=par['frame_colour'], bd=2)
fra2.grid(row=0, column=1, sticky=t.NSEW)

# ФРЕЙМ С КНОПКАМИ ЗАГРУЗКИ,ПЕЧАТИ,ОЧИСТКИ И НАСТРОЕК

fra1 = t.Frame(f1, width=250,height=200,bg=par['frame_colour'], bd=2)
fra1.grid(row=0, column=0, sticky=t.NSEW)

# ФРЕЙМ С БАЗОЙ
basafr = t.Frame(f1,width=250,height=200,bg=par['frame_colour'], bd=2)
basafr.grid(row=1, column=0, sticky=t.NSEW)

# ФРЕЙМ С ФУНКЦИЯМИ

dele_f = t.Frame(fra2,width=150,height=200,bg=par['frame_colour'], bd=2)
dele_f.grid(row=0, column=0, sticky=t.NSEW)





# КНОПКА ЗАГРУЗКИ БАЗЫ

load = t.Button(fra1, text="Load base", width=30, height=1, bg=par['button_colour'], fg=par['letter_colour'],
    font=(par['font'], par['letter_size_h1'], 'bold'), command=load)
load.grid(row=0, column=0, sticky=t.NSEW)

# КНОПКА ПЕЧАТИ БАЗЫ

prnt = t.Button(fra1, text="Print base", width=29, height=1, bg=par['button_colour'], fg=par['letter_colour'],
    font=(par['font'], par['letter_size_h1'], 'bold'), command=print_butt, state='disabled')
prnt.grid(row=0, column=1, sticky=t.NSEW)

# КНОПКА ОЧИСТКИ БАЗЫ

clr = t.Button(fra1, text="Clear base", width=29, height=1, bg=par['button_colour'], fg=par['letter_colour'],
    font=(par['font'], par['letter_size_h1'], 'bold'), command=lambda fra=basafr: clear_base(basafr), state='disabled')
clr.grid(row=0, column=2, sticky=t.NSEW)

# КНОПКА НАСТРОЕК

sett = t.Button(fra1, text="Settings", width=29, height=1, bg=par['button_colour'], fg=par['letter_colour'],
    font=(par['font'], par['letter_size_h1'], 'bold'), command=settings)
sett.grid(row=0, column=3, sticky=t.NSEW)

# КНОПКА ВОЗВРАЩЕНИЯ СТАНДАРТНОЙ БАЗЫ

defa = t.Button(dele_f, text="Return Defaults", width=20, height=2, bg=par['button_colour'], fg=par['letter_colour'],
    font=(par['font'], par['letter_size_h1'], 'bold'), command=defaults, state='disabled')
defa.grid(row=0, column=0, columnspan=2, sticky=t.NSEW)



# ВИДЖЕТ ДОБАВЛЕНИЯ ЭЛЕМЕНТОВ

adit = t.Label(dele_f, text=' \nInput data for new item:\n ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h2'], 'bold'))
adit.grid(row=1, column=0, columnspan=2, sticky=t.NSEW)

# ИМЯ
adit = t.Label(dele_f, text=' Name: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
adit.grid(row=2, column=0, sticky=t.NSEW)
nam = t.Entry(dele_f, width=30, bd=8)
nam.grid(row=2, column=1, sticky=t.NSEW)

# СТРАНА
adit = t.Label(dele_f, text=' Nation: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
adit.grid(row=3, column=0, sticky=t.NSEW)
nat = t.Entry(dele_f, width=20, bd=8)
nat.grid(row=3, column=1, sticky=t.NSEW)

# ВОЗРАСТ
adit = t.Label(dele_f, text=' Age: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
adit.grid(row=4, column=0, sticky=t.NSEW)
age1 = t.Entry(dele_f, width=20, bd=8)
age1.grid(row=4, column=1, sticky=t.NSEW)

# КЛУБ
adit = t.Label(dele_f, text=' Club: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
adit.grid(row=5, column=0, sticky=t.NSEW)
clu = t.Entry(dele_f, width=20, bd=8)
clu.grid(row=5, column=1, sticky=t.NSEW)

# ПОЗИЦИЯ
adit = t.Label(dele_f, text=' Position: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
adit.grid(row=6, column=0, sticky=t.NSEW)
pos = t.StringVar()
opm2=t.OptionMenu(dele_f, pos, 'Forward', 'Winger', 'Attacking Midfielder', 'Defending Midfielder',
                  'Left Defender', 'Center Defender', 'Right Defender', 'Goalkeeper')
opm2.grid(row=6, column=1, sticky=t.NSEW)

# СТОИМОСТЬ
adit = t.Label(dele_f, text=' Value: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
adit.grid(row=7, column=0, sticky=t.NSEW)
val = t.Entry(dele_f, width=20, bd=8)
val.grid(row=7, column=1, sticky=t.NSEW)

# ДАТА ИСТЕЧЕНИЯ КОНТРАКТА
adit = t.Label(dele_f, text=' Contract expire date: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
adit.grid(row=8, column=0, sticky=t.NSEW)
exp = t.StringVar()
opm3 = t.OptionMenu(dele_f, exp, '30.06.2018', '30.06.2019', '30.06.2020', '30.06.2021',
                        '30.06.2022', '30.06.2023', '30.06.2024', '30.06.2026', '30.06.2027', '30.06.2028', '30.06.2029')
opm3.grid(row=8, column=1, sticky=t.NSEW)

# ЗАРПЛАТА
adit = t.Label(dele_f, text=' Salary : ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
adit.grid(row=9, column=0, sticky=t.NSEW)
sal = t.Entry(dele_f, width=20, bd=8)
sal.grid(row=9, column=1, sticky=t.NSEW)

# КНОПКА ДОБАВЛЕНИЯ
ad = t.Button(dele_f, text="Add item", width=20, height=2, bg=par['button_colour'], fg=par['letter_colour'],
    font=(par['font'], par['letter_size_h1'], 'bold'), command=add, state='disabled')
ad.grid(row=10, column=0, columnspan=2, sticky=t.NSEW)

# ВИДЖЕТ ФИЛЬТРА

fil = t.Label(dele_f, text='\n Filter: \n', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
fil.grid(row=11, column=0,columnspan=4, sticky=t.NSEW)

fil = t.Label(dele_f, text='\n Column: \n', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
fil.grid(row=12, column=0,  sticky=t.NSEW)
fil = t.Label(dele_f, text='\n Operation: \n', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
fil.grid(row=12, column=1,  sticky=t.NSEW)
fil = t.Label(dele_f, text='\n Value1: \n', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
fil.grid(row=12, column=2,  sticky=t.NSEW)
fil = t.Label(dele_f, text='\n Value2: \n', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
fil.grid(row=12, column=3, sticky=t.NSEW)

#NAME
fil = t.Label(dele_f, text=' Name: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
fil.grid(row=13, column=0, columnspan=2, sticky=t.NSEW)

nama = t.Entry(dele_f, width=20, bd=8)
nama.grid(row=13, column=2, columnspan=2, sticky=t.NSEW)

#Nationality
fil = t.Label(dele_f, text=' Nationality ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
fil.grid(row=14, column=0, columnspan=2, sticky=t.NSEW)


nata = t.Entry(dele_f, width=20, bd=8)
nata.grid(row=14, column=2, columnspan=2, sticky=t.NSEW)

#AGE
fil = t.Label(dele_f, text=' Age: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
fil.grid(row=15, column=0, columnspan=2, sticky=t.NSEW)

a11 = t.Entry(dele_f, width=15, bd=8)
a11.grid(row=15, column=2, sticky=t.NSEW)
a12 = t.Entry(dele_f, width=15, bd=8)
a12.grid(row=15, column=3, sticky=t.NSEW)

#Club
fil = t.Label(dele_f, text=' Club: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
fil.grid(row=16, column=0, columnspan=2, sticky=t.NSEW)

cl3 = t.Entry(dele_f, width=20, bd=8)
cl3.grid(row=16, column=2, columnspan=2, sticky=t.NSEW)

#Position
fil = t.Label(dele_f, text=' Postion: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
fil.grid(row=17, column=0, columnspan=2, sticky=t.NSEW)
pos12 = t.StringVar()
pos123=t.OptionMenu(dele_f, pos12, '',  'Forward', 'Winger', 'Attacking Midfielder', 'Defending Midfielder',
                  'Left Defender', 'Center Defender', 'Right Defender', 'Goalkeeper')
pos123.grid(row=17, column=2, columnspan=2, sticky=t.NSEW)

#Transfer value
fil = t.Label(dele_f, text=' Transfer value: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
fil.grid(row=18, column=0, columnspan=2, sticky=t.NSEW)
tv2 = t.StringVar()

t11 = t.Entry(dele_f, width=15, bd=8)
t11.grid(row=18, column=2, sticky=t.NSEW)
t12 = t.Entry(dele_f, width=15, bd=8)
t12.grid(row=18, column=3, sticky=t.NSEW)

#Contract
fil = t.Label(dele_f, text=' Contract expire date: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
fil.grid(row=19, column=0,columnspan=2, sticky=t.NSEW)
dt2 = t.StringVar()

d11 = t.StringVar()
data11 = t.OptionMenu(dele_f, d11, '',  '30.06.2018', '30.06.2019', '30.06.2020', '30.06.2021',
                        '30.06.2022', '30.06.2023', '30.06.2024', '30.06.2026', '30.06.2027', '30.06.2028', '30.06.2029')
data11.grid(row=19, column=2, sticky=t.NSEW)
d12 = t.StringVar()
data12 = t.OptionMenu(dele_f, d12, '', '30.06.2018', '30.06.2019', '30.06.2020', '30.06.2021',
                        '30.06.2022', '30.06.2023', '30.06.2024', '30.06.2026', '30.06.2027', '30.06.2028', '30.06.2029')
data12.grid(row=19, column=3, sticky=t.NSEW)

#Salary
fil = t.Label(dele_f, text=' Salary: ', relief=t.GROOVE, bg=par['table_colour_high'], fg=par['letter_colour'],
                  font=(par['font'], par['letter_size_h1'], 'bold'))
fil.grid(row=20, column=0,columnspan=2, sticky=t.NSEW)

sl11 = t.Entry(dele_f, width=15, bd=8)
sl11.grid(row=20, column=2, sticky=t.NSEW)
sl12 = t.Entry(dele_f, width=15, bd=8)
sl12.grid(row=20, column=3, sticky=t.NSEW)


fltr = t.Button(dele_f, text="Filter", width=20, height=2, bg=par['button_colour'], fg=par['letter_colour'],
    font=(par['font'], par['letter_size_h1'], 'bold'), command=serch, state='disabled')
fltr.grid(row=21, column=0, columnspan=2, sticky=t.NSEW)

def clean():
    """
                                       Входные параметров нет
                                       Выходных параметров нет
                                       Очистка полей фильтра
                                       Автор: Яценко И.Ю.
                                       """
    nama.delete(0,t.END)
    sl11.delete(0, t.END)
    sl12.delete(0, t.END)
    t11.delete(0, t.END)
    t12.delete(0, t.END)
    cl3.delete(0, t.END)
    a11.delete(0, t.END)
    a12.delete(0, t.END)
    nata.delete(0, t.END)
    d11.set('')
    d12.set('')
    pos12.set('')
cl1 = t.Button(dele_f, text="Clear", width=20, height=2, bg=par['button_colour'], fg=par['letter_colour'],
    font=(par['font'], par['letter_size_h1'], 'bold'), command=clean)
cl1.grid(row=21, column=2, columnspan=2, sticky=t.NSEW)
root.bind_all('<MouseWheel>', lambda event: rollWheel(event))
root.update()
root.mainloop()
