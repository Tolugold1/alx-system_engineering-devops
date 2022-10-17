#!/usr/bin/python3
"""writing a csv file"""


if __name__ == '__main__':
    import requests
    from sys import argv
    import json

    id = set()
    post = requests.get("https://jsonplaceholder.typicode.com/post")
    p_Data = post.json()
    for i in p_Data:
        id.add(i.get("userId"))
    
    json_file = {}
    for uid in id:
        N = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(uid))
        V = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(uid))
        name = N.json().get("username")
        info = V.json()

        
        json_file['{}'.format(id)] = []
        for task in info:
            json_file['{}'.format(id)].append({
                'username': name,
                'task': task.get('title'),
                'completed': task.get('completed')
            })

    with open('todo_all_employees.json', 'w') as f:
        json.dump({int(x): json_file[x] for x in json_file.keys()}, f)
