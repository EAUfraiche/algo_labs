from collections import deque

def flood_fill_bfs(field, x, y, target, replacement, h, w):
    queue = deque()
    queue.append((x, y))
    
    while queue:
        cx, cy = queue.popleft()
        
        # межі
        if cx < 0 or cx >= h or cy < 0 or cy >= w:
            continue
        
        # якщо не той колір — пропускаємо
        if field[cx][cy] != target:
            continue
        
        # фарбуємо
        field[cx][cy] = replacement
        
        # додаємо сусідів
        queue.append((cx + 1, cy))
        queue.append((cx - 1, cy))
        queue.append((cx, cy + 1))
        queue.append((cx, cy - 1))


# ---------- ЗЧИТУВАННЯ ----------
with open("input.txt", "r", encoding="utf-8") as f:
    # розміри
    h, w = map(int, f.readline().strip().split(","))
    
    # координати
    x, y = map(int, f.readline().strip().split(","))
    
    # новий колір (гарантовано 1 символ)
    replacement = f.readline().strip().replace("'", "").strip()
    replacement = replacement[0]
    
    # поле
    field = []
    for _ in range(h):
        row = f.readline().strip().split()
        # гарантуємо, що кожен елемент — 1 символ
        row = [cell[0] for cell in row]
        field.append(row)


# ---------- ОБРОБКА ----------
target = field[x][y]

if target != replacement:
    flood_fill_bfs(field, x, y, target, replacement, h, w)


# ---------- ЗАПИС ----------
with open("output.txt", "w", encoding="utf-8") as f:
    for row in field:
        f.write(" ".join(row) + "\n")