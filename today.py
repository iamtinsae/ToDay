#!/usr/bin/env python3
from colorama import init
from termcolor import colored
from tabulate import tabulate

from database import Database
# init colorama
init(autoreset=True)



# globals
HEADERS = ['Task Name', 'Duration', 'Priority']

# short hands
pprint = lambda *a: print(colored(*a), end='')

choices = ["List all tasks", "Add a new task", "Update task"]

def format_tasks(tasks):
	priorities_block = ['▁', '▃','▆','█']
	priorities_color = ['red', 'yellow', 'orange', 'green']

	formatted_tasks = []

	for task in tasks:
		idx = int(task[2])
		formatted_tasks.append((task[0], task[1], colored(priorities_block[idx], priorities_color[idx], attrs=['bold'])))

	return formatted_tasks

def main():
	db = Database()
	tasks = db.get_tasks()

	print (tabulate(format_tasks (tasks), headers=HEADERS, tablefmt="fancy_grid"))

	while True:
		pprint("\n".join(map(lambda a: "%d. %s" %a, enumerate(choices, 1))))
		choice = input(colored("\n》", "blue"))


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		pprint ("\nExiting...\n", "red")
