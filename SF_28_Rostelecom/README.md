# SF_28_Rostelecom

Автоматизированное тестирование нового интерфейса авторизации в личном кабинете (https://b2c.passport.rt.ru/) 

В проекте использовались библиотеки Selenium и PayTest

Команда для запуска тестов: 
* python -m pytest -v --tb=line tests/test_auth_page.py 
* phon3 -m pytest -v --tb=line tests/test_auth_page.py

Учетных данные для тестирования находятся в файле settings.py

Корневая папка содержит:
* _сhromedriver_
* _conftest.py_
* _README.md_
* _settings.py_
* **pages**
* _auth_page.py_
* _base_page.py_
* _locators.py_
* **tests**
* _test_auth_page.py_



