#!/usr/bin/python3
'''This script  returns information about his/her
TODO list progress using RestApi'''
import requests
import sys
import csv


if __name__ == '__main__':
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        exit()

    base_url = 'https://jsonplaceholder.typicode.com'
    user_url = '{api}/users/{id}'.format(api=base_url, id=employee_id)
    todo_url = '{user_url}/todos'.format(user_url=user_url)

    '''get the user's response'''
    res = requests.get(user_url).json()
    '''get the employee name'''
    name = res.get('name')
    '''Get the todo response'''
    res_todo = requests.get(todo_url).json()
    '''get total number of tasks'''
    total_tasks = len(res)
    '''get the incompleted tasks'''
    non_completed = sum([elem['completed'] is False for elem in res_todo])
    '''get completed tasks'''
    completed_tasks = total_tasks - non_completed
    str = ("Employee {emp_name} is done with tasks" +
           "({completed_tasks}/{total_tasks}): ")
    print(str.format(emp_name=name, completed_tasks=completed_tasks,
                     total_tasks=total_tasks))
    '''print the the complete tasks'''
    for elem in res_todo:
        if elem.get('completed') is True:
            print('\t', elem.get('title'))
    '''write to the csv file'''
    csv_filename = 'USER_ID.csv'
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME",
                             "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in res_todo:
            user_id = employee_id
            username = name
            task_completed_status = "Completed"
            if todo['completed']:
                task_completed_status = "Completed"
            else:
                task_completed_status = "Incomplete"
            task_title = todo['title']
            csv_writer.writerow([user_id, username,
                                 task_completed_status, task_title])
