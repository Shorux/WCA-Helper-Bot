SQLALCHEMY_URL = 'sqlite+aiosqlite:///bot/database/db.sqlite3'

_ = {
    'please_set_wcaid': ('Тебе нужно зарегистрировать свой WCA ID с помощью команды:\n'
                        '`/set` wca\_id\n'
                        'Вместо wca\_id напиши WCA ID\n'
                        'Потом можно использовать команду `/me`'),
    'statistic': ('👤*Имя*: {name}\n🆔*WCA ID*: {wca_id}\n\n'
                '🌐*Рекорды*:\n'
                '       WR: {wrs}, CR: {crs}, NR: {nrs}\n\n'
                '🎖*Медали*:\n'
                '       🥇: {gold}, 🥈: {silver}, 🥉: {bronze}\n\n'
                '🏆*Личные рекорды*:\n{personal_records}'),
    'personal_record': ('\n        {type} 🫴  *{best}* ⚡️\n'
                        '            NR: {country_rank}, CR: {continent_rank}, WR: {world_rank}'),
    'wrong_wcaid': 'Неправильный WCA ID🍼',
    'register_wcaid': 'Зарегистрировал твой WCA ID🍼'
}
