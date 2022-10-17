#!/usr/bin/python3
"""Gather data from an API"""


if __name__ == '__main__':
    import requests
    from sys import argv

    urlName = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                           format(argv[1]))
    name = urlName.json().get('name')
    urlValue = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                            format(argv[1]))
    info = urlValue.json()

    total_no_of_task = 0
    number_of_completed_tasks = 0
    for task in info:
        total_no_of_task += 1
        if task.get('completed'):
            number_of_completed_tasks += 1
    
    print('Employee {} is done with tasks({}/{}):'.format(
        name, number_of_completed_tasks, total_no_of_task))
    for task in info:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))
