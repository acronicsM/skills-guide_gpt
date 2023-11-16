# skills-guide_gpt

Сервис проекта skills_guide по взаимодействую с GPT моделями

![](https://img.shields.io/badge/FastAPI-0.104.0-00CED1)
![](https://img.shields.io/badge/AIOHTTP-3.8.6-F0FFFF)
![](https://img.shields.io/badge/g4f-0.1.7.7-DC143C)

## 🛠️ Подготовка в запуску

1. [Download and install Python](https://www.python.org/downloads/) (Version 3.10+ is recommended).

2. Клонируйте репозиторий GitHub:
```bash
git clone https://github.com/acronicsM/skills-guide_gpt.git
```
3. Перейдите в директорию проекта:
```bash
cd skills-guide_gpt
```
4. Установите переменные окружения:
```bash
nano .env
```
5. (Рекомендуется) Создайте виртуальную среду Python::
[Python official documentation](https://docs.python.org/3/tutorial/venv.html).


```
python3 -m venv venv
```

6. Активируйте виртуальную среду:
   - On Windows:
   ```
   .\venv\Scripts\activate
   ```
   - On macOS and Linux:
   ```
   source venv/bin/activate
   ```
7. Установите необходимые пакеты Python из `requirements.txt`:

```
pip install -r requirements.txt
```

8. Запустите `gpt_api/app.py`


## 💡 Использование
После запуска документация API доступа по адресу http://localhost:7000/docs

## 🙌 Необходимы переменные окружения

1. ApiKeyYndx - IAM-токен [YandexGPT documentation](https://cloud.yandex.ru/docs/yandexgpt/quickstart).
2. FolderIDYndx - идентификатор_каталога
3. TemperatureYndx - чем выше значение этого параметра, тем более креативными и случайными будут ответы нейросети. Принимает значения больше 0, включая 0.

