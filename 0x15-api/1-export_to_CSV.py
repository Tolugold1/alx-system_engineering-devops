#!/usr/bin/python3
"""writing a csv file"""


if __name__ == '__main__':
    import requests
    from sys import argv
    import csv


    N = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(argv[1]))

    V = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                            format(argv[1]))
    username = N.json().get("username")
    info = V.json()
    
    with open("{}.csv".format(argv[1]), "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"',
                                quoting=csv.QUOTE_ALL)

        for task in info:
            writer.writerow([argv[1], username, task.get("completed"), 
                             task.get("title")])
