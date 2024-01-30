SQLALCHEMY_URL = 'sqlite+aiosqlite:///bot/database/db.sqlite3'

stat_string = '''**Имя**: {name}, **WCA ID**: {wca_id}
**Рекорды**: 
    WR:{wrs}, CR:{crs}, NR:{nrs}
**Медали**:
    🥇:{gold}, 🥈:{silver}, 🥉{bronze}
**Личные рекорды**:{personal_records}
'''

_ = {
    'please_set_wcaid': '''**Вам нужно зарегестрировать ваш WCA ID**\
                            с помощью команды:\
                            !set your_wca_id\
                            Вместо your_wca_id напишите ваш WCA ID'''
}
