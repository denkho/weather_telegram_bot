import requests
import json
from pprint import pprint

import constants


def get_info_from_api() -> dict:
    """Функция для получения данных о погоде из API Яндекс.Погоды"""
    response = requests.get(constants.URL,
                            headers=constants.HEADERS, 
                            params=constants.PARAMS)

    data = json.loads(response.content)
    return data

#   СОЗДАНИЕ ФАЙЛА ДЛЯ ОТЛАДКИ
#     with open('data_file.json', 'w', encoding='utf8') as f:
#         json.dump(data, f)

    # ДЛЯ ОТЛАДКИ ПО ФАЙЛУ JSON
    # with open('data_file.json', 'r', encoding='utf8') as f:
    #     data = json.load(f)
    # return data
    # # pprint(data['fact'])  # Для отладки смотрим, что есть в файле


def current_weather_output(data: list) -> str:
    """Вывод текущей погоды"""
    temp_feels = data['fact']['feels_like']
    temp_actual = data['fact']['temp']
    conditions = data['fact']['condition']
    wind = data['fact']['wind_speed']
    weather = [f'Сейчас в Воронеже:', 
               f'Температура {temp_actual} {chr(176)}C',
               f'Ощущается как {temp_feels} {chr(176)}C',
               f'{constants.CONDITIONS[conditions].title()} {constants.CONDITIONS_ICONS[conditions]}',
               f'Ветер {wind} м/с'
                ]
    return '\n'.join(weather)
    
def weather_forecast_output(data: list, num_of_day_part: int) -> str:
    """Вывод прогноза погоды на период""" 
    day_part = data['forecast']['parts'][num_of_day_part]['part_name']
    # print(f'\n===ПРОГНОЗ НА {constants.PART_DAY[day_part].upper()}===')
    temp_feels = data['forecast']['parts'][num_of_day_part]['feels_like']
    temp_actual = data['forecast']['parts'][num_of_day_part]['temp_avg']
    conditions = data['forecast']['parts'][num_of_day_part]['condition']
    wind = data['forecast']['parts'][num_of_day_part]['wind_speed']
    print(f'Температура {temp_actual} {chr(176)}C')
    print(f'Будет ощущаться как {temp_feels} {chr(176)}C')
    print(f'{constants.CONDITIONS[conditions].title()} {constants.CONDITIONS_ICONS[conditions]}')
    print(f'Ветер {wind} м/с')
    weather = [
        f'\n===ПРОГНОЗ НА {constants.PART_DAY[day_part].upper()}===',
        f'Температура {temp_actual} {chr(176)}C',
        f'Будет ощущаться как {temp_feels} {chr(176)}C',
        f'{constants.CONDITIONS[conditions].title()} {constants.CONDITIONS_ICONS[conditions]}',
        f'Ветер {wind} м/с'
        ]
    return '\n'.join(weather)
