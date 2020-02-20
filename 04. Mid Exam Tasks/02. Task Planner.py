# Create a program that helps you organize your daily tasks.
# First, you receive the hours each task takes оn a single line, separated by space, in the following format:
# "{task1} {task2} {task3}… {taskn}"
# Each task takes from 1 to 5 hours. If its time is set to 0 – it is completed.
# If its time is set to a negative number – the task is dropped.

# Take Input
task_input = list(int(x) for x in input().split(" "))
command = input().split(' ')

while not command[0] == 'End':
    completed_tasks = task_input.count(0)
    dropped_tasks = task_input.count(-1)
    incomplete_tasks_count = len(task_input) - completed_tasks - dropped_tasks
    if command[0] == 'Complete':
        # Check if the given index is valid
        if 0 <= int(command[1]) < len(task_input):
            index = int(command[1])
            task_input[index] = 0
    elif command[0] == 'Change':
        if 0 <= int(command[1]) < len(task_input):
            index = int(command[1])
            task_input[index] = int(command[2])
    elif command[0] == 'Drop':
        if 0 <= int(command[1]) < len(task_input):
            index = int(command[1])
            task_input[index] = -1
    elif command[1] == 'Completed':
        print(completed_tasks)
    elif command[1] == 'Incomplete':
        print(incomplete_tasks_count)
    elif command[1] == 'Dropped':
        print(dropped_tasks)
    command = input().split(' ')

# Print results
for each_item in task_input:
    if 0 < each_item:
        print(each_item, end=" ")
