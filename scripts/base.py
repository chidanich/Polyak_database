import sys  # модули sys и os для функции перезагрузки программы
sys.path.append('../library')
import functions as f
# создание оригинальной базы данных
def defa():
    """
                                        Входные параметров нет
                                        Выходных параметров нет
                                        Возвращение оригинальной базы
                                        Автор: Петин Д.М.
                                        """
    def base_fotballers():
        """
                                                Входные параметров нет
                                                Выходных параметров нет
                                                Создание базы
                                                Автор: Петин Д.М.
                                                """
        Promes = {'Name': 'Quincy Promes',
                  'Nationality': 'Netherlands',
                  'Age': 26,
                  'Club': 'Spartak',
                  'Position': 'Winger',
                  'Transfer Value': 22 ,
                  'Contract expiry date': '30.06.2021' ,
                  'Salary': 3.8}
        Smolov = {'Name': 'Fedor Smolov',
                  'Nationality': 'Russia',
                  'Age': 28,
                  'Club': 'FC Krasnodar',
                  'Position': 'Forward',
                  'Transfer Value': 15,
                  'Contract expiry date': '30.06.2019',
                  'Salary': 2.9}
        Kokorin = {'Name': 'Alexandr Kokorin',
                   'Nationality': 'Russia',
                   'Age': 27,
                   'Club': 'Zenit',
                   'Position': 'Forward',
                   'Transfer Value': 11,
                   'Contract expiry date': '30.06.2019',
                   'Salary': 3.3}
        Adriano = {'Name': 'Luis Adriano',
                   'Nationality': 'Brazil',
                   'Age': 30,
                   'Club': 'Spartak',
                   'Position': 'Forward',
                   'Transfer Value': 6,
                   'Contract expiry date': '30.06.2019',
                   'Salary': 3.5}
        Miranchuk = {'Name': 'Alexey Miranchuk',
                     'Nationality': 'Russia',
                     'Age': 22,
                     'Club': 'Lokomotiv',
                     'Position': 'Attacking Midfielder',
                     'Transfer Value': 10,
                     'Contract expiry date': '30.06.2021',
                     'Salary': 1.8}
        Akinfeev = {'Name': 'Igor Akinfeev',
                    'Nationality': 'Russia',
                    'Age': 32,
                    'Club': 'CSKA',
                    'Position': 'Goalkeeper',
                    'Transfer Value': 10,
                    'Contract expiry date': '30.06.2019',
                    'Salary': 2.5}
        Popov = {'Name': 'Ivelin Popov',
                 'Nationality': 'Bulgaria',
                 'Age': 30,
                 'Club': 'Rubin',
                 'Position': 'Attacking Midfielder',
                 'Transfer Value': 3.5,
                 'Contract expiry date': '30.06.2019',
                 'Salary': 1.8}
        MarFernandes = {'Name': 'Mario Fernandes',
                        'Nationality': 'Brazil',
                        'Age': 27,
                        'Club': 'CSKA',
                        'Position': 'Right Defender',
                        'Transfer Value': 16,
                        'Contract expiry date': '30.06.2021',
                        'Salary': 2.2}
        Shatov = {'Name': 'Oleg Shatov',
                  'Nationality' : 'Russia',
                  'Age': 27,
                  'Club': 'Zenit',
                  'Position' : 'Attacking Midfielder',
                  'Transfer Value': 8.5,
                  'Contract expiry date': '30.06.2020',
                  'Salary': 2.5}
        Samedov = {'Name': 'Alexander Samedov',
                   'Nationality': 'Russia',
                   'Age': 33,
                   'Club': 'Spartak',
                   'Position': 'Winger',
                   'Transfer Value': 1.7,
                   'Contract expiry date': '30.06.2019',
                   'Salary': 2.5}
        ManFernandes = {'Name': 'Manuel Fernandes',
                        'Nationality': 'Portugal',
                        'Age': 32,
                        'Club': 'Lokomotiv',
                        'Position': 'Attacking Midfielder',
                        'Transfer Value': 4.5,
                        'Contract expiry date': '30.06.2019',
                        'Salary': 3.8}
        Paredes = {'Name': 'Leandro Paredes',
                   'Nationality': 'Argentina',
                   'Age': 23,
                   'Club': 'Zenit',
                   'Position': 'Defending Midfielder',
                   'Transfer Value': 18,
                   'Contract expiry date': '30.06.2019',
                   'Salary': 5}
        Fernando = {'Name': 'Lukas Fernando',
                    'Nationality': 'Brazil',
                    'Age': 26,
                    'Club': 'Spartak',
                    'Position': 'Defending Midfielder',
                    'Transfer Value': 14,
                    'Contract expiry date': '30.06.2021',
                    'Salary': 2.8}
        Wernbloom = {'Name': 'Pontus Wernbloom',
                     'Nationality': 'Sweden',
                     'Age': 31,
                     'Club': 'CSKA',
                     'Position': 'Defending Midfielder',
                     'Transfer Value': 7.5,
                     'Contract expiry date': '30.06.2018',
                     'Salary': 2}
        Criscito = {'Name': 'Dominico Criscito',
                    'Nationality': 'Italy',
                    'Age': 31,
                    'Club': 'Zenit',
                    'Position': 'Left Defender',
                    'Transfer Value': 5,
                    'Contract expiry date': '30.06.2018',
                    'Salary': 3}
        Corluka = {'Name': 'Vedran Corluka',
                   'Nationality': 'Croatia',
                   'Age': 32,
                   'Club': 'Lokomotiv',
                   'Position': 'Center Defender',
                   'Transfer Value': 4.2,
                   'Contract expiry date': '30.06.2020',
                   'Salary': 4.5}
        Ivanovich = {'Name': 'Branislav Ivanovich',
                   'Nationality': 'Serbia',
                   'Age': 34,
                   'Club': 'Zenit',
                   'Position': 'Center Defender',
                   'Transfer Value': 4,
                   'Contract expiry date': '30.06.2019',
                   'Salary': 4.1}
        Glushakov = {'Name': 'Denis Glushakov',
                     'Nationality': 'Russia',
                     'Age': 31,
                     'Club': 'Spartak',
                     'Position': 'Defending Midfielder',
                     'Transfer Value': 7.5,
                     'Contract expiry date': '30.06.2020',
                     'Salary': 2.6}
        ZeLuis = {'Name': 'Ze Luis',
                  'Nationality': 'Cabo-Verde',
                  'Age': 27,
                  'Club': 'Spartak',
                  'Position': 'Forward',
                  'Transfer Value': 5.5,
                  'Contract expiry date': '30.06.2021',
                  'Salary': 2}
        Kombarov = {'Name': 'Dmitry Kombarov',
                    'Nationality': 'Russia',
                    'Age': 31,
                    'Club': 'Spartak',
                    'Position': 'Left Defender',
                    'Transfer Value': 3.2,
                    'Contract expiry date': '30.06.2020',
                    'Salary': 2}
        Tasci = {'Name': 'Serdar Tasci',
                    'Nationality': 'Germany',
                    'Age': 30,
                    'Club': 'Spartak',
                    'Position': 'Center Defender',
                    'Transfer Value': 2,
                    'Contract expiry date': '30.06.2018',
                    'Salary': 2.2}
        Dzagoev = {'Name': 'Alan Dzagoev',
                   'Nationality': 'Russia',
                   'Age': 27,
                   'Club': 'CSKA',
                   'Position': 'Attacking Midfielder',
                   'Transfer Value': 15,
                   'Contract expiry date': '30.06.2019',
                   'Salary': 2.2}
        Guilherme = {'Name': 'Marinato Guilherme',
                   'Nationality': 'Russia',
                   'Age': 32,
                   'Club': 'Lokomotiv',
                   'Position': 'Goalkeeper',
                   'Transfer Value': 4,
                   'Contract expiry date': '30.06.2019',
                   'Salary': 2}
        Zobnin = {'Name': 'Roman Zobnin',
                  'Nationality': 'Russia',
                  'Age': 24,
                  'Club': 'Spartak',
                  'Position': 'Defending Midfielder',
                  'Transfer Value': 6,
                  'Contract expiry date': '30.06.2021',
                  'Salary': 2.4}
        Granquist = {'Name': 'Andreas Granquist',
                     'Nationality': 'Sweden',
                     'Age': 32,
                     'Club': 'FC Krasnodar',
                     'Position': 'Center Defender',
                     'Transfer Value': 4.5,
                     'Contract expiry date': '30.06.2018',
                     'Salary': 2.4}
        Driussi = {'Name': 'Sebastjan Driussi',
                   'Nationality': 'Argentina',
                   'Age': 22,
                   'Club': 'Zenit',
                   'Position': 'Forward',
                   'Transfer Value': 12,
                   'Contract expiry date': '30.06.2021',
                   'Salary': 2.7}
        Melgarejo = {'Name': 'Lorenzo Melgarejo',
                     'Nationality': 'Paraguay',
                     'Age': 27,
                     'Club': 'Spartak',
                     'Position': 'Winger',
                     'Transfer Value': 3.5,
                     'Contract expiry date': '30.06.2020',
                     'Salary': 2}
        Poloz = {'Name': 'Dmitry Poloz',
                 'Nationality': 'Russia',
                 'Age': 26,
                 'Club': 'Zenit',
                 'Position': 'Winger',
                 'Transfer Value': 7,
                 'Contract expiry date': '30.06.2020',
                 'Salary': 1.8}
        Djanaev = {'Name': 'Soslan Djanaev',
                   'Nationality': 'Russia',
                   'Age': 31,
                   'Club': 'Rubin',
                   'Position': 'Goalkeeper',
                   'Transfer Value': 2.5,
                   'Contract expiry date': '30.06.2020',
                   'Salary': 1.60}
        Kardeniz = {'Name': 'Gokdeniz Kardeniz',
                    'Nationality': 'Turkey',
                    'Age': 38,
                    'Club': 'Rubin',
                    'Position': 'Winger',
                    'Transfer Value': 0.5,
                    'Contract expiry date': '30.06.2018',
                    'Salary': 2.5}
        footballers = {
            1: Promes,
            2: Smolov,
            3: Kokorin,
            4: Adriano,
            5: Miranchuk,
            6: Akinfeev,
            7: Popov,
            8: MarFernandes,
            9: Shatov,
            10: Samedov,
            11: ManFernandes,
            12: Paredes,
            13: Fernando,
            14: Wernbloom,
            15: Criscito,
            16: Corluka,
            17: Ivanovich,
            18: Glushakov,
            19: ZeLuis,
            20: Kombarov,
            21: Tasci,
            22: Dzagoev,
            23: Guilherme,
            24: Zobnin,
            25: Granquist,
            26: Driussi,
            27: Melgarejo,
            28: Poloz,
            29: Djanaev,
            30: Kardeniz,

            }

        return footballers


    base = base_fotballers()
    f.save_file(base)







