## Котикова Ксения, 18-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import data

# создание заказа
def post_new_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         headers=data.headers,
                         json=data.order_body)

# получение заказа по номеру трекера
def get_order_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.CREATE_ORDER + '?t=' + str(track),
                        headers=data.headers)

# запрос на получения заказа по треку заказа.
def code_200():
    response_code = post_new_order(data.order_body)
    track = response_code.json()["track"]
    return get_order_track(track).status_code

# Проверка, что код ответа равен 200.
def test_get_order_track_code_200():
    assert code_200() == 200