import requests
import allure
from config import AUTH_TOKEN, base_url


@allure.feature("API Кинопоиск")
@allure.story("Поиск фильма по названию")
def test_movie_title_search():
    """
    Проверяет работоспособность API-поиска фильма по названию.
    Ожидаемый результат: Возвращается список фильмов,
    соответствующих указанному названию
    """
    with allure.step("GET-запрос на поиск фильма по названию"):
        params = {"query": "работа без авторства"}
        headers = {"X-KP-API-KEY": AUTH_TOKEN}
        base_url + "/v1.4/movie/search"
        response = requests.get(base_url, params=params, headers=headers)
    with allure.step("Проверка статус-кода на соответствие ожидаемому"):
        assert response.status_code == 200


@allure.feature("API Кинопоиск")
@allure.story("Получение списка жанров фильмов")
def test_getting_list_genre():
    """
    Проверка возможности получения списка жанров фильмов.
      Ожидаемый результат: Возвращение полного списока жанров
    """
    with allure.step("GET-запрос на получение списка жанров"):
        params = {"field": "genres.name"}
        headers = {"X-KP-API-KEY": AUTH_TOKEN}
        base_url + "/v1/movie/possible-values-by-field"
        response = requests.get(base_url, params=params, headers=headers)

    with allure.step("Проверка статус-кода на соответствие ожидаемому"):
        assert response.status_code == 200


@allure.feature("API Кинопоиск")
@allure.story("Получение информации о фильме по ID")
def test_movie_id_search(id="435"):
    """
    Проверка возможности получения детальной информации
    о фильме по ID. Ожидаемый результат: Возвращение информации
    о конкретном фильме
    """
    with allure.step("GET-запрос на получение информации о фильме по ID"):
        headers = {"X-API-KEY": AUTH_TOKEN}
    response = requests.get(f"{base_url}/v1.4/movie/{id}", headers=headers)

    with allure.step("Проверка статус-кода на соответствие ожидаемому"):
        assert response.status_code == 200


@allure.feature("API Кинопоиск")
@allure.story(
    "Негативная проверка на запрос "
    "с невалидным параметром: год выпуска фильма"
)
def test_invalid_year_release():
    """
    Проверка обработки запроса с невалидным
    годом выпуска фильма. Ожидаемый результат: статус-код 400
    """
    with allure.step("GET-запрос с невалидным годом выпуска фильма"):
        params = {
            "page": 1,
            "limit": 10,
            "year": "1850",
        }

    headers = {"X-API-KEY": AUTH_TOKEN}

    response = requests.get(
        base_url + "/v1.4/movie", params=params, headers=headers)
    with allure.step("Проверка соответствия статус-кода ожидаемому"):
        assert response.status_code == 400


@allure.feature("API Кинопоиск")
@allure.story(
    "Негативная проверка обработки "
    "запроса с невалидным параметром: страна производства фильма"
)
def test_invalid_country():
    """
    Проверка обработки запроса с указанием несуществующей страны.
    Ожидаемый результат: Статус-код: 200, длина списка фильмов: 0
    """
    with allure.step(
        "GET-запрос с невалидным параметром:" " страна производства фильма"
    ):
        params = {"page": 1, "limit": 10, "countries.name": "Зурумбия"}
    headers = {"X-API-KEY": AUTH_TOKEN}
    endpoint = base_url + "/v1.4/movie"
    response = requests.get(endpoint, params=params, headers=headers)

    result = response.json()

    with allure.step("Проверка статус-кода на соответствие ожидаемому"):
        assert response.status_code == 200

    with allure.step("Проверка длины списка фильмов"):
        assert len(result.get("docs", [])) == 0
