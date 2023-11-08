from decouple import config

YANDEX_API = config('YANDEX_API', default='')
TELEBOT_API = config('TELEBOT_API', default='')
CHAT_ID = config('CHAT_ID', default='')

# URL = 'https://api.weather.yandex.ru/v2/forecast' # ТЕСТОВЫЙ 

# Ссылка и параметры
URL = 'https://api.weather.yandex.ru/v2/informers'
HEADERS = {'Content-Type': 'application/json', 
           'X-Yandex-API-Key': YANDEX_API,
           }  # Yandex-API-Key

# Широта и долгота г. Воронежа
PARAMS = {'lat': 51.673622, 
          'lon': 39.254372, 
          'lang': 'ru_RU'}

# Погодные условия
CONDITIONS = {'clear': "ясно",
              'partly-cloudy': 'малооблачно',
              'cloudy': 'облачно с прояснениями',
              'overcast': 'пасмурно',
              'light-rain': 'небольшой дождь',
              'rain': 'дождь',
              'heavy-rain': 'сильный дождь',
              'showers': 'ливень',
              'wet-snow': 'дождь со снегом',
              'light-snow': 'небольшой снег',
              'snow': 'снег',
              'snow-showers': 'снегопад',
              'hail': 'град',
              'thunderstorm': 'гроза',
              'thunderstorm-with-rain': 'дождь с грозой',
              'thunderstorm-with-hail': 'гроза с градом'}

# Иконки погодных условий для телеграма
CONDITIONS_ICONS = {'clear': '☀️',
              'partly-cloudy': '🌤',
              'cloudy': '🌥',
              'overcast': '☁️',
              'light-rain': '🌦',
              'rain': '🌧',
              'heavy-rain': '🌧',
              'showers': '🌧',
              'wet-snow': '🌨',
              'light-snow': '🌨',
              'snow': '🌨',
              'snow-showers': '🌨',
              'hail': '🌧',
              'thunderstorm': '🌩',
              'thunderstorm-with-rain': '⛈',
              'thunderstorm-with-hail': '⛈'}

# Время суток
PART_DAY = {'night': 'ночь',
            'morning': 'утро',
            'day': 'день',
            'evening': 'вечер'}