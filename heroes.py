import requests


def get_json(path):
    response = requests.get(path)
    return response.json()

def get_stat_dict(json):
    superhero = ('Agent Zero', 'Adam Strange', 'Alan Scott')
    dict_stat = {
        item['name']: item['powerstats']['intelligence'] for item in json
        if item['name'] in superhero
    }
    return dict_stat

def key_with_max_value(dict):
    hero_list = [key for key, value in dict.items() if value == max(dict.values())]
    return hero_list


if __name__ == '__main__':
    path = 'https://akabab.github.io/superhero-api/api/all.json'
    content = get_json(path)
    dict_stats = get_stat_dict(content)
    print(*key_with_max_value(dict_stats), sep=', ')