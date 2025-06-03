# Документация проекта "Final_project"

## Автоматизация тестирования на python

### Стек:
- pytest (Основной язык программирования для написания тестов)
- selenium (Библиотека для автоматизации взаимодействия с веб-браузером)
- requests (Фреймворк для написания и запуска тестов)
- allure (Инструмент для генерации отчетов о выполнении тестов)

### Форматирование кода

- Код форматируется в соответствии с PEP 8 (стиль написания кода на Python).
- Все шаги теста размечаются с помощью `@allure.step` или `with allure.step` для улучшения читаемости отчетов.

### Шаги
1. Склонировать проект 'git clone https://github.com/Diana-Bazdyreva/Final-project.git
2. Установить зависимости
3. Запустить тесты 'pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'


### Библиотеки (!)
- pyp install pytest
- pip install selenium
- pip3 install allure-pytest

### Ссылка на финальный проект: 
- тест-план финального проекта: https://beshtau.yonote.ru/share/e12a6d60-938e-42f7-a4b2-635a114b8902
- отчет о тестировании финального проекта: https://beshtau.yonote.ru/share/2ff41495-7e2b-4601-9b58-46c96641cd99