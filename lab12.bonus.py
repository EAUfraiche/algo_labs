def snake_cleaning(grid, C):
    """
    Робот прибирає підлогу змійкою.
    grid: 2D список підлоги (число ≥0 — кількість сміття на клітинці)
    C: об'єм баку
    Повертає список координат прибраних клітинок (y, x) та кількість сміття на кожній.
    """
    m = len(grid)
    n = len(grid[0])
    result = []          
    collected = 0        
    x, y = 0, 0          

    for i, row in enumerate(grid):
        if i % 2 == 0:
            indices = range(n)
        else:
            indices = range(n-1, -1, -1)

        for j in indices:
            y = i
            x = j
            while grid[y][x] > 0:
                space_left = C - collected
                take = min(grid[y][x], space_left)  
                collected += take
                grid[y][x] -= take
                result.append((y, x, take))

                if collected == C:
                    print(f"Бак заповнений! Робот повертається на старт (0,0).")
                    x, y = 0, 0
                    collected = 0  

    return result, (y, x)


m = int(input("Введіть кількість рядків (m): "))
n = int(input("Введіть кількість стовпців (n): "))
C = int(input("Введіть об’єм баку C: "))

grid = []
print(f"Введіть {m} рядків по {n} чисел через пробіл (число ≥0 — кількість сміття на клітинці):")
for i in range(m):
    row = list(map(int, input(f"Рядок {i+1}: ").split()))
    if len(row) != n:
        print(f"Помилка: рядок має містити {n} чисел!")
        exit(1)
    grid.append(row)

cleaned_cells, final_pos = snake_cleaning(grid, C)

print("\nПослідовність прибраних клітинок та кількість сміття на них:")
for y, x, trash in cleaned_cells:
    print(f"Клітинка ({y},{x}) — зібрано сміття: {trash}")

print(f"\nКінцеві координати робота: {final_pos}")
total_trash = sum(trash for _, _, trash in cleaned_cells)
print(f"Всього зібрано сміття: {total_trash}")