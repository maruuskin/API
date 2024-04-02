import requests


def get_zapr(line):
    return requests.get(line).json()


res = get_zapr('https://swapi.dev/api/people/1/')
res_new = get_zapr('https://swapi.dev/api/people/2/')
films = set(res['films'])
#print(films)
films_new = set(res_new['films'])
print(films & films_new)
print(res_new)
