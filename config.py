SQLALCHEMY_URL = 'sqlite+aiosqlite:///bot/database/db.sqlite3'

events_list = ('222', '333', '333fm', '333mbf', '333bf', '333oh', '444', '444bf'
               '555', '555bf', '666', '777', 'clock', 'skewb', 'pyram', 'minx',
               'sq1', '333ft')

_ = {
    'please_set_wcaid': ('Тебе нужно зарегистрировать свой WCA ID с помощью команды:\n'
                        '`/set` wca\_id\n'
                        'Вместо wca\_id напиши свой WCA ID\n'
                        'Потом можно использовать команду `/me`'),
    'statistic': ('👤*Имя*: {name}\n🆔*WCA ID*: {wca_id}\n\n'
                '🌐*Рекорды*:\n'
                '       WR: {wrs}, CR: {crs}, NR: {nrs}\n\n'
                '🎖*Медали*:\n'
                '       🥇: {gold}, 🥈: {silver}, 🥉: {bronze}\n\n'
                '🏆*Личные рекорды*:\n{personal_records}'),
    'personal_record': ('\n        {type} 🫴  *{best}* ⚡️\n'
                        '            NR: {country_rank}, CR: {continent_rank}, WR: {world_rank}'),
    'event': '🍼*Дисциплина {event}*:',
    'finded_users': '👥Найденные спидкуберы:\n',
    'user': ('{gender}Имя: {name}\n'
            '       🏳️Страна: {country}\n'
            '       🆔WCA ID: {wcaid}\n\n'),
    'not_found': 'Не найдено таких спидкуберов🍼',
    'wrong_wcaid': 'Неправильный WCA ID🍼',
    'register_wcaid': 'Зарегистрировал твой WCA ID🍼'
}
