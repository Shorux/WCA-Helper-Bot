```
██╗    ██╗ ██████╗ █████╗     ██╗  ██╗███████╗██╗     ██████╗ ███████╗██████╗     ██████╗  ██████╗ ████████╗
██║    ██║██╔════╝██╔══██╗    ██║  ██║██╔════╝██║     ██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝
██║ █╗ ██║██║     ███████║    ███████║█████╗  ██║     ██████╔╝█████╗  ██████╔╝    ██████╔╝██║   ██║   ██║   
██║███╗██║██║     ██╔══██║    ██╔══██║██╔══╝  ██║     ██╔═══╝ ██╔══╝  ██╔══██╗    ██╔══██╗██║   ██║   ██║   
╚███╔███╔╝╚██████╗██║  ██║    ██║  ██║███████╗███████╗██║     ███████╗██║  ██║    ██████╔╝╚██████╔╝   ██║   
 ╚══╝╚══╝  ╚═════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝    ╚═╝ 
```

# WCA Helper Bot
Это бот для телеграм.

Он помогает [спидкуберам](https://www.youtube.com/watch?v=1oZY2e25VUw&t=10s, 'Кто такие спидкуберы?') следить за своими официальными результатами по спидкубингу из сайта [WorldCubingAssociation](https://www.worldcubeassociation.org/)

Мой профиль в сайте WCA (кликните на фото):

[<img src="https://avatars.worldcubeassociation.org/uploads/user/avatar/2021TOLI01/1689360886.jpg" width="300" border=1px/>](https://www.worldcubeassociation.org/persons/2021TOLI01)

## Как запустить бота?
Сперва создаём файлик `.env` в главном каталоге.

Внутри этого файла пишем:
```env
TOKEN='Сюда вставьте ваш токен бота'
```

Далее в терминале находясь в каталоге с ботом запускаем:
```python
python3 -m venv .venv

.venv\Scripts\activate #- для Windows;
source .venv\bin\activate #- для Linux и MacOS.

pip install -r requirements.txt
python3 app.py
```
____
### Библиотеки использованные в проекте:
![PyPI - Version](https://img.shields.io/pypi/v/aiogram?style=flat-square&label=aiogram)
![PyPI - Version](https://img.shields.io/pypi/v/aiohttp?label=aiohttp)
![PyPI - Version](https://img.shields.io/pypi/v/sqlalchemy?style=flat-square&label=sqlalchemy)
![PyPI - Version](https://img.shields.io/pypi/v/python-dotenv?label=python-dotenv)
