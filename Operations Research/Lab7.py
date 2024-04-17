import matplotlib.pyplot as plt

class Task:
    def __init__(self, name, duration, predecessors=None):
        self.name = name  # Nazwa zadania
        self.duration = duration  # Czas trwania zadania
        self.predecessors = predecessors if predecessors else []  # Lista poprzedników zdarzenia
        self.early_start = None  # Najwcześniejszy czas rozpoczęcia
        self.early_finish = None  # Najwcześnieszy czas zakończenia
        self.late_start = None  # Najpóźniejszy czas rozpoczęcia
        self.late_finish = None  # Najpóźniejszy czas zakończenia
        self.total_float = None  # Upływ czasu
        self.successors = []  # Następcy zdarzenia

def cpm(tasks):
    # Przejście w przód:
    for task in tasks:
        if not task.predecessors:
            task.early_start = 0
            task.early_finish = task.duration
        else:
            task.early_start = max(pred.early_finish for pred in task.predecessors)
            task.early_finish = task.early_start + task.duration

    # Przejście w tył
    tasks[-1].late_finish = tasks[-1].early_finish
    tasks[-1].late_start = tasks[-1].late_finish - tasks[-1].duration

    # Idziemy po zdarzeniach od tyłu
    for task in reversed(tasks[:-1]):
        if task.successors and any(succ.late_start is not None for succ in task.successors):
            task.late_finish = min(succ.late_start for succ in task.successors if succ.late_start is not None)
            task.late_start = task.late_finish - task.duration

    # Różnica między najwcześniejszym możliwym terminem rozpoczęcia, a najpóźniejszym
    for task in tasks:
        if task.early_start is not None and task.late_start is not None:
            task.total_float = task.late_start - task.early_start
        else:
            task.total_float = None

    # Szukamy krytycznej ścieżki patrząc, czy dopuszczalne jest jakiekolwiek opóźnienie
    critical_path = [task.name for task in tasks if task.total_float == 0]

    # Obliczamy czas wykonania krytycznej ścieżki
    critical_path_duration = sum(task.duration for task in tasks if task.name in critical_path)

    return critical_path, critical_path_duration

# Tworzymy zdarzenia (Nazwa i długość trwania)
tasks = [
    Task("Task 1", 1),
    Task("Task 2", 5),
    Task("Task 3", 9),
    Task("Task 4", 12),
    Task("Task 5", 9),
    Task("Task 6", 11),
    Task("Task 7", 7),
    Task("Task 8", 8),
    Task("Task 9", 4),
    Task("Task 10", 6),
    Task("Task 11", 3), 
    Task("Task 12", 7), 
    Task("Task 13", 10),
    Task("Task 14", 6), 
    Task("Task 15", 8), 
    Task("Task 16", 5), 
    Task("Task 17", 9), 
    Task("Task 18", 11),
    Task("Task 19", 7), 
    Task("Task 20", 4)  
]

# Ustawiamy relacje między zadaniami (poprzednicy i następcy)
tasks[0].successors = [tasks[1], tasks[2], tasks[3], tasks[10]]
tasks[1].predecessors = [tasks[0]]
tasks[1].successors = [tasks[4]]
tasks[2].predecessors = [tasks[0]]
tasks[2].successors = [tasks[5]]
tasks[3].predecessors = [tasks[0]]
tasks[3].successors = [tasks[6]]
tasks[4].predecessors = [tasks[1]]
tasks[4].successors = [tasks[6]]
tasks[5].predecessors = [tasks[2]]
tasks[5].successors = [tasks[6]]
tasks[6].predecessors = [tasks[3], tasks[4], tasks[5]]
tasks[7].successors = [tasks[8], tasks[9]]
tasks[8].predecessors = [tasks[7]]
tasks[8].successors = [tasks[6]]
tasks[9].predecessors = [tasks[7]]
tasks[10].successors = [tasks[11], tasks[12]]
tasks[10].predecessors = [tasks[0]]
tasks[11].predecessors = [tasks[10]]
tasks[11].successors = [tasks[13]]
tasks[12].predecessors = [tasks[10]]
tasks[12].successors = [tasks[14]]
tasks[13].predecessors = [tasks[11]]
tasks[13].successors = [tasks[15]]
tasks[14].predecessors = [tasks[12]]
tasks[14].successors = [tasks[15]]
tasks[15].predecessors = [tasks[13], tasks[14]]
tasks[15].successors = [tasks[16], tasks[17], tasks[18], tasks[19]]
tasks[16].predecessors = [tasks[15]]
tasks[17].predecessors = [tasks[15]]
tasks[18].predecessors = [tasks[15]]
tasks[19].predecessors = [tasks[15]]


# Wywołujemy funkcję cpm
critical_path, critical_path_duration = cpm(tasks)

# Liczymy liczbę krawędzi
num_edges = sum(len(task.predecessors) for task in tasks)

print(f"Liczba zdarzeń: {len(tasks)}")
print(f"Liczba krawędzi: {num_edges}")
print(f"Czas wykonania krytycznej ścieżki: {critical_path_duration}")
print(f"Ścieżka krytyczna: {critical_path}")

task_names = [task.name for task in tasks]
start_times = [task.early_start for task in tasks]
end_times = [task.early_finish for task in tasks]

critical_tasks = [task.name for task in tasks if task.name in critical_path]

plt.figure(figsize=(10, 5))

for i, task_name in enumerate(task_names):
    plt.barh(task_name, end_times[i] - start_times[i], left=start_times[i], color='b', alpha=0.3)
    if task_name in critical_tasks:
        plt.barh(task_name, end_times[i] - start_times[i], left=start_times[i], color='r', alpha=0.3) 

plt.xlabel('Czas')
plt.ylabel('Zadania')
plt.title('Wykres Gantta')
plt.grid(True)
plt.legend(['Zadanie', 'Zadanie na ścieżce krytycznej'])
plt.show()