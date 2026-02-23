def snake_planting(grid):
    result = []
    for i, row in enumerate(grid):
        if i % 2 == 0:
            result.extend(row)
        else:
            result.extend(row[::-1])
    return result

m = int(input("Введіть кількість рядків (m): "))
n = int(input("Введіть кількість стовпців (n): "))

grid = []
print(f"Введіть {m} рядків по {n} чисел через пробіл:")
for i in range(m):
    row = list(map(int, input(f"Рядок {i+1}: ").split()))
    if len(row) != n:
        print(f"Помилка: рядок має містити {n} чисел!")
        exit(1)
    grid.append(row)

result = snake_planting(grid)

print("Послідовність садіння гарбузів за маршрутом робота:")
print(result)