def snake_cleaning(grid, C):
    """
    Робот прибирає підлогу змійкою.
    grid: 2D список підлоги (0 - сміття)
    C: об'єм баку
    Повертає список координат прибраних клітинок.
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
            if grid[y][x] == 0:
                grid[y][x] = 1  
                result.append((y, x))
                collected += 1

            if collected >= C:
                print(f"Бак заповнений! Робот повертається на старт (0,0).")
                x, y = 0, 0
                collected = 0

    return result, (y, x)


m = int(input("Введіть кількість рядків (m): "))
n = int(input("Введіть кількість стовпців (n): "))
C = int(input("Введіть об’єм баку C: "))

grid = []
print(f"Введіть {m} рядків по {n} чисел через пробіл (0 - сміття, інше - чисто):")
for i in range(m):
    row = list(map(int, input(f"Рядок {i+1}: ").split()))
    if len(row) != n:
        print(f"Помилка: рядок має містити {n} чисел!")
        exit(1)
    grid.append(row)

cleaned_cells, final_pos = snake_cleaning(grid, C)

print("\nПослідовність координат прибраних клітинок за маршрутом робота:")
print(cleaned_cells)
print(f"Кінцеві координати робота: {final_pos}")
print(f"Всього прибрано клітинок: {len(cleaned_cells)}")