#!/usr/bin/python3
"""writing a csv file"""


if __name__ == '__main__':
    import requests
    from sys import argv
    import csv


    urlName = requests.get("https://jsonplaceholder.typicode.com/users/{}".
    format(argv[1]))

    urlValue = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1]))
    name = urlName.json().get("name")
    info = urlValue.json()

    total_no_of_task = 0
    number_of_completed_tasks = 0
    for task in info:
        total_no_of_task += 1
        if task.get('completed'):
            number_of_completed_tasks += 1

    header = ["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"]
    
    with open("{}.csv".format(argv[1]), "w") as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(header)
        for task in info:
            writer.writerow([argv[1], name, task.get("completed"), task.get("title")])
