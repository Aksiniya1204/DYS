Дипломный проект. Вторая часть. Тестирование Яндекс Самокат.
Содержание
Запрос. Список логинов курьеров с количеством их заказов в статусе «В доставке»
Запрос. Трекеры заказов и их статусы
Автотест. Получение данных о заказе по треку
Автоматизация теста к API
Автоматизируй сценарий, который подготовили коллеги-тестировщики:
Клиент создает заказ.
Проверяется, что по треку заказа можно получить данные о заказе.
Шаги автотеста:
1. Выполнить запрос на создание заказа.
2. Сохранить номер трека заказа.
3. Выполнить запрос на получения заказа по треку заказа.
4. Проверить, что код ответа равен 200.

Скриншот результата:
![автотест скрин.png](images/%D0%B0%D0%B2%D1%82%D0%BE%D1%82%D0%B5%D1%81%D1%82%20%D1%81%D0%BA%D1%80%D0%B8%D0%BD.png)

Для проверки запросов к БД через Postman были созданы несколько курьеров и заказов. Для заказов использовались различные статусы: создан, в работе, завершен, отменен.
Для реализации автотеста использовалась среда разработки PyCharm.
Для запуска теста должны быть установлены пакеты pytest и requests.
Запуск теста выполянется командой pytest 