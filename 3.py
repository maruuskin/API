import requests


# def get_zapr(line):
#     return requests.get(line).json()
#
#
# res = get_zapr('https://swapi.dev/api/people/1/')
# res_new = get_zapr('https://swapi.dev/api/people/2/')
# films = set(res['films'])
# #print(films)
# films_new = set(res_new['films'])
# print(films & films_new)
# print(res_new)


def magic_help(usual_ev, server=('127.0.0.1', 8080), match=1):
    res = []
    line = f"http://{server[0]}:{server[1]}"
    u_e = set(usual_ev)
    data = requests.get(line).json()
    for event in data:
        unu_e = set(event['event'])
        if len(unu_e & u_e) >= match:
            res.append([', '.join(event["helpers"]), event['usefulness']])
    result = sorted(res, key=lambda x: (x[1], ''.join(x[0])))
    return result
