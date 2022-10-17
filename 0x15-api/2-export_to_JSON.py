#!/usr/bin/python3
"""writing a csv file"""


if __name__ == '__main__':
    import requests
    from sys import argv
    import json


    N = requests.get("https://jsonplaceholder.typicode.com/users/{}".
    format(argv[1]))

    V = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1]))
    name = N.json().get("username")
    info = V.json()

    json_file = {}
    json_file['{}'.format(argv[1])] = []
    for task in info:
        json_file['{}'.format(argv[1])].append({
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': name
        })

    with open('{}.json'.format(argv[1]), 'w') as f:
        json.dump(json_file, f)
