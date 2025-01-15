events_list = ('222', '333', '333fm', '333mbf', '333bf', '333oh', '444',
               '444bf', '555', '555bf', '666', '777', 'clock',
               'skewb', 'pyram', 'minx', 'sq1', '333ft')


class _():
    follow = '@Speedcubes\_uz kanaliga obuna bo\'ling!'
    please_set_wcaid = {
        'en': ('You need to register your WCA ID with the command:\n'
               '`/set` wca\_id\n'
               'Instead of wca\_id write your WCA ID\n'
               'Then you can use the command `/me`'),
        'ru': ('Тебе нужно зарегистрировать свой WCA ID с помощью команды:\n'
               '`/set` wca\_id\n'
               'Вместо wca\_id напиши свой WCA ID\n'
               'Потом можно использовать команду `/me`'),
        'uz': ('Ushbu komanda bilan o\'zingizni WCA ID\'izni registratsiya qilishingiz kerak:\n'
               '`/set` wca\_id\n'
               'wca\_id\'ni o\'rniga WCA ID\'izni yozin\n'
               'Keyin `/me` komandasini ishlatsangiz bo\'ladi\n'
               f'{follow}'),
        'kz': ('Сізге `/set` wca\_id командасы арқылы WCA ID-ңізді тіркеу керек\n'
               'wca\_id сөзінің орнына өзіңіздің WCA ID-ңізді жазыңыз\n'
               'Осыдан кейін `/me` командасын қолдануға болады')
    }
    statistic = {
        'en': ('{gender}*Name*: {name}\n🆔*WCA ID*: {wca_id}\n'
               '🏳️*Country*: {country}\n\n'
               '🌐*Records*:\n'
               '       WR: {wrs}, CR: {crs}, NR: {nrs}\n\n'
               '🎖*Medals*:\n'
               '       🥇: {gold}, 🥈: {silver}, 🥉: {bronze}\n\n'
               '🏆*Personal records*:\n{personal_records}'),
        'ru': ('{gender}*Имя*: {name}\n🆔*WCA ID*: {wca_id}\n'
               '🏳️*Страна*: {country}\n\n'
               '🌐*Рекорды*:\n'
               '       WR: {wrs}, CR: {crs}, NR: {nrs}\n\n'
               '🎖*Медали*:\n'
               '       🥇: {gold}, 🥈: {silver}, 🥉: {bronze}\n\n'
               '🏆*Личные рекорды*:\n{personal_records}'),
        'uz': ('{gender}*Ism*: {name}\n🆔*WCA ID*: {wca_id}\n'
               '🏳️*Mamlakati*: {country}\n\n'
               '🌐*Rekordlar*:\n'
               '       WR: {wrs}, CR: {crs}, NR: {nrs}\n\n'
               '🎖*Medallar*:\n'
               '       🥇: {gold}, 🥈: {silver}, 🥉: {bronze}\n\n'
               '🏆*Shaxsiy rekordlar*:\n{personal_records}'
               f'{follow}'),
        'kz': ('{gender}*Аты*: {name}\n🆔*WCA ID*: {wca_id}\n'
               '🏳️*Мемлекеті*: {country}\n\n'
               '🌐*Рекордтар*:\n'
               '       WR: {wrs}, CR: {crs}, NR: {nrs}\n\n'
               '🎖*Медальдар*:\n'
               '       🥇: {gold}, 🥈: {silver}, 🥉: {bronze}\n\n'
               '🏆*Жеке рекордтар*:\n{personal_records}'),
    }
    
    pr = ('   {type} - *{best}*\n'
          '      NR: {country_rank} | CR: {continent_rank} | WR: {world_rank}\n\n')
    personal_record = {
        'en': pr,
        'ru': pr,
        'uz': pr,
        'kz': pr
    }
    event = {
        'en': '⏱️*Event {event}*:\n\n',
        'ru': '⏱️*Дисциплина {event}*:\n\n',
        'uz': '⏱️*{event} yo\'nalishi*:\n\n',
        'kz': '⏱️*{event} дисциплинасы*:\n\n'
    }
    finded_users = {
        'en': '👥Finded speedcubers:\n',
        'ru': '👥Найденные спидкуберы:\n',
        'uz': '👥Topilgan spidkuberlar:\n',
        'kz': '👥Табылған спидкуберлер тізімі:\n'
    }
    user = {
        'en': ('{gender}Name: {name}\n'
               '       🏳️Country: {country}\n'
               '       🆔WCA ID: `{wcaid}`\n\n'),
        'ru': ('{gender}Имя: {name}\n'
               '       🏳️Страна: {country}\n'
               '       🆔WCA ID: `{wcaid}`\n\n'),
        'uz': ('{gender}Ism: {name}\n'
               '       🏳️Mamlakat: {country}\n'
               '       🆔WCA ID: `{wcaid}`\n\n'),
        'kz': ('{gender}Аты: {name}\n'
               '       🏳️Мемлекет: {country}\n'
               '       🆔WCA ID: `{wcaid}`\n\n')
    }
    not_found = {
        'en': 'No such speedcubers found🍼',
        'ru': 'Не найдено таких спидкуберов🍼',
        'uz': 'Bunday isimlik spidkuberlar topilmadi🍼',
        'kz': 'Бұндай спидкуберлер табылған жоқ🍼'
    }
    wrong_wcaid = {
        'en': 'Wrong WCA ID🍼',
        'ru': 'Неправильный WCA ID🍼',
        'uz': 'Not\'g\'ri WCA ID🍼',
        'kz': 'WCA ID дұрыс емес🍼'
    }
    register_wcaid = {
        'en': 'Registered your WCA ID🍼',
        'ru': 'Зарегистрировал твой WCA ID🍼',
        'uz': 'WCA ID\'izni registratsiya qildim🍼',
        'kz': 'Сіздің WCA ID-іңіз тіркелді🍼'
    }
    choose_lang = {
        'en': 'Choose language🍼',
        'ru': 'Выберите язык🍼',
        'uz': 'Til tanlang🍼',
        'kz': 'Тілді таңдаңыз🍼'
    }
    lang_registred = {
        'en': 'Language registered🍼',
        'ru': 'Язык зарегистрирован🍼',
        'uz': 'Til tanlandi🍼',
        'kz': 'Тіл жаңартылды🍼'
    }
