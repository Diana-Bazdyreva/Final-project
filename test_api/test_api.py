import requests


AUTH_TOKEN = "24K82W5-7PWM7CF-N0MFYK5-1VVXXAW"
base_url = "https://api.kinopoisk.dev"

def test_movie_search():
    """Get запрос 'Поиск фильма по названию'"""
    params = {
        'query': 'работа без авторства'
    }
    headers = {
        'X-KP-API-KEY': AUTH_TOKEN
    }   
    base_url + '/v1.4/movie/search'
    response = requests.get(base_url, params=params, headers=headers)
            # Проверяем статус-код ответа
    assert response.status_code == 200, f'Ошибка: неверный статус-код ({response.status_code})'
        
    
        
        