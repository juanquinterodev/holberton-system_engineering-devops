#!/usr/bin/python3
"""returns information about a given employee ID.
"""
import requests
from sys import argv


if __name__ == "__main__":
    """not execute when imports
    """
    url = "https://jsonplaceholder.typicode.com/"
    request = requests.get("{}users/{}".format(url, argv[1])).json()
    EMPLOYEE_NAME = request["name"]
    TOTAL_NUMBER_OF_TASKS = len(requests.get("{}todos?userId={}"
                                             .format(url, argv[1])).json())
    NUMBER_OF_DONE_TASKS = len(requests.get("{}todos?userId={}&&completed=true"
                                            .format(url, argv[1])).json())
    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    DONE_TASKS = requests.get("{}todos?userId={}&&completed=true"
                              .format(url, argv[1])).json()
    for task in DONE_TASKS:
        print("\t " + task["title"])
