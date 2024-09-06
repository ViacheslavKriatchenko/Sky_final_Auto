# Sky_final_Auto

## Разработка шаблона на примере тестирования сайта Кинопоиск
На момент написания, тесты находят реальные баги как со стороны UI, так и API и тесты падают.

### Шаги:
1. Склонировать репозитой "git clone https://github.com/ViacheslavKriatchenko/Sky_final_Auto.git"
2. Запустить виртуальное окружение "python -m venv venv"
3. Установить окружение "python -m pip install -r requirements.txt"
4. Запустить тесты

### Стэк:
- Selenium
- Webdriver-manager
- Requests
- PyTest
- Allure

### Структура:
- ./api - методы для работы с API
- ./config - настройка конфигурации
    - config_page.py - конструктор страниц
    - ConfigProvider.py - глобальные настройки
- ./pages - описание страниц сайта
- ./tests - тесты
    - test_API.py - API тесты
    - test_UI.py - UI тесты
- ./userdata - провайдер пользовательских данных
    - DataProvider.py
- conftest.py - фикстуры
- global_options.ini - глобальные переменные
- pytest.ini - настройка тестов
- requirements.txt - настройка окружения
- user_data.json - пользовательские данные

### Полезные ссылки:
[Гайд по Markdown](https://www.markdownguide.org/basic-syntax/)  
[Сайт генератор .gitignore](https://www.toptal.com/developers/gitignore)  
[Перенос окружения](https://pip.pypa.io/en/stable/cli/pip_freeze/)  
[Вызов PyTest инструкция](https://pytest-docs-ru.readthedocs.io/ru/latest/usage.html)

### Библиотеки:
- pip install selenium
- pip install webdriver-manager
- pip install pytest
- pip install requests
- pip install allure-pytest
