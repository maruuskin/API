import os
import sys
from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт
import pygame
import requests
from PIL import Image

import sys
from io import BytesIO
# Этот класс поможет нам сделать картинку из потока байт

import requests
from PIL import Image

RES = WIDTH, HEIGHT = 723, 723


def find_delta(l_corner, up_corner):
    l_corner = l_corner.split()
    up_corner = up_corner.split()
    delta = str(max(abs(float(l_corner[0]) - float(up_corner[0])), abs(float(l_corner[1]) - float(up_corner[1]))) / 3)
    return delta


# Пусть наше приложение предполагает запуск:
# python search.py Москва, ул. Ак. Королева, 12
# Тогда запрос к геокодеру формируется следующим образом:
toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    # обработка ошибочной ситуации
    pass

# Преобразуем ответ в json-объект
json_response = response.json()
# Получаем первый топоним из ответа геокодера.
toponym = json_response["response"]["GeoObjectCollection"][
    "featureMember"][0]["GeoObject"]
# Координаты центра топонима:
toponym_coodrinates = toponym["Point"]["pos"]
# Долгота и широта:
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

delta = "0.005"

# Собираем параметры для запроса к StaticMapsAPI:
map_params = {
    "ll": ",".join([toponym_longitude, toponym_lattitude]),
    "spn": ",".join([delta, delta]),
    "l": "map"
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
# ... и выполняем запрос
response = requests.get(map_api_server, params=map_params)


# def load_image(name, colorkey=None):
#     fullname = os.path.join(name)
#     # если файл не существует, то выходим
#     if not os.path.isfile(fullname):
#         print(f"Файл с изображением '{fullname}' не найден")
#         sys.exit()
#     image = pygame.image.load(fullname)
#     return image

# Image.open(BytesIO(
#     response.content)).show()
# image = Image.open(BytesIO(response.content))
# image = Image.open(BytesIO(response.content))
# image.save("map.png", "PNG")
# image = pygame.image.load("map.png")
# fon = pygame.transform.scale(image, RES)

# if __name__ == '__main__':
pygame.init()
size = WIDTH, HEIGHT = 723, 723
screen = pygame.display.set_mode(size)
image = Image.open(BytesIO(response.content))
image.save("map.png", "PNG")
image = pygame.image.load("map.png")
fon = pygame.transform.scale(image, RES)
# game_surface = pygame.Surface(RES)
# surface = pygame.display.set_mode((WIDTH, HEIGHT))
# surface.blit(game_surface, (0, 0))
# game_surface.blit(fon, (0, 0))
# image = pygame.Surface([100, 100])
# image.fill(pygame.Color("red"))
screen.blit(fon, (0, 0))
pygame.display.flip()
# pygame.quit()
