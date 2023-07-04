import heapq
from utils import CarMovement
import random
import time


# Task class representing a task with priority and name
class Task:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name

    def __lt__(self, other):
        # Define less than comparison for Task objects based on priority values
        return self.priority.value > other.priority.value


# Priority queue to store tasks
task_queue = []


# Function to add a task to the queue
def add_task(priority, name):
    task = Task(priority, name)
    heapq.heappush(task_queue, task)


# Function to execute tasks based on priority
def execute_tasks():
    # while task_queue:
    task = heapq.heappop(task_queue)
    print("Executing task:", task.name)


if __name__ == "__main__":
    add_task(CarMovement.BACKWARD, f"Task 1: {CarMovement.BACKWARD.name}")
    add_task(CarMovement.LEFT, f"Task 2: {CarMovement.LEFT.name}")
    add_task(CarMovement.STOP, f"Task 3: {CarMovement.STOP.name}")
    # EDF (the task with higher value has earlier deadline)

    t = 4
    while task_queue:
        list_carMovement = list(CarMovement)
        list_carMovement.append(None)
        # print(list_carMovement)
        new_car_movement = random.choice(list_carMovement)
        if new_car_movement is not None:
            add_task(new_car_movement, "Task " + str(t) + ": " + new_car_movement.name)
        print("Task queue:", [task.name for task in task_queue])
        execute_tasks()
        time.sleep(2)
        t += 1
        print()
    print("Done")
