class TaskGraph:
    def __init__(self):
        self.graph = {}

    def add_task(self, task, dependencies):
        self.graph[task] = dependencies

    def get_dependencies(self, task):
        return self.graph.get(task, [])


def dfs(graph, task, visited, schedule):
    if task in visited:
        return

    visited.add(task)

    for dependency in graph.get_dependencies(task):
        dfs(graph, dependency, visited, schedule)

    schedule.append(task)


def task_scheduler(tasks):
    graph = TaskGraph()
    for task, dependencies in tasks.items():
        graph.add_task(task, dependencies)

    visited = set()
    schedule = []

    for task in graph.graph.keys():
        dfs(graph, task, visited, schedule)

    schedule.reverse()
    return schedule


def get_user_input():
    tasks = {}
    while True:
        task_name = input("Enter task name (or 'done' to finish): ")
        if task_name.lower() == 'done':
            break

        dependencies_str = input(f"Enter dependencies for '{task_name}' (comma-separated, or leave empty): ")
        dependencies = [dep.strip() for dep in dependencies_str.split(',') if dep.strip()]
        tasks[task_name] = dependencies

    return tasks


if __name__ == "__main__":
    print("Enter tasks and their dependencies (enter 'done' for task name to finish):")
    tasks = get_user_input()

    schedule = task_scheduler(tasks)
    print("\nOptimized Schedule:")
    for idx, task in enumerate(schedule, start=1):
        print(f"{idx}. {task}")

