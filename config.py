SQLALCHEMY_URL = 'sqlite+aiosqlite:///bot/database/db.sqlite3'

_ = {
    'please_set_wcaid': ('Вам нужно зарегистрировать ваш WCA ID\n'
                        'с помощью команды:\n'
                        '`!set` your_wca_id\n'
                        'Вместо your_wca_id напишите ваш WCA ID'),
    'statistic': ('👤*Имя*: {name}\n🆔*WCA ID*: {wca_id}\n\n'
                '🌐*Рекорды*:\n'
                '       WR: {wrs}, CR: {crs}, NR: {nrs}\n\n'
                '🎖*Медали*:\n'
                '       🥇: {gold}, 🥈: {silver}, 🥉: {bronze}\n\n'
                '🏆*Личные рекорды*:\n{personal_records}'),
    'wrong_wcaid': 'Неправильный WCA ID🍼',
    'register_wcaid': 'Зарегистрировал твой WCA ID🍼'
}
